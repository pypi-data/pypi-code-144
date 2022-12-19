"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.2
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.project_service_identity import ProjectServiceIdentity
from ory_client.model.project_service_o_auth2 import ProjectServiceOAuth2
from ory_client.model.project_service_permission import ProjectServicePermission
globals()['ProjectServiceIdentity'] = ProjectServiceIdentity
globals()['ProjectServiceOAuth2'] = ProjectServiceOAuth2
globals()['ProjectServicePermission'] = ProjectServicePermission
from ory_client.model.project_services import ProjectServices


class TestProjectServices(unittest.TestCase):
    """ProjectServices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProjectServices(self):
        """Test ProjectServices"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProjectServices()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
