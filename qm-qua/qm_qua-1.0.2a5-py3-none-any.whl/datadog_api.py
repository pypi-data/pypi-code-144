import sys
from qm.version import __version__
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.content_encoding import ContentEncoding
from datadog_api_client.v2.model.http_log import HTTPLog
from datadog_api_client.v2.model.http_log_item import HTTPLogItem


from logging import LogRecord
from logging.handlers import BufferingHandler


class DatadogHandler(BufferingHandler):
    def __init__(
        self, user_id: str, organization: str, user_token: str, session_id: str
    ):
        super().__init__(capacity=100)
        self._user_id = user_id
        self._organization = organization
        self._user_token = user_token
        self._session_id = session_id

    def _prepare_record(self, record: LogRecord):
        return HTTPLogItem(
            ddsource="python",
            hostname=self._user_id,
            message=record.msg,
            service=record.name,
            status=record.levelname,
            session_id=str(self._session_id),
            python_version=sys.version,
            qua_version=__version__,
        )

    @property
    def logs_as_http(self):
        _logs = []
        for record in self.buffer:
            _logs.append(self._prepare_record(record))
        return HTTPLog(_logs)

    def send_logs(self):
        configuration = Configuration(
            api_key={"apiKeyAuth": self._user_token},
            server_variables={"site": "datadoghq.eu"},
        )
        with ApiClient(configuration) as api_client:
            api_instance = LogsApi(api_client)
            response = api_instance.submit_log(
                content_encoding=ContentEncoding.GZIP, body=self.logs_as_http
            )
            print(response)

    def flush(self):
        self.send_logs()
        super().flush()
