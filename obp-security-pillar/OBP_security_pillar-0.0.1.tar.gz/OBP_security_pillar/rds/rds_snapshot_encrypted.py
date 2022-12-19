import logging

from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# checks compliance for rds snapshot encrypted
def rds_snapshot_encrypted(self) -> dict:
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside rds :: rds_snapshot_encrypted()")

    result = True
    failReason = ''
    offenders = []
    compliance_type = "RDS snapshot encrypted"
    description = "Checks whether Amazon Relational Database Service (Amazon RDS) DB snapshots are encrypted"
    resource_type = "RDS"

    regions = self.session.get_available_regions('rds')

    for region in regions:
        try:
            client = self.session.client('rds', region_name=region)
            marker = ''
            while True:
                if marker == '' or marker is None:
                    response = client.describe_db_snapshots()
                else:
                    response = client.describe_db_snapshots(
                        Marker=marker
                    )
                for snapshot in response['DBSnapshots']:
                    print(snapshot['DBSnapshotIdentifier'])
                    encryption = snapshot['Encrypted']
                    if not encryption:
                        result = False
                        failReason = 'DB snapshot is not encrypted'
                        offenders.append(snapshot['DBSnapshotIdentifier'])

                try:
                    marker = response['Marker']
                    if marker == '':
                        break
                except KeyError:
                    break
        except ClientError as e:
            logger.error("Something went wrong with the region {}: {}".format(region, e))

    return {
        'Result': result,
        'failReason': failReason,
        'resource_type': resource_type,
        'Offenders': offenders,
        'Compliance_type': compliance_type,
        'Description': description
    }
