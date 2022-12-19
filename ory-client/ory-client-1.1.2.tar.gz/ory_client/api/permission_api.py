"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.2
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ory_client.api_client import ApiClient, Endpoint as _Endpoint
from ory_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ory_client.model.check_permission_result import CheckPermissionResult
from ory_client.model.error_generic import ErrorGeneric
from ory_client.model.expanded_permission_tree import ExpandedPermissionTree
from ory_client.model.post_check_permission_body import PostCheckPermissionBody
from ory_client.model.post_check_permission_or_error_body import PostCheckPermissionOrErrorBody


class PermissionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.check_permission_endpoint = _Endpoint(
            settings={
                'response_type': (CheckPermissionResult,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/relation-tuples/check/openapi',
                'operation_id': 'check_permission',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'namespace',
                    'object',
                    'relation',
                    'subject_id',
                    'subject_set_namespace',
                    'subject_set_object',
                    'subject_set_relation',
                    'max_depth',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'namespace':
                        (str,),
                    'object':
                        (str,),
                    'relation':
                        (str,),
                    'subject_id':
                        (str,),
                    'subject_set_namespace':
                        (str,),
                    'subject_set_object':
                        (str,),
                    'subject_set_relation':
                        (str,),
                    'max_depth':
                        (int,),
                },
                'attribute_map': {
                    'namespace': 'namespace',
                    'object': 'object',
                    'relation': 'relation',
                    'subject_id': 'subject_id',
                    'subject_set_namespace': 'subject_set.namespace',
                    'subject_set_object': 'subject_set.object',
                    'subject_set_relation': 'subject_set.relation',
                    'max_depth': 'max-depth',
                },
                'location_map': {
                    'namespace': 'query',
                    'object': 'query',
                    'relation': 'query',
                    'subject_id': 'query',
                    'subject_set_namespace': 'query',
                    'subject_set_object': 'query',
                    'subject_set_relation': 'query',
                    'max_depth': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.check_permission_or_error_endpoint = _Endpoint(
            settings={
                'response_type': (CheckPermissionResult,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/relation-tuples/check',
                'operation_id': 'check_permission_or_error',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'namespace',
                    'object',
                    'relation',
                    'subject_id',
                    'subject_set_namespace',
                    'subject_set_object',
                    'subject_set_relation',
                    'max_depth',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'namespace':
                        (str,),
                    'object':
                        (str,),
                    'relation':
                        (str,),
                    'subject_id':
                        (str,),
                    'subject_set_namespace':
                        (str,),
                    'subject_set_object':
                        (str,),
                    'subject_set_relation':
                        (str,),
                    'max_depth':
                        (int,),
                },
                'attribute_map': {
                    'namespace': 'namespace',
                    'object': 'object',
                    'relation': 'relation',
                    'subject_id': 'subject_id',
                    'subject_set_namespace': 'subject_set.namespace',
                    'subject_set_object': 'subject_set.object',
                    'subject_set_relation': 'subject_set.relation',
                    'max_depth': 'max-depth',
                },
                'location_map': {
                    'namespace': 'query',
                    'object': 'query',
                    'relation': 'query',
                    'subject_id': 'query',
                    'subject_set_namespace': 'query',
                    'subject_set_object': 'query',
                    'subject_set_relation': 'query',
                    'max_depth': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.expand_permissions_endpoint = _Endpoint(
            settings={
                'response_type': (ExpandedPermissionTree,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/relation-tuples/expand',
                'operation_id': 'expand_permissions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'namespace',
                    'object',
                    'relation',
                    'max_depth',
                ],
                'required': [
                    'namespace',
                    'object',
                    'relation',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'namespace':
                        (str,),
                    'object':
                        (str,),
                    'relation':
                        (str,),
                    'max_depth':
                        (int,),
                },
                'attribute_map': {
                    'namespace': 'namespace',
                    'object': 'object',
                    'relation': 'relation',
                    'max_depth': 'max-depth',
                },
                'location_map': {
                    'namespace': 'query',
                    'object': 'query',
                    'relation': 'query',
                    'max_depth': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.post_check_permission_endpoint = _Endpoint(
            settings={
                'response_type': (CheckPermissionResult,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/relation-tuples/check/openapi',
                'operation_id': 'post_check_permission',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'max_depth',
                    'post_check_permission_body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'max_depth':
                        (int,),
                    'post_check_permission_body':
                        (PostCheckPermissionBody,),
                },
                'attribute_map': {
                    'max_depth': 'max-depth',
                },
                'location_map': {
                    'max_depth': 'query',
                    'post_check_permission_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.post_check_permission_or_error_endpoint = _Endpoint(
            settings={
                'response_type': (CheckPermissionResult,),
                'auth': [
                    'oryAccessToken'
                ],
                'endpoint_path': '/relation-tuples/check',
                'operation_id': 'post_check_permission_or_error',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'max_depth',
                    'post_check_permission_or_error_body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'max_depth':
                        (int,),
                    'post_check_permission_or_error_body':
                        (PostCheckPermissionOrErrorBody,),
                },
                'attribute_map': {
                    'max_depth': 'max-depth',
                },
                'location_map': {
                    'max_depth': 'query',
                    'post_check_permission_or_error_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def check_permission(
        self,
        **kwargs
    ):
        """Check a permission  # noqa: E501

        To learn how relationship tuples and the check works, head over to [the documentation](https://www.ory.sh/docs/keto/concepts/api-overview).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_permission(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            namespace (str): Namespace of the Relationship. [optional]
            object (str): Object of the Relationship. [optional]
            relation (str): Relation of the Relationship. [optional]
            subject_id (str): SubjectID of the Relationship. [optional]
            subject_set_namespace (str): Namespace of the Subject Set. [optional]
            subject_set_object (str): Object of the Subject Set. [optional]
            subject_set_relation (str): Relation of the Subject Set. [optional]
            max_depth (int): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CheckPermissionResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.check_permission_endpoint.call_with_http_info(**kwargs)

    def check_permission_or_error(
        self,
        **kwargs
    ):
        """Check a permission  # noqa: E501

        To learn how relationship tuples and the check works, head over to [the documentation](https://www.ory.sh/docs/keto/concepts/api-overview).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_permission_or_error(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            namespace (str): Namespace of the Relationship. [optional]
            object (str): Object of the Relationship. [optional]
            relation (str): Relation of the Relationship. [optional]
            subject_id (str): SubjectID of the Relationship. [optional]
            subject_set_namespace (str): Namespace of the Subject Set. [optional]
            subject_set_object (str): Object of the Subject Set. [optional]
            subject_set_relation (str): Relation of the Subject Set. [optional]
            max_depth (int): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CheckPermissionResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.check_permission_or_error_endpoint.call_with_http_info(**kwargs)

    def expand_permissions(
        self,
        namespace,
        object,
        relation,
        **kwargs
    ):
        """Expand a Relationship into permissions.  # noqa: E501

        Use this endpoint to expand a relationship tuple into permissions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.expand_permissions(namespace, object, relation, async_req=True)
        >>> result = thread.get()

        Args:
            namespace (str): Namespace of the Subject Set
            object (str): Object of the Subject Set
            relation (str): Relation of the Subject Set

        Keyword Args:
            max_depth (int): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ExpandedPermissionTree
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['namespace'] = \
            namespace
        kwargs['object'] = \
            object
        kwargs['relation'] = \
            relation
        return self.expand_permissions_endpoint.call_with_http_info(**kwargs)

    def post_check_permission(
        self,
        **kwargs
    ):
        """Check a permission  # noqa: E501

        To learn how relationship tuples and the check works, head over to [the documentation](https://www.ory.sh/docs/keto/concepts/api-overview).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_check_permission(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            max_depth (int): [optional]
            post_check_permission_body (PostCheckPermissionBody): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CheckPermissionResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.post_check_permission_endpoint.call_with_http_info(**kwargs)

    def post_check_permission_or_error(
        self,
        **kwargs
    ):
        """Check a permission  # noqa: E501

        To learn how relationship tuples and the check works, head over to [the documentation](https://www.ory.sh/docs/keto/concepts/api-overview).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_check_permission_or_error(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            max_depth (int): [optional]
            post_check_permission_or_error_body (PostCheckPermissionOrErrorBody): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CheckPermissionResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.post_check_permission_or_error_endpoint.call_with_http_info(**kwargs)

