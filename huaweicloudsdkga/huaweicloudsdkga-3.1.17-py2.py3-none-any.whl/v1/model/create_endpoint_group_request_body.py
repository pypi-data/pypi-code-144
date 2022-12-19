# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_group': 'CreateEndpointGroupOption'
    }

    attribute_map = {
        'endpoint_group': 'endpoint_group'
    }

    def __init__(self, endpoint_group=None):
        """CreateEndpointGroupRequestBody

        The model defined in huaweicloud sdk

        :param endpoint_group: 
        :type endpoint_group: :class:`huaweicloudsdkga.v1.CreateEndpointGroupOption`
        """
        
        

        self._endpoint_group = None
        self.discriminator = None

        self.endpoint_group = endpoint_group

    @property
    def endpoint_group(self):
        """Gets the endpoint_group of this CreateEndpointGroupRequestBody.

        :return: The endpoint_group of this CreateEndpointGroupRequestBody.
        :rtype: :class:`huaweicloudsdkga.v1.CreateEndpointGroupOption`
        """
        return self._endpoint_group

    @endpoint_group.setter
    def endpoint_group(self, endpoint_group):
        """Sets the endpoint_group of this CreateEndpointGroupRequestBody.

        :param endpoint_group: The endpoint_group of this CreateEndpointGroupRequestBody.
        :type endpoint_group: :class:`huaweicloudsdkga.v1.CreateEndpointGroupOption`
        """
        self._endpoint_group = endpoint_group

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
        if not isinstance(other, CreateEndpointGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
