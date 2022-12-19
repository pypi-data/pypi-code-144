# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricConfig:

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
        'type': 'str',
        'threshold': 'int',
        'min': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'threshold': 'threshold',
        'min': 'min'
    }

    def __init__(self, name=None, type=None, threshold=None, min=None):
        """MetricConfig

        The model defined in huaweicloud sdk

        :param name: 流量配置名称
        :type name: str
        :param type: 流量配置类型
        :type type: str
        :param threshold: 流量阈值
        :type threshold: int
        :param min: 流量最小值
        :type min: int
        """
        
        

        self._name = None
        self._type = None
        self._threshold = None
        self._min = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if threshold is not None:
            self.threshold = threshold
        if min is not None:
            self.min = min

    @property
    def name(self):
        """Gets the name of this MetricConfig.

        流量配置名称

        :return: The name of this MetricConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricConfig.

        流量配置名称

        :param name: The name of this MetricConfig.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this MetricConfig.

        流量配置类型

        :return: The type of this MetricConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MetricConfig.

        流量配置类型

        :param type: The type of this MetricConfig.
        :type type: str
        """
        self._type = type

    @property
    def threshold(self):
        """Gets the threshold of this MetricConfig.

        流量阈值

        :return: The threshold of this MetricConfig.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this MetricConfig.

        流量阈值

        :param threshold: The threshold of this MetricConfig.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def min(self):
        """Gets the min of this MetricConfig.

        流量最小值

        :return: The min of this MetricConfig.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this MetricConfig.

        流量最小值

        :param min: The min of this MetricConfig.
        :type min: int
        """
        self._min = min

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
        if not isinstance(other, MetricConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
