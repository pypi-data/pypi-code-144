# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IvsStandardByNameAndIdRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'meta': 'Meta',
        'data': 'IvsStandardByNameAndIdRequestBodyData'
    }

    attribute_map = {
        'meta': 'meta',
        'data': 'data'
    }

    def __init__(self, meta=None, data=None):
        """IvsStandardByNameAndIdRequestBody

        The model defined in huaweicloud sdk

        :param meta: 
        :type meta: :class:`huaweicloudsdkivs.v2.Meta`
        :param data: 
        :type data: :class:`huaweicloudsdkivs.v2.IvsStandardByNameAndIdRequestBodyData`
        """
        
        

        self._meta = None
        self._data = None
        self.discriminator = None

        self.meta = meta
        self.data = data

    @property
    def meta(self):
        """Gets the meta of this IvsStandardByNameAndIdRequestBody.

        :return: The meta of this IvsStandardByNameAndIdRequestBody.
        :rtype: :class:`huaweicloudsdkivs.v2.Meta`
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this IvsStandardByNameAndIdRequestBody.

        :param meta: The meta of this IvsStandardByNameAndIdRequestBody.
        :type meta: :class:`huaweicloudsdkivs.v2.Meta`
        """
        self._meta = meta

    @property
    def data(self):
        """Gets the data of this IvsStandardByNameAndIdRequestBody.

        :return: The data of this IvsStandardByNameAndIdRequestBody.
        :rtype: :class:`huaweicloudsdkivs.v2.IvsStandardByNameAndIdRequestBodyData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this IvsStandardByNameAndIdRequestBody.

        :param data: The data of this IvsStandardByNameAndIdRequestBody.
        :type data: :class:`huaweicloudsdkivs.v2.IvsStandardByNameAndIdRequestBodyData`
        """
        self._data = data

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
        if not isinstance(other, IvsStandardByNameAndIdRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
