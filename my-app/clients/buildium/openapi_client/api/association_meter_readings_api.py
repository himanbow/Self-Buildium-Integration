# coding: utf-8

"""
    Open API, powered by Buildium

      # Introduction  ### Welcome!    Welcome to Buildium’s API—a powerful, RESTful programming interface that lets you leverage valuable Buildium data.    Using HTTP requests, you can create integrations with applications that specialize in accounting, lead tracking, and more. Enjoy greater flexibility, transparency, and control over your business!      ### What's in this Guide?    This guide is full of simple, easy-to-follow instructions that’ll help you use Buildium’s API like a pro.    Topics include:    * choosing the right resources for your use case  * making HTTP requests to any resource  * understanding data and response codes    <br />    # Getting Started  Excited to get going? We’ll walk you through the setup process.  >  **Note:** To take advantage of the Buildium Open API you must have a <a target=\"_blank\" href=\"https://www.buildium.com/pricing/\">**Premium Subscription**</a>.    ## Account Configuration  Before you can use Buildium’s API, you’ll need to make some tweaks to your account settings.    <br />    ### Enabling the API  In order to start creating your keys and making requests, you’ll need to enable the API.      >  **Tip:** You’ll need an administrator user role with access to ***Application settings*** to set things up properly.    <br />    ​ **Let's Begin!**    1. Sign in to your [Buildium](https://signin.managebuilding.com/manager/public/authentication/login?ReturnUrl=%2Fmanager%2F) account from your browser.    2. Open the ***Settings*** menu and click ***Application settings***.    3. Under ***System preferences***, click ***Api settings***. A modal will appear.    4. Click the ***Open API*** toggle to turn it on. Then click ***Save***.    <video width=\"100%\" autoplay loop muted>    <source src=\"enable_open_api.mp4\" type=\"video/mp4\" />  </video>      Congratulations! Your account's enabled. Now, you’re ready to start managing API keys.  <br />  <br />  If you are having issues enabling the API within your account you can submit a [Support](#section/API-Overview/Support) request for assistance.    <br />      ## API Keys  Account-level API keys authenticate every request and keep things secure.    API keys have two components: a “client ID” and a “secret”.    * **Client IDs** are similar to usernames. They’re used to identify your Buildium account and are safe to share.  * **Secrets** are similar to passwords. They must be kept confidential.    Whenever you make a request, you’ll need the API key’s client ID and secret. If you forget it, make a mistake, or try to use information that’s linked to a deleted key, the API will return a `401` response code.    >  **Tip:** We compiled a list of best practices that detail how securely store API keys. [Give it a read](#section/Getting-Started/Keeping-API-Keys-Safe)!    ## Creating API Keys  Now that the Open APi is enabled, you’ll be able to create API keys. You’re almost there!    >  **Tip:** You’ll need an administrator user role to complete this step, too.    <br />    **How to create an API key**    1. Sign in to your [Buildium](https://signin.managebuilding.com/manager/public/authentication/login?ReturnUrl=%2Fmanager%2F) account from your browser.    2. Open the ***Settings*** menu and click ***Developer Tools***. The page will open automatically.    3. Click the ***Create API Key*** button. A modal will appear.    4. Enter a clear, memorable name and description for your API key. It’ll make it easier to locate the right key when you make a request. Once finished, click **Next**.    5. Now, choose which pieces of Buildium data you want this API key to have access to by marking the corresponding checkboxes. Once finished, click **Next**.    6. You successfully created an API key!    > **Important:** This is your only chance to record the secret. Make sure it’s stored somewhere secure! If it’s forgotten, you’ll need to delete this key and start from scratch.    <br />    <video width=\"100%\" autoplay loop muted>    <source src=\"generate_open_api_key.mp4\" type=\"video/mp4\" />  </video>    <br />    You have now successfully created an API key and have everything you need to  send requests to the Buildium API!    Before moving on to [making your first request](#section/Getting-Started/How-to-Make-a-Request) please review [Keeping your Keys Safe](#section/Getting-Started/Keeping-your-Keys-Safe) for an overview on securely storing your API keys.    <br />  If you are having issues creating API keys you can submit a [Support](#section/API-Overview/Support) request for assistance.  <br />      ## Keeping API Keys Safe    Based on their permissions, API keys could have full access to your account’s Buildium data. It’s important that you only grant access to trusted applications, securely record secrets, and consider a password manager to stay organized.      ### Recommended Practices    - Avoid hard-coding client IDs and secrets inside source files.  - Avoid storing client IDs and secrets in any files that may be committed to source control, particularly cloud-based source control platforms.  - Apply restrictions to client IDs and secrets shared with your staff. You can restrict a key to particular Buildium entities or to read-only access (GET resources only).  - Avoid sharing client IDs and secrets across public, insecure platforms.  - Establish a process to regularly recreate your client IDs and secrets from your Buildium account.    <br />    <br />    ## How to Make a Request    You’ve done a great job setting up your account, Now, we’ll walk you through how to access your data. It’s very straightforward and should only take a few minutes!      > **Tip:** Looking for the right HTTP client? If you’re just getting started, we recommend Postman.      <br />    ### Let's Get Started!    #### Step 1: Get Your API Key    If you haven't yet done so, obtain your API key client ID and secret from your Buildium account. Your API key is how the Buildium API authenticates requests and ensures only you can access your data.    See [Getting Started](#section/Getting-Started) for a deeper dive into enabling the API and creating keys.    #### Step 2: Install a HTTP client  The Buildium API supports any standard HTTP client. If you're looking for a user-friendly HTTP client application, we recommend [Postman](https://www.postman.com/product/api-client) – it allows you to access the Buildium API without writing code. We’ll use Postman for our example below to demonstrate sending an API request.      #### Step 3: Make a Sample Request    Let's dive in and make a simple request to get all the [Rental Properties](#operation/RentalsGetAllGLAccounts) response message now includes the property `IsBankAccount`. This is a boolean property that indicates whether the general ledger account is also a bank account.  * A `Country` property has been added to all Address messages. This property contains an enumeration indicating the country of the address.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import date
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from openapi_client.models.meter_reading_details_message import MeterReadingDetailsMessage
from openapi_client.models.meter_reading_details_put_message import MeterReadingDetailsPutMessage
from openapi_client.models.meter_reading_message import MeterReadingMessage

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class AssociationMeterReadingsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def delete_meter_reading_details_for_association(
        self,
        association_id: StrictInt,
        readingdate: Annotated[date, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[StrictStr, Field(description="Filters results to the specified meter type.")],
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
    ) -> None:
        """Delete meter reading details for a given date

        Delete meter reading details for an association for a given date.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Ownership account transactions</span> - `View` `Edit` `Delete`

        :param association_id: (required)
        :type association_id: int
        :param readingdate: Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. (required)
        :type readingdate: date
        :param metertype: Filters results to the specified meter type. (required)
        :type metertype: str
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

        _param = self._delete_meter_reading_details_for_association_serialize(
            association_id=association_id,
            readingdate=readingdate,
            metertype=metertype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_meter_reading_details_for_association_with_http_info(
        self,
        association_id: StrictInt,
        readingdate: Annotated[date, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[StrictStr, Field(description="Filters results to the specified meter type.")],
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
    ) -> ApiResponse[None]:
        """Delete meter reading details for a given date

        Delete meter reading details for an association for a given date.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Ownership account transactions</span> - `View` `Edit` `Delete`

        :param association_id: (required)
        :type association_id: int
        :param readingdate: Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. (required)
        :type readingdate: date
        :param metertype: Filters results to the specified meter type. (required)
        :type metertype: str
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

        _param = self._delete_meter_reading_details_for_association_serialize(
            association_id=association_id,
            readingdate=readingdate,
            metertype=metertype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_meter_reading_details_for_association_without_preload_content(
        self,
        association_id: StrictInt,
        readingdate: Annotated[date, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[StrictStr, Field(description="Filters results to the specified meter type.")],
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
        """Delete meter reading details for a given date

        Delete meter reading details for an association for a given date.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Ownership account transactions</span> - `View` `Edit` `Delete`

        :param association_id: (required)
        :type association_id: int
        :param readingdate: Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. (required)
        :type readingdate: date
        :param metertype: Filters results to the specified meter type. (required)
        :type metertype: str
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

        _param = self._delete_meter_reading_details_for_association_serialize(
            association_id=association_id,
            readingdate=readingdate,
            metertype=metertype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_meter_reading_details_for_association_serialize(
        self,
        association_id,
        readingdate,
        metertype,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if association_id is not None:
            _path_params['associationId'] = association_id
        # process the query parameters
        if readingdate is not None:
            if isinstance(readingdate, date):
                _query_params.append(
                    (
                        'readingdate',
                        readingdate.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('readingdate', readingdate))
            
        if metertype is not None:
            
            _query_params.append(('metertype', metertype))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'clientId', 
            'clientSecret'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/v1/associations/{associationId}/meterreadings/summary',
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
    def get_association_meter_reading_details_async(
        self,
        association_id: StrictInt,
        readingdate: Annotated[date, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[StrictStr, Field(description="Filters results to the specified meter type.")],
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
    ) -> MeterReadingDetailsMessage:
        """Retrieve all meter reading details

        Retrieves all meter reading details for an association.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Associations and units</span> - `View`

        :param association_id: (required)
        :type association_id: int
        :param readingdate: Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. (required)
        :type readingdate: date
        :param metertype: Filters results to the specified meter type. (required)
        :type metertype: str
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

        _param = self._get_association_meter_reading_details_async_serialize(
            association_id=association_id,
            readingdate=readingdate,
            metertype=metertype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MeterReadingDetailsMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_association_meter_reading_details_async_with_http_info(
        self,
        association_id: StrictInt,
        readingdate: Annotated[date, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[StrictStr, Field(description="Filters results to the specified meter type.")],
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
    ) -> ApiResponse[MeterReadingDetailsMessage]:
        """Retrieve all meter reading details

        Retrieves all meter reading details for an association.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Associations and units</span> - `View`

        :param association_id: (required)
        :type association_id: int
        :param readingdate: Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. (required)
        :type readingdate: date
        :param metertype: Filters results to the specified meter type. (required)
        :type metertype: str
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

        _param = self._get_association_meter_reading_details_async_serialize(
            association_id=association_id,
            readingdate=readingdate,
            metertype=metertype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MeterReadingDetailsMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_association_meter_reading_details_async_without_preload_content(
        self,
        association_id: StrictInt,
        readingdate: Annotated[date, Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")],
        metertype: Annotated[StrictStr, Field(description="Filters results to the specified meter type.")],
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
        """Retrieve all meter reading details

        Retrieves all meter reading details for an association.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Associations and units</span> - `View`

        :param association_id: (required)
        :type association_id: int
        :param readingdate: Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. (required)
        :type readingdate: date
        :param metertype: Filters results to the specified meter type. (required)
        :type metertype: str
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

        _param = self._get_association_meter_reading_details_async_serialize(
            association_id=association_id,
            readingdate=readingdate,
            metertype=metertype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MeterReadingDetailsMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_association_meter_reading_details_async_serialize(
        self,
        association_id,
        readingdate,
        metertype,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if association_id is not None:
            _path_params['associationId'] = association_id
        # process the query parameters
        if readingdate is not None:
            if isinstance(readingdate, date):
                _query_params.append(
                    (
                        'readingdate',
                        readingdate.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('readingdate', readingdate))
            
        if metertype is not None:
            
            _query_params.append(('metertype', metertype))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'clientId', 
            'clientSecret'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/associations/{associationId}/meterreadings/summary',
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
    def get_meter_readings_for_association(
        self,
        association_id: StrictInt,
        readingdatefrom: Annotated[date, Field(description="Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        readingdateto: Annotated[date, Field(description="Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        metertypes: Annotated[Optional[List[StrictStr]], Field(description="Filters results to the specified meter types.")] = None,
        orderby: Annotated[Optional[StrictStr], Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information.")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
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
    ) -> List[MeterReadingMessage]:
        """Retrieve all meter readings

        Retrieves all meter readings for an association.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Associations and units</span> - `View`

        :param association_id: (required)
        :type association_id: int
        :param readingdatefrom: Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days. (required)
        :type readingdatefrom: date
        :param readingdateto: Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days. (required)
        :type readingdateto: date
        :param metertypes: Filters results to the specified meter types.
        :type metertypes: List[str]
        :param orderby: `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information.
        :type orderby: str
        :param offset: `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.
        :type offset: int
        :param limit: `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.
        :type limit: int
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

        _param = self._get_meter_readings_for_association_serialize(
            association_id=association_id,
            readingdatefrom=readingdatefrom,
            readingdateto=readingdateto,
            metertypes=metertypes,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[MeterReadingMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_meter_readings_for_association_with_http_info(
        self,
        association_id: StrictInt,
        readingdatefrom: Annotated[date, Field(description="Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        readingdateto: Annotated[date, Field(description="Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        metertypes: Annotated[Optional[List[StrictStr]], Field(description="Filters results to the specified meter types.")] = None,
        orderby: Annotated[Optional[StrictStr], Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information.")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
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
    ) -> ApiResponse[List[MeterReadingMessage]]:
        """Retrieve all meter readings

        Retrieves all meter readings for an association.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Associations and units</span> - `View`

        :param association_id: (required)
        :type association_id: int
        :param readingdatefrom: Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days. (required)
        :type readingdatefrom: date
        :param readingdateto: Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days. (required)
        :type readingdateto: date
        :param metertypes: Filters results to the specified meter types.
        :type metertypes: List[str]
        :param orderby: `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information.
        :type orderby: str
        :param offset: `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.
        :type offset: int
        :param limit: `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.
        :type limit: int
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

        _param = self._get_meter_readings_for_association_serialize(
            association_id=association_id,
            readingdatefrom=readingdatefrom,
            readingdateto=readingdateto,
            metertypes=metertypes,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[MeterReadingMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_meter_readings_for_association_without_preload_content(
        self,
        association_id: StrictInt,
        readingdatefrom: Annotated[date, Field(description="Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        readingdateto: Annotated[date, Field(description="Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.")],
        metertypes: Annotated[Optional[List[StrictStr]], Field(description="Filters results to the specified meter types.")] = None,
        orderby: Annotated[Optional[StrictStr], Field(description="`orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information.")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="`offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="`limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.")] = None,
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
        """Retrieve all meter readings

        Retrieves all meter readings for an association.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Associations and units</span> - `View`

        :param association_id: (required)
        :type association_id: int
        :param readingdatefrom: Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days. (required)
        :type readingdatefrom: date
        :param readingdateto: Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days. (required)
        :type readingdateto: date
        :param metertypes: Filters results to the specified meter types.
        :type metertypes: List[str]
        :param orderby: `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information.
        :type orderby: str
        :param offset: `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0.
        :type offset: int
        :param limit: `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50.
        :type limit: int
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

        _param = self._get_meter_readings_for_association_serialize(
            association_id=association_id,
            readingdatefrom=readingdatefrom,
            readingdateto=readingdateto,
            metertypes=metertypes,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[MeterReadingMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_meter_readings_for_association_serialize(
        self,
        association_id,
        readingdatefrom,
        readingdateto,
        metertypes,
        orderby,
        offset,
        limit,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'metertypes': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if association_id is not None:
            _path_params['associationId'] = association_id
        # process the query parameters
        if readingdatefrom is not None:
            if isinstance(readingdatefrom, date):
                _query_params.append(
                    (
                        'readingdatefrom',
                        readingdatefrom.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('readingdatefrom', readingdatefrom))
            
        if readingdateto is not None:
            if isinstance(readingdateto, date):
                _query_params.append(
                    (
                        'readingdateto',
                        readingdateto.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('readingdateto', readingdateto))
            
        if metertypes is not None:
            
            _query_params.append(('metertypes', metertypes))
            
        if orderby is not None:
            
            _query_params.append(('orderby', orderby))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'clientId', 
            'clientSecret'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/associations/{associationId}/meterreadings',
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
    def upsert_association_meter_reading_details_async(
        self,
        association_id: StrictInt,
        meter_reading_details_put_message: MeterReadingDetailsPutMessage,
        readingdate: Annotated[Optional[date], Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")] = None,
        metertype: Annotated[Optional[StrictStr], Field(description="Filters results to the specified meter type.")] = None,
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
    ) -> MeterReadingDetailsMessage:
        """Create/Update meter reading details

        This endpoint can be used to both create and update a meter reading detail for an association.              <ul><li>There can only be one meter reading detail for a given combination of MeterType and ReadingDate for an association</li><li>If you are updating an existing meter reading detail, use the query parameters to specify the existing meter reading detail to update.</li><li>If you are creating a new meter reading detail, do not pass any query parameters.</li><li>When adding a new item to the Details array, leave out the `Id` field.</li><li>When updating an existing item in the Details array, the `Id` field of the existing item must be included.</li></ul><br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Associations and units</span> - `View` `Edit`

        :param association_id: (required)
        :type association_id: int
        :param meter_reading_details_put_message: (required)
        :type meter_reading_details_put_message: MeterReadingDetailsPutMessage
        :param readingdate: Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.
        :type readingdate: date
        :param metertype: Filters results to the specified meter type.
        :type metertype: str
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

        _param = self._upsert_association_meter_reading_details_async_serialize(
            association_id=association_id,
            meter_reading_details_put_message=meter_reading_details_put_message,
            readingdate=readingdate,
            metertype=metertype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MeterReadingDetailsMessage",
            '201': "MeterReadingDetailsMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '409': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def upsert_association_meter_reading_details_async_with_http_info(
        self,
        association_id: StrictInt,
        meter_reading_details_put_message: MeterReadingDetailsPutMessage,
        readingdate: Annotated[Optional[date], Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")] = None,
        metertype: Annotated[Optional[StrictStr], Field(description="Filters results to the specified meter type.")] = None,
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
    ) -> ApiResponse[MeterReadingDetailsMessage]:
        """Create/Update meter reading details

        This endpoint can be used to both create and update a meter reading detail for an association.              <ul><li>There can only be one meter reading detail for a given combination of MeterType and ReadingDate for an association</li><li>If you are updating an existing meter reading detail, use the query parameters to specify the existing meter reading detail to update.</li><li>If you are creating a new meter reading detail, do not pass any query parameters.</li><li>When adding a new item to the Details array, leave out the `Id` field.</li><li>When updating an existing item in the Details array, the `Id` field of the existing item must be included.</li></ul><br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Associations and units</span> - `View` `Edit`

        :param association_id: (required)
        :type association_id: int
        :param meter_reading_details_put_message: (required)
        :type meter_reading_details_put_message: MeterReadingDetailsPutMessage
        :param readingdate: Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.
        :type readingdate: date
        :param metertype: Filters results to the specified meter type.
        :type metertype: str
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

        _param = self._upsert_association_meter_reading_details_async_serialize(
            association_id=association_id,
            meter_reading_details_put_message=meter_reading_details_put_message,
            readingdate=readingdate,
            metertype=metertype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MeterReadingDetailsMessage",
            '201': "MeterReadingDetailsMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '409': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def upsert_association_meter_reading_details_async_without_preload_content(
        self,
        association_id: StrictInt,
        meter_reading_details_put_message: MeterReadingDetailsPutMessage,
        readingdate: Annotated[Optional[date], Field(description="Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.")] = None,
        metertype: Annotated[Optional[StrictStr], Field(description="Filters results to the specified meter type.")] = None,
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
        """Create/Update meter reading details

        This endpoint can be used to both create and update a meter reading detail for an association.              <ul><li>There can only be one meter reading detail for a given combination of MeterType and ReadingDate for an association</li><li>If you are updating an existing meter reading detail, use the query parameters to specify the existing meter reading detail to update.</li><li>If you are creating a new meter reading detail, do not pass any query parameters.</li><li>When adding a new item to the Details array, leave out the `Id` field.</li><li>When updating an existing item in the Details array, the `Id` field of the existing item must be included.</li></ul><br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Associations > Associations and units</span> - `View` `Edit`

        :param association_id: (required)
        :type association_id: int
        :param meter_reading_details_put_message: (required)
        :type meter_reading_details_put_message: MeterReadingDetailsPutMessage
        :param readingdate: Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.
        :type readingdate: date
        :param metertype: Filters results to the specified meter type.
        :type metertype: str
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

        _param = self._upsert_association_meter_reading_details_async_serialize(
            association_id=association_id,
            meter_reading_details_put_message=meter_reading_details_put_message,
            readingdate=readingdate,
            metertype=metertype,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MeterReadingDetailsMessage",
            '201': "MeterReadingDetailsMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '409': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _upsert_association_meter_reading_details_async_serialize(
        self,
        association_id,
        meter_reading_details_put_message,
        readingdate,
        metertype,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if association_id is not None:
            _path_params['associationId'] = association_id
        # process the query parameters
        if readingdate is not None:
            if isinstance(readingdate, date):
                _query_params.append(
                    (
                        'readingdate',
                        readingdate.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('readingdate', readingdate))
            
        if metertype is not None:
            
            _query_params.append(('metertype', metertype))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if meter_reading_details_put_message is not None:
            _body_params = meter_reading_details_put_message


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'clientId', 
            'clientSecret'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/v1/associations/{associationId}/meterreadings/summary',
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


