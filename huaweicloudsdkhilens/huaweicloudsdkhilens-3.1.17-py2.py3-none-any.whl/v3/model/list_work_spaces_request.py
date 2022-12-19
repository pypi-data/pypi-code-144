# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkSpacesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iam_user_id': 'str'
    }

    attribute_map = {
        'iam_user_id': 'iam_user_id'
    }

    def __init__(self, iam_user_id=None):
        """ListWorkSpacesRequest

        The model defined in huaweicloud sdk

        :param iam_user_id: 用户的userId，用于查询指定的的子工作空间
        :type iam_user_id: str
        """
        
        

        self._iam_user_id = None
        self.discriminator = None

        if iam_user_id is not None:
            self.iam_user_id = iam_user_id

    @property
    def iam_user_id(self):
        """Gets the iam_user_id of this ListWorkSpacesRequest.

        用户的userId，用于查询指定的的子工作空间

        :return: The iam_user_id of this ListWorkSpacesRequest.
        :rtype: str
        """
        return self._iam_user_id

    @iam_user_id.setter
    def iam_user_id(self, iam_user_id):
        """Sets the iam_user_id of this ListWorkSpacesRequest.

        用户的userId，用于查询指定的的子工作空间

        :param iam_user_id: The iam_user_id of this ListWorkSpacesRequest.
        :type iam_user_id: str
        """
        self._iam_user_id = iam_user_id

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
        if not isinstance(other, ListWorkSpacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
