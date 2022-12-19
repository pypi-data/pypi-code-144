# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoints': 'list[EndpointResp]'
    }

    attribute_map = {
        'endpoints': 'endpoints'
    }

    def __init__(self, endpoints=None):
        """UpdateEndpointResponse

        The model defined in huaweicloud sdk

        :param endpoints: 
        :type endpoints: list[:class:`huaweicloudsdkdns.v2.EndpointResp`]
        """
        
        super(UpdateEndpointResponse, self).__init__()

        self._endpoints = None
        self.discriminator = None

        if endpoints is not None:
            self.endpoints = endpoints

    @property
    def endpoints(self):
        """Gets the endpoints of this UpdateEndpointResponse.

        :return: The endpoints of this UpdateEndpointResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.EndpointResp`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this UpdateEndpointResponse.

        :param endpoints: The endpoints of this UpdateEndpointResponse.
        :type endpoints: list[:class:`huaweicloudsdkdns.v2.EndpointResp`]
        """
        self._endpoints = endpoints

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateEndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
