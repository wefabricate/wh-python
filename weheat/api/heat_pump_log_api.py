# coding: utf-8

"""
    Weheat Backend

    This is the backend for the Weheat project

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from datetime import datetime

from pydantic import Field, StrictStr

from typing import List, Optional

from weheat.models.heat_pump_log_view_dto import HeatPumpLogViewDto
from weheat.models.raw_heat_pump_log_dto import RawHeatPumpLogDto

from weheat.api_client import ApiClient
from weheat.api_response import ApiResponse
from weheat.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class HeatPumpLogApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def api_v1_heat_pumps_heat_pump_id_logs_get(self, heat_pump_id : Annotated[StrictStr, Field(..., description="The id of the heat pump")], start_time : Annotated[Optional[datetime], Field(description="Start time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)")] = None, end_time : Annotated[Optional[datetime], Field(description="End time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)")] = None, interval : Annotated[Optional[StrictStr], Field(description="Interval granularity of the log data, allowed intervals:                                      \"Minute\", \"FiveMinute\", \"FifteenMinute\", \"Hour\", \"Day\", \"Week\", \"Month\", \"Year\"")] = None, x_version : Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None, **kwargs) -> List[HeatPumpLogViewDto]:  # noqa: E501
        """Gets the heat pump logs of the heat pump in a from start time to end time for a given interval  Correct Intervals include: Minute, FiveMinute, FifteenMinute, Hour, Day, Week, Month, Year  Limits for these intervals are: 2 days, 1 week, 1 month, 1 month, 1 year, 2 years, 5 years, 100 years  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_heat_pumps_heat_pump_id_logs_get(heat_pump_id, start_time, end_time, interval, x_version, async_req=True)
        >>> result = thread.get()

        :param heat_pump_id: The id of the heat pump (required)
        :type heat_pump_id: str
        :param start_time: Start time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)
        :type start_time: datetime
        :param end_time: End time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)
        :type end_time: datetime
        :param interval: Interval granularity of the log data, allowed intervals:                                      \"Minute\", \"FiveMinute\", \"FifteenMinute\", \"Hour\", \"Day\", \"Week\", \"Month\", \"Year\"
        :type interval: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[HeatPumpLogViewDto]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the api_v1_heat_pumps_heat_pump_id_logs_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.api_v1_heat_pumps_heat_pump_id_logs_get_with_http_info(heat_pump_id, start_time, end_time, interval, x_version, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_heat_pumps_heat_pump_id_logs_get_with_http_info(self, heat_pump_id : Annotated[StrictStr, Field(..., description="The id of the heat pump")], start_time : Annotated[Optional[datetime], Field(description="Start time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)")] = None, end_time : Annotated[Optional[datetime], Field(description="End time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)")] = None, interval : Annotated[Optional[StrictStr], Field(description="Interval granularity of the log data, allowed intervals:                                      \"Minute\", \"FiveMinute\", \"FifteenMinute\", \"Hour\", \"Day\", \"Week\", \"Month\", \"Year\"")] = None, x_version : Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Gets the heat pump logs of the heat pump in a from start time to end time for a given interval  Correct Intervals include: Minute, FiveMinute, FifteenMinute, Hour, Day, Week, Month, Year  Limits for these intervals are: 2 days, 1 week, 1 month, 1 month, 1 year, 2 years, 5 years, 100 years  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_heat_pumps_heat_pump_id_logs_get_with_http_info(heat_pump_id, start_time, end_time, interval, x_version, async_req=True)
        >>> result = thread.get()

        :param heat_pump_id: The id of the heat pump (required)
        :type heat_pump_id: str
        :param start_time: Start time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)
        :type start_time: datetime
        :param end_time: End time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)
        :type end_time: datetime
        :param interval: Interval granularity of the log data, allowed intervals:                                      \"Minute\", \"FiveMinute\", \"FifteenMinute\", \"Hour\", \"Day\", \"Week\", \"Month\", \"Year\"
        :type interval: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[HeatPumpLogViewDto], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'heat_pump_id',
            'start_time',
            'end_time',
            'interval',
            'x_version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_heat_pumps_heat_pump_id_logs_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['heat_pump_id'] is not None:
            _path_params['heatPumpId'] = _params['heat_pump_id']


        # process the query parameters
        _query_params = []
        if _params.get('start_time') is not None:  # noqa: E501
            if isinstance(_params['start_time'], datetime):
                _query_params.append(('startTime', _params['start_time'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('startTime', _params['start_time']))

        if _params.get('end_time') is not None:  # noqa: E501
            if isinstance(_params['end_time'], datetime):
                _query_params.append(('endTime', _params['end_time'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('endTime', _params['end_time']))

        if _params.get('interval') is not None:  # noqa: E501
            _query_params.append(('interval', _params['interval']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['x_version'] is not None:
            _header_params['x-version'] = _params['x_version']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '403': "str",
            '505': None,
            '200': "List[HeatPumpLogViewDto]",
            '400': None,
            '404': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/heat-pumps/{heatPumpId}/logs', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_v1_heat_pumps_heat_pump_id_logs_latest_get(self, heat_pump_id : Annotated[StrictStr, Field(..., description="The id of the heat pump")], x_version : Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None, **kwargs) -> RawHeatPumpLogDto:  # noqa: E501
        """Gets the latest raw heat pump log of the heat pump  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_heat_pumps_heat_pump_id_logs_latest_get(heat_pump_id, x_version, async_req=True)
        >>> result = thread.get()

        :param heat_pump_id: The id of the heat pump (required)
        :type heat_pump_id: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RawHeatPumpLogDto
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the api_v1_heat_pumps_heat_pump_id_logs_latest_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.api_v1_heat_pumps_heat_pump_id_logs_latest_get_with_http_info(heat_pump_id, x_version, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_heat_pumps_heat_pump_id_logs_latest_get_with_http_info(self, heat_pump_id : Annotated[StrictStr, Field(..., description="The id of the heat pump")], x_version : Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Gets the latest raw heat pump log of the heat pump  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_heat_pumps_heat_pump_id_logs_latest_get_with_http_info(heat_pump_id, x_version, async_req=True)
        >>> result = thread.get()

        :param heat_pump_id: The id of the heat pump (required)
        :type heat_pump_id: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(RawHeatPumpLogDto, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'heat_pump_id',
            'x_version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_heat_pumps_heat_pump_id_logs_latest_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['heat_pump_id'] is not None:
            _path_params['heatPumpId'] = _params['heat_pump_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['x_version'] is not None:
            _header_params['x-version'] = _params['x_version']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '403': "str",
            '505': None,
            '200': "RawHeatPumpLogDto",
            '404': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/heat-pumps/{heatPumpId}/logs/latest', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_v1_heat_pumps_heat_pump_id_logs_raw_get(self, heat_pump_id : Annotated[StrictStr, Field(..., description="The id of the heat pump")], start_time : Annotated[Optional[datetime], Field(description="Start time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)")] = None, end_time : Annotated[Optional[datetime], Field(description="End time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)")] = None, x_version : Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None, **kwargs) -> List[RawHeatPumpLogDto]:  # noqa: E501
        """Gets the raw heat pump logs of the heat pump in a from start time to end time for a given interval.  Maximum interval is 4 hours.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_heat_pumps_heat_pump_id_logs_raw_get(heat_pump_id, start_time, end_time, x_version, async_req=True)
        >>> result = thread.get()

        :param heat_pump_id: The id of the heat pump (required)
        :type heat_pump_id: str
        :param start_time: Start time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)
        :type start_time: datetime
        :param end_time: End time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)
        :type end_time: datetime
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[RawHeatPumpLogDto]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the api_v1_heat_pumps_heat_pump_id_logs_raw_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.api_v1_heat_pumps_heat_pump_id_logs_raw_get_with_http_info(heat_pump_id, start_time, end_time, x_version, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_heat_pumps_heat_pump_id_logs_raw_get_with_http_info(self, heat_pump_id : Annotated[StrictStr, Field(..., description="The id of the heat pump")], start_time : Annotated[Optional[datetime], Field(description="Start time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)")] = None, end_time : Annotated[Optional[datetime], Field(description="End time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)")] = None, x_version : Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Gets the raw heat pump logs of the heat pump in a from start time to end time for a given interval.  Maximum interval is 4 hours.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_heat_pumps_heat_pump_id_logs_raw_get_with_http_info(heat_pump_id, start_time, end_time, x_version, async_req=True)
        >>> result = thread.get()

        :param heat_pump_id: The id of the heat pump (required)
        :type heat_pump_id: str
        :param start_time: Start time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)
        :type start_time: datetime
        :param end_time: End time of the interval as a DateTime object in UTC (format: yyyy-MM-dd HH:mm:ss)
        :type end_time: datetime
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[RawHeatPumpLogDto], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'heat_pump_id',
            'start_time',
            'end_time',
            'x_version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_heat_pumps_heat_pump_id_logs_raw_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['heat_pump_id'] is not None:
            _path_params['heatPumpId'] = _params['heat_pump_id']


        # process the query parameters
        _query_params = []
        if _params.get('start_time') is not None:  # noqa: E501
            if isinstance(_params['start_time'], datetime):
                _query_params.append(('startTime', _params['start_time'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('startTime', _params['start_time']))

        if _params.get('end_time') is not None:  # noqa: E501
            if isinstance(_params['end_time'], datetime):
                _query_params.append(('endTime', _params['end_time'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('endTime', _params['end_time']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['x_version'] is not None:
            _header_params['x-version'] = _params['x_version']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '403': "str",
            '505': None,
            '200': "List[RawHeatPumpLogDto]",
            '400': None,
            '404': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/heat-pumps/{heatPumpId}/logs/raw', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))