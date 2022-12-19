# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'job_count': 'int',
        'jobs': 'list[ListJobsJobs]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_count': 'job_count',
        'jobs': 'jobs'
    }

    def __init__(self, is_success=None, message=None, job_count=None, jobs=None):
        """ListJobsResponse

        The model defined in huaweicloud sdk

        :param is_success: 请求发送是否成功。“true”表示请求发送成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param job_count: 作业总个数。
        :type job_count: int
        :param jobs: 作业信息。
        :type jobs: list[:class:`huaweicloudsdkdli.v1.ListJobsJobs`]
        """
        
        super(ListJobsResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_count = None
        self._jobs = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_count is not None:
            self.job_count = job_count
        if jobs is not None:
            self.jobs = jobs

    @property
    def is_success(self):
        """Gets the is_success of this ListJobsResponse.

        请求发送是否成功。“true”表示请求发送成功。

        :return: The is_success of this ListJobsResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListJobsResponse.

        请求发送是否成功。“true”表示请求发送成功。

        :param is_success: The is_success of this ListJobsResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListJobsResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ListJobsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListJobsResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ListJobsResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_count(self):
        """Gets the job_count of this ListJobsResponse.

        作业总个数。

        :return: The job_count of this ListJobsResponse.
        :rtype: int
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count):
        """Sets the job_count of this ListJobsResponse.

        作业总个数。

        :param job_count: The job_count of this ListJobsResponse.
        :type job_count: int
        """
        self._job_count = job_count

    @property
    def jobs(self):
        """Gets the jobs of this ListJobsResponse.

        作业信息。

        :return: The jobs of this ListJobsResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.ListJobsJobs`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ListJobsResponse.

        作业信息。

        :param jobs: The jobs of this ListJobsResponse.
        :type jobs: list[:class:`huaweicloudsdkdli.v1.ListJobsJobs`]
        """
        self._jobs = jobs

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
        if not isinstance(other, ListJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
