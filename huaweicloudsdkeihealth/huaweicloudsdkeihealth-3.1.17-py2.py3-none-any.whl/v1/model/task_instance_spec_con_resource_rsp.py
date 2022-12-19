# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInstanceSpecConResourceRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limits': 'TaskInstanceSpecConResLimitRsp',
        'requests': 'TaskInstanceSpecConResRequestRsp'
    }

    attribute_map = {
        'limits': 'limits',
        'requests': 'requests'
    }

    def __init__(self, limits=None, requests=None):
        """TaskInstanceSpecConResourceRsp

        The model defined in huaweicloud sdk

        :param limits: 
        :type limits: :class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecConResLimitRsp`
        :param requests: 
        :type requests: :class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecConResRequestRsp`
        """
        
        

        self._limits = None
        self._requests = None
        self.discriminator = None

        if limits is not None:
            self.limits = limits
        if requests is not None:
            self.requests = requests

    @property
    def limits(self):
        """Gets the limits of this TaskInstanceSpecConResourceRsp.

        :return: The limits of this TaskInstanceSpecConResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecConResLimitRsp`
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this TaskInstanceSpecConResourceRsp.

        :param limits: The limits of this TaskInstanceSpecConResourceRsp.
        :type limits: :class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecConResLimitRsp`
        """
        self._limits = limits

    @property
    def requests(self):
        """Gets the requests of this TaskInstanceSpecConResourceRsp.

        :return: The requests of this TaskInstanceSpecConResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecConResRequestRsp`
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this TaskInstanceSpecConResourceRsp.

        :param requests: The requests of this TaskInstanceSpecConResourceRsp.
        :type requests: :class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecConResRequestRsp`
        """
        self._requests = requests

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
        if not isinstance(other, TaskInstanceSpecConResourceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
