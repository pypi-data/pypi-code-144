import datetime
import io
import itertools
import logging
import threading
import time
from collections import defaultdict

import requests
from dateutil import parser
from pydicom import dcmread
from pynetdicom import AE

from echoloader.lib import unpack

logger = logging.getLogger('echolog')
DEFAULT_AE_TITLE = "Us2.ai"


class PacsConnection:
    def __init__(self, details):
        parts = details.split(':')
        self.host, port, self.remote_ae_title = parts[:3]
        self.local_ae_title = parts[3] if len(parts) > 3 else DEFAULT_AE_TITLE
        self.port = int(port)

    def store(self, ds):
        ae = AE(ae_title=self.local_ae_title)
        ae.add_requested_context(ds.SOPClassUID, ds.file_meta.TransferSyntaxUID)
        assoc = ae.associate(self.host, self.port, ae_title=self.remote_ae_title)
        if not assoc.is_established:
            raise ConnectionError('Association rejected, aborted or never connected')
        # Use the C-STORE service to send the dataset
        # returns the response status as a pydicom Dataset
        try:
            # force treat context as supporting the SCP role
            for cx in assoc.accepted_contexts:
                cx._as_scp = True

            status = assoc.send_c_store(ds)

            # Check the status of the storage request
            if status:
                # If the storage request succeeded this will be 0x0000
                logger.debug(f'C-STORE request status: 0x{status.Status:04x}')
            else:
                raise ValueError('Connection timed out, was aborted or received invalid response')
        finally:
            # Release the association
            assoc.release()

    def __str__(self):
        return f"{self.host}:{self.port}"


class Sync(threading.Thread):
    def __init__(self, cmd, pool, *vargs, **kwargs):
        super().__init__(*vargs, **kwargs)
        self.args = cmd
        self.connections = cmd.sync
        self.auth = cmd.auth
        self.api_url = self.auth.api_url
        self.uploader = self.auth.username
        self.killed = False
        self.search = f"{self.api_url}/study/search?uploader={self.uploader}&reportCompleted=true"
        self.last_sync = datetime.datetime.min.replace(tzinfo=datetime.timezone.utc)
        self.modalities = cmd.sync_modalities
        self.sr_params = {}
        self.pool = pool
        self.protocol = unpack(requests.get(
            f'{self.api_url}/sync/protocol', headers=self.auth.get_headers()))['current_protocol']
        if cmd.sync_url:
            self.sr_params['url'] = True
        if cmd.sync_main_findings:
            self.sr_params['main_findings'] = True
        if cmd.sync_designators:
            self.sr_params['designators'] = cmd.sync_designators
        self.ps_params = {}
        self.sc_params = {}

    def sr(self, sid):
        return requests.get(f"{self.api_url}/study/sr/{sid}", headers=self.auth.get_headers(), params=self.sr_params)

    def ps(self, ms):
        return requests.get(f"{self.api_url}/dicom/ps", headers=self.auth.get_headers(),
                            params={**self.ps_params, 'measurements': ms})

    def sc(self, ms):
        return requests.get(f"{self.api_url}/dicom/sc", headers=self.auth.get_headers(),
                            params={**self.sc_params, 'measurements': ms})

    def media(self, sid, t):
        mods = unpack(requests.get(
            f"{self.api_url}/sync/modification/{sid}", headers=self.auth.get_headers()))
        ms = defaultdict(dict)
        for mod in mods:
            if mod['model'] == 'measurement.measurements':
                pk = mod['obj_pk']
                ms[pk].update(mod['new_fields'])
                ms[pk]['last_update'] = parser.parse(mod['creation']).replace(tzinfo=datetime.timezone.utc)
                if mod['action'] == 'delete' and pk in ms:
                    del ms[pk]
        by_dcm_frame = defaultdict(list)
        for m in ms.values():
            proto = self.protocol.get('measurements', {}).get(str(m.get('code_id')), {})
            if (proto.get('shouldDisplay')
                    and m['last_update'] > t
                    and m.get('used')
                    and m.get('dicom_id')
                    and m.get('plot_obj')):
                by_dcm_frame[m['dicom_id'], m['frame']].append(m['id'])
        for ms in by_dcm_frame.values():
            if 'PS' in self.modalities:
                yield self.ps(ms)
            if 'SC' in self.modalities:
                yield self.sc(ms)

    def latest_mod(self, sid):
        return unpack(requests.get(
            f"{self.api_url}/sync/modification/{sid}", params={'limit': 1}, headers=self.auth.get_headers()))[0]

    def stop(self):
        self.killed = True

    def sync_study(self, sid, t):
        for req in itertools.chain(
                self.media(sid, t) if [m in self.modalities for m in ['PS', 'SC']] else [],
                [self.sr(sid)] if 'SR' in self.modalities else [],
        ):
            url = req.url
            try:
                bs = unpack(req)
            except Exception as exc:
                logger.error(f'Failed to fetch {url} due to {exc}')
                continue
            ds = dcmread(io.BytesIO(bs))
            for conn in self.connections:
                try:
                    conn.store(ds)
                    logger.info(f'Synced {url} to {conn}')
                except Exception as exc:
                    logger.error(f'Failed to sync {url} due to {exc}')

    def handle_study_sync_error(self, err, sid):
        logger.error(f'Failed to sync study {sid} due to {err}')

    def sync(self):
        t = self.last_sync
        res = unpack(requests.get(self.search, headers=self.auth.get_headers()), {})
        results = res.get('results', [])
        for study in results:
            sid = study['id']
            mod = self.latest_mod(sid)
            creation = parser.parse(mod['creation']).replace(tzinfo=datetime.timezone.utc)
            if creation > self.last_sync:
                self.pool.apply_async(self.sync_study, [sid, self.last_sync],
                                      error_callback=lambda err: self.handle_study_sync_error(err, sid))
            t = max(creation, t)
        self.last_sync = t

    def run(self) -> None:
        while not self.killed:
            try:
                self.sync()
            except Exception as exc:
                logger.error(f'Failed sync due to: {exc}')
            time.sleep(10)
