# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipResourcesAvailableV3RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'type': 'type',
        'limit': 'limit'
    }

    def __init__(self, type=None, limit=None):
        """EipResourcesAvailableV3RequestBody

        The model defined in huaweicloud sdk

        :param type: 公共池类型
        :type type: str
        :param limit: 查询的公共池数量
        :type limit: int
        """
        
        

        self._type = None
        self._limit = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.limit = limit

    @property
    def type(self):
        """Gets the type of this EipResourcesAvailableV3RequestBody.

        公共池类型

        :return: The type of this EipResourcesAvailableV3RequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EipResourcesAvailableV3RequestBody.

        公共池类型

        :param type: The type of this EipResourcesAvailableV3RequestBody.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this EipResourcesAvailableV3RequestBody.

        查询的公共池数量

        :return: The limit of this EipResourcesAvailableV3RequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this EipResourcesAvailableV3RequestBody.

        查询的公共池数量

        :param limit: The limit of this EipResourcesAvailableV3RequestBody.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, EipResourcesAvailableV3RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
