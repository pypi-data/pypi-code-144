# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineDeleteStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, name=None, status=None):
        """PipelineDeleteStatus

        The model defined in huaweicloud sdk

        :param name: 流水线名称
        :type name: str
        :param status: 流水线删除状态,deleted:删除成功,failed:删除失败,going:正在删除中
        :type status: str
        """
        
        

        self._name = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Gets the name of this PipelineDeleteStatus.

        流水线名称

        :return: The name of this PipelineDeleteStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineDeleteStatus.

        流水线名称

        :param name: The name of this PipelineDeleteStatus.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this PipelineDeleteStatus.

        流水线删除状态,deleted:删除成功,failed:删除失败,going:正在删除中

        :return: The status of this PipelineDeleteStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PipelineDeleteStatus.

        流水线删除状态,deleted:删除成功,failed:删除失败,going:正在删除中

        :param status: The status of this PipelineDeleteStatus.
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
        if not isinstance(other, PipelineDeleteStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
