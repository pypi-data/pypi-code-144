# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_group_id': 'str',
        'endpoint_id': 'str',
        'body': 'UpdateEndpointRequestBody'
    }

    attribute_map = {
        'endpoint_group_id': 'endpoint_group_id',
        'endpoint_id': 'endpoint_id',
        'body': 'body'
    }

    def __init__(self, endpoint_group_id=None, endpoint_id=None, body=None):
        """UpdateEndpointRequest

        The model defined in huaweicloud sdk

        :param endpoint_group_id: 终端节点组ID。
        :type endpoint_group_id: str
        :param endpoint_id: 终端节点ID。
        :type endpoint_id: str
        :param body: Body of the UpdateEndpointRequest
        :type body: :class:`huaweicloudsdkga.v1.UpdateEndpointRequestBody`
        """
        
        

        self._endpoint_group_id = None
        self._endpoint_id = None
        self._body = None
        self.discriminator = None

        self.endpoint_group_id = endpoint_group_id
        self.endpoint_id = endpoint_id
        if body is not None:
            self.body = body

    @property
    def endpoint_group_id(self):
        """Gets the endpoint_group_id of this UpdateEndpointRequest.

        终端节点组ID。

        :return: The endpoint_group_id of this UpdateEndpointRequest.
        :rtype: str
        """
        return self._endpoint_group_id

    @endpoint_group_id.setter
    def endpoint_group_id(self, endpoint_group_id):
        """Sets the endpoint_group_id of this UpdateEndpointRequest.

        终端节点组ID。

        :param endpoint_group_id: The endpoint_group_id of this UpdateEndpointRequest.
        :type endpoint_group_id: str
        """
        self._endpoint_group_id = endpoint_group_id

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this UpdateEndpointRequest.

        终端节点ID。

        :return: The endpoint_id of this UpdateEndpointRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this UpdateEndpointRequest.

        终端节点ID。

        :param endpoint_id: The endpoint_id of this UpdateEndpointRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def body(self):
        """Gets the body of this UpdateEndpointRequest.

        :return: The body of this UpdateEndpointRequest.
        :rtype: :class:`huaweicloudsdkga.v1.UpdateEndpointRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateEndpointRequest.

        :param body: The body of this UpdateEndpointRequest.
        :type body: :class:`huaweicloudsdkga.v1.UpdateEndpointRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateEndpointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
