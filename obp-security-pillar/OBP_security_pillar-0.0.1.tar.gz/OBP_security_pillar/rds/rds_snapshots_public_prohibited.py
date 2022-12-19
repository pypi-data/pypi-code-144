import logging

from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# checks compliance for rds snapshot public prohibited
def rds_snapshots_public_prohibited(self) -> dict:
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside rds :: rds_snapshots_public_prohibited")

    result = True
    failReason = ''
    offenders = []
    compliance_type = "RDS snapshot public prohibited"
    description = "Checks if Amazon Relational Database Service (Amazon RDS) snapshots are public"
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
                    res = client.describe_db_snapshot_attributes(
                        DBSnapshotIdentifier=snapshot['DBSnapshotIdentifier']
                    )
                    for attribute in res['DBSnapshotAttributesResult']['DBSnapshotAttributes']:
                        if attribute['AttributeName'] == 'restore':
                            if 'all' in attribute['AttributeValues']:
                                result = False
                                failReason = 'Amazon RDS database snapshot is publicly accessible and available for ' \
                                             'any AWS account to copy or restore it '
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