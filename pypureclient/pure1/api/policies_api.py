# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from ..api_client import ApiClient


class PoliciesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api10_policies_file_system_snapshots_get(self, **kwargs):
        """Get policy / file system snapshot pairs

        Retrieves pairs of policy references and their file system snapshot members. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api10_policies_file_system_snapshots_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the continuation_token field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] member_ids: A comma-separated list of member IDs. If there is not at least one member that matches each of the elements of `member_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] member_names: A comma-separated list of member names. If there is not at least one member that matches each of the elements of `member_names`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If there is not at least one policy that matches each of the elements of `policy_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_names: A comma-separated list of policy names. If there is not at least one policy that matches each of the elements of `policy_names`, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :return: PolicyMembersGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api10_policies_file_system_snapshots_get_with_http_info(**kwargs)
        else:
            (data) = self.api10_policies_file_system_snapshots_get_with_http_info(**kwargs)
            return data

    def api10_policies_file_system_snapshots_get_with_http_info(self, **kwargs):
        """Get policy / file system snapshot pairs

        Retrieves pairs of policy references and their file system snapshot members. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api10_policies_file_system_snapshots_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the continuation_token field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] member_ids: A comma-separated list of member IDs. If there is not at least one member that matches each of the elements of `member_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] member_names: A comma-separated list of member names. If there is not at least one member that matches each of the elements of `member_names`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If there is not at least one policy that matches each of the elements of `policy_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_names: A comma-separated list of policy names. If there is not at least one policy that matches each of the elements of `policy_names`, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :return: PolicyMembersGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_request_id', 'continuation_token', 'filter', 'limit', 'member_ids', 'member_names', 'policy_ids', 'policy_names', 'offset', 'sort']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api10_policies_file_system_snapshots_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api10_policies_file_system_snapshots_get`, must be a value greater than or equal to `0`")
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'member_ids' in params:
            query_params.append(('member_ids', params['member_ids']))
            collection_formats['member_ids'] = 'csv'
        if 'member_names' in params:
            query_params.append(('member_names', params['member_names']))
            collection_formats['member_names'] = 'csv'
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.0/policies/file-system-snapshots', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyMembersGetResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api10_policies_file_systems_get(self, **kwargs):
        """Get policy / file system pairs

        Retrieves pairs of policy references and their file system members. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api10_policies_file_systems_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the continuation_token field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] member_ids: A comma-separated list of member IDs. If there is not at least one member that matches each of the elements of `member_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] member_names: A comma-separated list of member names. If there is not at least one member that matches each of the elements of `member_names`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If there is not at least one policy that matches each of the elements of `policy_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_names: A comma-separated list of policy names. If there is not at least one policy that matches each of the elements of `policy_names`, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :return: PolicyMembersGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api10_policies_file_systems_get_with_http_info(**kwargs)
        else:
            (data) = self.api10_policies_file_systems_get_with_http_info(**kwargs)
            return data

    def api10_policies_file_systems_get_with_http_info(self, **kwargs):
        """Get policy / file system pairs

        Retrieves pairs of policy references and their file system members. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api10_policies_file_systems_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the continuation_token field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] member_ids: A comma-separated list of member IDs. If there is not at least one member that matches each of the elements of `member_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] member_names: A comma-separated list of member names. If there is not at least one member that matches each of the elements of `member_names`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If there is not at least one policy that matches each of the elements of `policy_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_names: A comma-separated list of policy names. If there is not at least one policy that matches each of the elements of `policy_names`, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :return: PolicyMembersGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_request_id', 'continuation_token', 'filter', 'limit', 'member_ids', 'member_names', 'policy_ids', 'policy_names', 'offset', 'sort']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api10_policies_file_systems_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api10_policies_file_systems_get`, must be a value greater than or equal to `0`")
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'member_ids' in params:
            query_params.append(('member_ids', params['member_ids']))
            collection_formats['member_ids'] = 'csv'
        if 'member_names' in params:
            query_params.append(('member_names', params['member_names']))
            collection_formats['member_names'] = 'csv'
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.0/policies/file-systems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyMembersGetResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api10_policies_get(self, **kwargs):
        """Get policies

        Retrieves policies and their rules. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api10_policies_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the continuation_token field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param list[str] ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each of the elements of ids, an error is returned. Single quotes are required around all strings.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of names, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :return: PolicyGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api10_policies_get_with_http_info(**kwargs)
        else:
            (data) = self.api10_policies_get_with_http_info(**kwargs)
            return data

    def api10_policies_get_with_http_info(self, **kwargs):
        """Get policies

        Retrieves policies and their rules. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api10_policies_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the continuation_token field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param list[str] ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each of the elements of ids, an error is returned. Single quotes are required around all strings.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of names, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :return: PolicyGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_request_id', 'continuation_token', 'filter', 'ids', 'limit', 'names', 'offset', 'sort']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api10_policies_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api10_policies_get`, must be a value greater than or equal to `0`")
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.0/policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyGetResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api10_policies_members_get(self, **kwargs):
        """Get policy / member pairs

        Retrieves pairs of policy references and their members. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api10_policies_members_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the continuation_token field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] member_ids: A comma-separated list of member IDs. If there is not at least one member that matches each of the elements of `member_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] member_names: A comma-separated list of member names. If there is not at least one member that matches each of the elements of `member_names`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If there is not at least one policy that matches each of the elements of `policy_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_names: A comma-separated list of policy names. If there is not at least one policy that matches each of the elements of `policy_names`, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :return: PolicyMembersGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api10_policies_members_get_with_http_info(**kwargs)
        else:
            (data) = self.api10_policies_members_get_with_http_info(**kwargs)
            return data

    def api10_policies_members_get_with_http_info(self, **kwargs):
        """Get policy / member pairs

        Retrieves pairs of policy references and their members. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api10_policies_members_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the continuation_token field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] member_ids: A comma-separated list of member IDs. If there is not at least one member that matches each of the elements of `member_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] member_names: A comma-separated list of member names. If there is not at least one member that matches each of the elements of `member_names`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If there is not at least one policy that matches each of the elements of `policy_ids`, an error is returned. Single quotes are required around all strings.
        :param list[str] policy_names: A comma-separated list of policy names. If there is not at least one policy that matches each of the elements of `policy_names`, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :return: PolicyMembersGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_request_id', 'continuation_token', 'filter', 'limit', 'member_ids', 'member_names', 'policy_ids', 'policy_names', 'offset', 'sort']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api10_policies_members_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api10_policies_members_get`, must be a value greater than or equal to `0`")
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'member_ids' in params:
            query_params.append(('member_ids', params['member_ids']))
            collection_formats['member_ids'] = 'csv'
        if 'member_names' in params:
            query_params.append(('member_names', params['member_names']))
            collection_formats['member_names'] = 'csv'
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.0/policies/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyMembersGetResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
