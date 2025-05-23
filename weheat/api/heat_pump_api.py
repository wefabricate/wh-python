# coding: utf-8

"""
    Weheat Backend

    This is the backend for the Weheat project

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictInt, StrictStr

from typing import List, Optional

from weheat.models.device_state import DeviceState
from weheat.models.read_all_heat_pump_dto import ReadAllHeatPumpDto
from weheat.models.read_heat_pump_dto import ReadHeatPumpDto

from weheat.api_client import ApiClient
from weheat.api_response import ApiResponse
from weheat.rest import RESTResponseType


class HeatPumpApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def api_v1_heat_pumps_get(
        self,
        search: Annotated[Optional[StrictStr], Field(description="String with keywords (split by spaces) to search on SN, PN and Name of a heat pump")] = None,
        page: Annotated[Optional[StrictInt], Field(description="The page number")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="The page size")] = None,
        state: Annotated[Optional[DeviceState], Field(description="Filter for which device state the heat pump should be in using Device")] = None,
        generic_model: Annotated[Optional[StrictStr], Field(description="Filter for which generic model the heat pump should have")] = None,
        x_version: Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[ReadAllHeatPumpDto]:
        """Gets all heat pumps (Paged, Searchable)


        :param search: String with keywords (split by spaces) to search on SN, PN and Name of a heat pump
        :type search: str
        :param page: The page number
        :type page: int
        :param page_size: The page size
        :type page_size: int
        :param state: Filter for which device state the heat pump should be in using Device
        :type state: DeviceState
        :param generic_model: Filter for which generic model the heat pump should have
        :type generic_model: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_heat_pumps_get_serialize(
            search=search,
            page=page,
            page_size=page_size,
            state=state,
            generic_model=generic_model,
            x_version=x_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '403': "str",
            '500': None,
            '505': None,
            '200': "List[ReadAllHeatPumpDto]",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def api_v1_heat_pumps_get_with_http_info(
        self,
        search: Annotated[Optional[StrictStr], Field(description="String with keywords (split by spaces) to search on SN, PN and Name of a heat pump")] = None,
        page: Annotated[Optional[StrictInt], Field(description="The page number")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="The page size")] = None,
        state: Annotated[Optional[DeviceState], Field(description="Filter for which device state the heat pump should be in using Device")] = None,
        generic_model: Annotated[Optional[StrictStr], Field(description="Filter for which generic model the heat pump should have")] = None,
        x_version: Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[ReadAllHeatPumpDto]]:
        """Gets all heat pumps (Paged, Searchable)


        :param search: String with keywords (split by spaces) to search on SN, PN and Name of a heat pump
        :type search: str
        :param page: The page number
        :type page: int
        :param page_size: The page size
        :type page_size: int
        :param state: Filter for which device state the heat pump should be in using Device
        :type state: DeviceState
        :param generic_model: Filter for which generic model the heat pump should have
        :type generic_model: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_heat_pumps_get_serialize(
            search=search,
            page=page,
            page_size=page_size,
            state=state,
            generic_model=generic_model,
            x_version=x_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '403': "str",
            '500': None,
            '505': None,
            '200': "List[ReadAllHeatPumpDto]",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def api_v1_heat_pumps_get_without_preload_content(
        self,
        search: Annotated[Optional[StrictStr], Field(description="String with keywords (split by spaces) to search on SN, PN and Name of a heat pump")] = None,
        page: Annotated[Optional[StrictInt], Field(description="The page number")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="The page size")] = None,
        state: Annotated[Optional[DeviceState], Field(description="Filter for which device state the heat pump should be in using Device")] = None,
        generic_model: Annotated[Optional[StrictStr], Field(description="Filter for which generic model the heat pump should have")] = None,
        x_version: Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Gets all heat pumps (Paged, Searchable)


        :param search: String with keywords (split by spaces) to search on SN, PN and Name of a heat pump
        :type search: str
        :param page: The page number
        :type page: int
        :param page_size: The page size
        :type page_size: int
        :param state: Filter for which device state the heat pump should be in using Device
        :type state: DeviceState
        :param generic_model: Filter for which generic model the heat pump should have
        :type generic_model: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_heat_pumps_get_serialize(
            search=search,
            page=page,
            page_size=page_size,
            state=state,
            generic_model=generic_model,
            x_version=x_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '403': "str",
            '500': None,
            '505': None,
            '200': "List[ReadAllHeatPumpDto]",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_heat_pumps_get_serialize(
        self,
        search,
        page,
        page_size,
        state,
        generic_model,
        x_version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if search is not None:
            
            _query_params.append(('search', search))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if state is not None:
            
            _query_params.append(('state', state.value))
            
        if generic_model is not None:
            
            _query_params.append(('genericModel', generic_model))
            
        # process the header parameters
        if x_version is not None:
            _header_params['x-version'] = x_version
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'text/plain', 
                'application/json', 
                'text/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/heat-pumps',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


    @validate_call
    async def api_v1_heat_pumps_heat_pump_id_get(
        self,
        heat_pump_id: Annotated[StrictStr, Field(description="The heatPumpId of the heat pump you want to get")],
        x_version: Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ReadHeatPumpDto:
        """Gets a heat pump by heatPumpId


        :param heat_pump_id: The heatPumpId of the heat pump you want to get (required)
        :type heat_pump_id: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_heat_pumps_heat_pump_id_get_serialize(
            heat_pump_id=heat_pump_id,
            x_version=x_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '403': "str",
            '500': None,
            '505': None,
            '200': "ReadHeatPumpDto",
            '404': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def api_v1_heat_pumps_heat_pump_id_get_with_http_info(
        self,
        heat_pump_id: Annotated[StrictStr, Field(description="The heatPumpId of the heat pump you want to get")],
        x_version: Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ReadHeatPumpDto]:
        """Gets a heat pump by heatPumpId


        :param heat_pump_id: The heatPumpId of the heat pump you want to get (required)
        :type heat_pump_id: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_heat_pumps_heat_pump_id_get_serialize(
            heat_pump_id=heat_pump_id,
            x_version=x_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '403': "str",
            '500': None,
            '505': None,
            '200': "ReadHeatPumpDto",
            '404': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def api_v1_heat_pumps_heat_pump_id_get_without_preload_content(
        self,
        heat_pump_id: Annotated[StrictStr, Field(description="The heatPumpId of the heat pump you want to get")],
        x_version: Annotated[Optional[StrictStr], Field(description="Optional version parameter for frontend applications to check if an update / refresh is needed")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Gets a heat pump by heatPumpId


        :param heat_pump_id: The heatPumpId of the heat pump you want to get (required)
        :type heat_pump_id: str
        :param x_version: Optional version parameter for frontend applications to check if an update / refresh is needed
        :type x_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_v1_heat_pumps_heat_pump_id_get_serialize(
            heat_pump_id=heat_pump_id,
            x_version=x_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '403': "str",
            '500': None,
            '505': None,
            '200': "ReadHeatPumpDto",
            '404': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_v1_heat_pumps_heat_pump_id_get_serialize(
        self,
        heat_pump_id,
        x_version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if heat_pump_id is not None:
            _path_params['heatPumpId'] = heat_pump_id
        # process the query parameters
        # process the header parameters
        if x_version is not None:
            _header_params['x-version'] = x_version
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'text/plain', 
                'application/json', 
                'text/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/heat-pumps/{heatPumpId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


