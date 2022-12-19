# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRunRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'run_id': 'str',
        'with_details': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'run_id': 'run_id',
        'with_details': 'with_details'
    }

    def __init__(self, job_id=None, run_id=None, with_details=None):
        """ShowRunRequest

        The model defined in huaweicloud sdk

        :param job_id: 作业ID。
        :type job_id: str
        :param run_id: 作业运行ID。
        :type run_id: str
        :param with_details: 是否查询作业详情。true：查询；false：不查询。details属性为空。默认为false。
        :type with_details: bool
        """
        
        

        self._job_id = None
        self._run_id = None
        self._with_details = None
        self.discriminator = None

        self.job_id = job_id
        self.run_id = run_id
        if with_details is not None:
            self.with_details = with_details

    @property
    def job_id(self):
        """Gets the job_id of this ShowRunRequest.

        作业ID。

        :return: The job_id of this ShowRunRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowRunRequest.

        作业ID。

        :param job_id: The job_id of this ShowRunRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def run_id(self):
        """Gets the run_id of this ShowRunRequest.

        作业运行ID。

        :return: The run_id of this ShowRunRequest.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ShowRunRequest.

        作业运行ID。

        :param run_id: The run_id of this ShowRunRequest.
        :type run_id: str
        """
        self._run_id = run_id

    @property
    def with_details(self):
        """Gets the with_details of this ShowRunRequest.

        是否查询作业详情。true：查询；false：不查询。details属性为空。默认为false。

        :return: The with_details of this ShowRunRequest.
        :rtype: bool
        """
        return self._with_details

    @with_details.setter
    def with_details(self, with_details):
        """Sets the with_details of this ShowRunRequest.

        是否查询作业详情。true：查询；false：不查询。details属性为空。默认为false。

        :param with_details: The with_details of this ShowRunRequest.
        :type with_details: bool
        """
        self._with_details = with_details

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
        if not isinstance(other, ShowRunRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
