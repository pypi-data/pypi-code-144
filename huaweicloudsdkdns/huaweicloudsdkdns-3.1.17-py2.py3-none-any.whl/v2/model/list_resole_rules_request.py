# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResoleRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, domain_name=None, limit=None, offset=None):
        """ListResoleRulesRequest

        The model defined in huaweicloud sdk

        :param domain_name: 待查询的resolverrule的域名。
        :type domain_name: str
        :param limit: 每页返回的资源个数。 取值范围：0~500，取值一般为10，20，50。
        :type limit: int
        :param offset: 分页查询起始页码，起始值为0。 当前设置marker不为空时，以marker为分页起始标识。取值范围：0~2147483647。
        :type offset: int
        """
        
        

        self._domain_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def domain_name(self):
        """Gets the domain_name of this ListResoleRulesRequest.

        待查询的resolverrule的域名。

        :return: The domain_name of this ListResoleRulesRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListResoleRulesRequest.

        待查询的resolverrule的域名。

        :param domain_name: The domain_name of this ListResoleRulesRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def limit(self):
        """Gets the limit of this ListResoleRulesRequest.

        每页返回的资源个数。 取值范围：0~500，取值一般为10，20，50。

        :return: The limit of this ListResoleRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResoleRulesRequest.

        每页返回的资源个数。 取值范围：0~500，取值一般为10，20，50。

        :param limit: The limit of this ListResoleRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListResoleRulesRequest.

        分页查询起始页码，起始值为0。 当前设置marker不为空时，以marker为分页起始标识。取值范围：0~2147483647。

        :return: The offset of this ListResoleRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListResoleRulesRequest.

        分页查询起始页码，起始值为0。 当前设置marker不为空时，以marker为分页起始标识。取值范围：0~2147483647。

        :param offset: The offset of this ListResoleRulesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListResoleRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
