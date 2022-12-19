# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPauseResumeStutusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str'
    }

    attribute_map = {
        'status': 'status'
    }

    def __init__(self, status=None):
        """ShowPauseResumeStutusResponse

        The model defined in huaweicloud sdk

        :param status: 容灾实例数据同步状态 - NA：实例尚未搭建容灾关系 - NEW：尚未启动的数据同步状态 - SYNCING：数据同步正常进行中 - SUSPENDING：正在暂停数据同步 - SUSPENDED：数据同步已暂停 - RECOVERYING：正在恢复数据同步
        :type status: str
        """
        
        super(ShowPauseResumeStutusResponse, self).__init__()

        self._status = None
        self.discriminator = None

        if status is not None:
            self.status = status

    @property
    def status(self):
        """Gets the status of this ShowPauseResumeStutusResponse.

        容灾实例数据同步状态 - NA：实例尚未搭建容灾关系 - NEW：尚未启动的数据同步状态 - SYNCING：数据同步正常进行中 - SUSPENDING：正在暂停数据同步 - SUSPENDED：数据同步已暂停 - RECOVERYING：正在恢复数据同步

        :return: The status of this ShowPauseResumeStutusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowPauseResumeStutusResponse.

        容灾实例数据同步状态 - NA：实例尚未搭建容灾关系 - NEW：尚未启动的数据同步状态 - SYNCING：数据同步正常进行中 - SUSPENDING：正在暂停数据同步 - SUSPENDED：数据同步已暂停 - RECOVERYING：正在恢复数据同步

        :param status: The status of this ShowPauseResumeStutusResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowPauseResumeStutusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
