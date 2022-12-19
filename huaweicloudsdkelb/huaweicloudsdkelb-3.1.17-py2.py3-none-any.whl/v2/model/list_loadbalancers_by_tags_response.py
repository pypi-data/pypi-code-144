# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLoadbalancersByTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'resources': 'list[ResourcesByTag]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'resources': 'resources'
    }

    def __init__(self, total_count=None, resources=None):
        """ListLoadbalancersByTagsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总记录数。当resources为空时，表示名称为matches字段中指定的value的负载均衡器个数；resources不为空时，表示和tags字段匹配的负载均衡器的个数。
        :type total_count: int
        :param resources: 根据tag查询出的负载均衡器对象。 当请求中的action为filters，返回体中有该字段。 当请求中的action为count时，返回体中无该字段。
        :type resources: list[:class:`huaweicloudsdkelb.v2.ResourcesByTag`]
        """
        
        super(ListLoadbalancersByTagsResponse, self).__init__()

        self._total_count = None
        self._resources = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if resources is not None:
            self.resources = resources

    @property
    def total_count(self):
        """Gets the total_count of this ListLoadbalancersByTagsResponse.

        总记录数。当resources为空时，表示名称为matches字段中指定的value的负载均衡器个数；resources不为空时，表示和tags字段匹配的负载均衡器的个数。

        :return: The total_count of this ListLoadbalancersByTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListLoadbalancersByTagsResponse.

        总记录数。当resources为空时，表示名称为matches字段中指定的value的负载均衡器个数；resources不为空时，表示和tags字段匹配的负载均衡器的个数。

        :param total_count: The total_count of this ListLoadbalancersByTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def resources(self):
        """Gets the resources of this ListLoadbalancersByTagsResponse.

        根据tag查询出的负载均衡器对象。 当请求中的action为filters，返回体中有该字段。 当请求中的action为count时，返回体中无该字段。

        :return: The resources of this ListLoadbalancersByTagsResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v2.ResourcesByTag`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListLoadbalancersByTagsResponse.

        根据tag查询出的负载均衡器对象。 当请求中的action为filters，返回体中有该字段。 当请求中的action为count时，返回体中无该字段。

        :param resources: The resources of this ListLoadbalancersByTagsResponse.
        :type resources: list[:class:`huaweicloudsdkelb.v2.ResourcesByTag`]
        """
        self._resources = resources

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
        if not isinstance(other, ListLoadbalancersByTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
