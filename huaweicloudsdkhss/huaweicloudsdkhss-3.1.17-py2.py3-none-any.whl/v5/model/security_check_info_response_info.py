# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity': 'str',
        'check_name': 'str',
        'check_type': 'str',
        'standard': 'str',
        'check_rule_num': 'int',
        'failed_rule_num': 'int',
        'host_num': 'int',
        'scan_time': 'int',
        'check_type_desc': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'check_name': 'check_name',
        'check_type': 'check_type',
        'standard': 'standard',
        'check_rule_num': 'check_rule_num',
        'failed_rule_num': 'failed_rule_num',
        'host_num': 'host_num',
        'scan_time': 'scan_time',
        'check_type_desc': 'check_type_desc'
    }

    def __init__(self, severity=None, check_name=None, check_type=None, standard=None, check_rule_num=None, failed_rule_num=None, host_num=None, scan_time=None, check_type_desc=None):
        """SecurityCheckInfoResponseInfo

        The model defined in huaweicloud sdk

        :param severity: 风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危
        :type severity: str
        :param check_name: 基线名称
        :type check_name: str
        :param check_type: 基线类型
        :type check_type: str
        :param standard: 标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准
        :type standard: str
        :param check_rule_num: 检查项数量
        :type check_rule_num: int
        :param failed_rule_num: 风险项数量
        :type failed_rule_num: int
        :param host_num: 影响的服务器数量
        :type host_num: int
        :param scan_time: 最新检测时间
        :type scan_time: int
        :param check_type_desc: 基线描述信息
        :type check_type_desc: str
        """
        
        

        self._severity = None
        self._check_name = None
        self._check_type = None
        self._standard = None
        self._check_rule_num = None
        self._failed_rule_num = None
        self._host_num = None
        self._scan_time = None
        self._check_type_desc = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if check_name is not None:
            self.check_name = check_name
        if check_type is not None:
            self.check_type = check_type
        if standard is not None:
            self.standard = standard
        if check_rule_num is not None:
            self.check_rule_num = check_rule_num
        if failed_rule_num is not None:
            self.failed_rule_num = failed_rule_num
        if host_num is not None:
            self.host_num = host_num
        if scan_time is not None:
            self.scan_time = scan_time
        if check_type_desc is not None:
            self.check_type_desc = check_type_desc

    @property
    def severity(self):
        """Gets the severity of this SecurityCheckInfoResponseInfo.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :return: The severity of this SecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this SecurityCheckInfoResponseInfo.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :param severity: The severity of this SecurityCheckInfoResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_name(self):
        """Gets the check_name of this SecurityCheckInfoResponseInfo.

        基线名称

        :return: The check_name of this SecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        """Sets the check_name of this SecurityCheckInfoResponseInfo.

        基线名称

        :param check_name: The check_name of this SecurityCheckInfoResponseInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_type(self):
        """Gets the check_type of this SecurityCheckInfoResponseInfo.

        基线类型

        :return: The check_type of this SecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this SecurityCheckInfoResponseInfo.

        基线类型

        :param check_type: The check_type of this SecurityCheckInfoResponseInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        """Gets the standard of this SecurityCheckInfoResponseInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准

        :return: The standard of this SecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this SecurityCheckInfoResponseInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准

        :param standard: The standard of this SecurityCheckInfoResponseInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def check_rule_num(self):
        """Gets the check_rule_num of this SecurityCheckInfoResponseInfo.

        检查项数量

        :return: The check_rule_num of this SecurityCheckInfoResponseInfo.
        :rtype: int
        """
        return self._check_rule_num

    @check_rule_num.setter
    def check_rule_num(self, check_rule_num):
        """Sets the check_rule_num of this SecurityCheckInfoResponseInfo.

        检查项数量

        :param check_rule_num: The check_rule_num of this SecurityCheckInfoResponseInfo.
        :type check_rule_num: int
        """
        self._check_rule_num = check_rule_num

    @property
    def failed_rule_num(self):
        """Gets the failed_rule_num of this SecurityCheckInfoResponseInfo.

        风险项数量

        :return: The failed_rule_num of this SecurityCheckInfoResponseInfo.
        :rtype: int
        """
        return self._failed_rule_num

    @failed_rule_num.setter
    def failed_rule_num(self, failed_rule_num):
        """Sets the failed_rule_num of this SecurityCheckInfoResponseInfo.

        风险项数量

        :param failed_rule_num: The failed_rule_num of this SecurityCheckInfoResponseInfo.
        :type failed_rule_num: int
        """
        self._failed_rule_num = failed_rule_num

    @property
    def host_num(self):
        """Gets the host_num of this SecurityCheckInfoResponseInfo.

        影响的服务器数量

        :return: The host_num of this SecurityCheckInfoResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this SecurityCheckInfoResponseInfo.

        影响的服务器数量

        :param host_num: The host_num of this SecurityCheckInfoResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def scan_time(self):
        """Gets the scan_time of this SecurityCheckInfoResponseInfo.

        最新检测时间

        :return: The scan_time of this SecurityCheckInfoResponseInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        """Sets the scan_time of this SecurityCheckInfoResponseInfo.

        最新检测时间

        :param scan_time: The scan_time of this SecurityCheckInfoResponseInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def check_type_desc(self):
        """Gets the check_type_desc of this SecurityCheckInfoResponseInfo.

        基线描述信息

        :return: The check_type_desc of this SecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._check_type_desc

    @check_type_desc.setter
    def check_type_desc(self, check_type_desc):
        """Sets the check_type_desc of this SecurityCheckInfoResponseInfo.

        基线描述信息

        :param check_type_desc: The check_type_desc of this SecurityCheckInfoResponseInfo.
        :type check_type_desc: str
        """
        self._check_type_desc = check_type_desc

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
        if not isinstance(other, SecurityCheckInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
