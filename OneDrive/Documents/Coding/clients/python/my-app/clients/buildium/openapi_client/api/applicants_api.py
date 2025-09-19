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

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from openapi_client.models.applicant_group_message import ApplicantGroupMessage
from openapi_client.models.applicant_group_post_message import ApplicantGroupPostMessage
from openapi_client.models.applicant_group_put_message import ApplicantGroupPutMessage
from openapi_client.models.applicant_message import ApplicantMessage
from openapi_client.models.applicant_post_message import ApplicantPostMessage
from openapi_client.models.applicant_put_message import ApplicantPutMessage
from openapi_client.models.application_message import ApplicationMessage
from openapi_client.models.application_put_message import ApplicationPutMessage
from openapi_client.models.note_message import NoteMessage
from openapi_client.models.note_post_message import NotePostMessage
from openapi_client.models.note_put_message import NotePutMessage

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class ApplicantsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_applicant(
        self,
        applicant_post_message: ApplicantPostMessage,
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
    ) -> ApplicantMessage:
        """Create an applicant

        Creates an applicant.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_post_message: (required)
        :type applicant_post_message: ApplicantPostMessage
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

        _param = self._create_applicant_serialize(
            applicant_post_message=applicant_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApplicantMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def create_applicant_with_http_info(
        self,
        applicant_post_message: ApplicantPostMessage,
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
    ) -> ApiResponse[ApplicantMessage]:
        """Create an applicant

        Creates an applicant.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_post_message: (required)
        :type applicant_post_message: ApplicantPostMessage
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

        _param = self._create_applicant_serialize(
            applicant_post_message=applicant_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApplicantMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def create_applicant_without_preload_content(
        self,
        applicant_post_message: ApplicantPostMessage,
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
        """Create an applicant

        Creates an applicant.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_post_message: (required)
        :type applicant_post_message: ApplicantPostMessage
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

        _param = self._create_applicant_serialize(
            applicant_post_message=applicant_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApplicantMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_applicant_serialize(
        self,
        applicant_post_message,
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
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if applicant_post_message is not None:
            _body_params = applicant_post_message


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
            method='POST',
            resource_path='/v1/applicants',
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
    def create_applicant_group(
        self,
        applicant_group_post_message: ApplicantGroupPostMessage,
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
    ) -> ApplicantGroupMessage:
        """Create an applicant group

        Creates an applicant group.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_post_message: (required)
        :type applicant_group_post_message: ApplicantGroupPostMessage
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

        _param = self._create_applicant_group_serialize(
            applicant_group_post_message=applicant_group_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApplicantGroupMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def create_applicant_group_with_http_info(
        self,
        applicant_group_post_message: ApplicantGroupPostMessage,
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
    ) -> ApiResponse[ApplicantGroupMessage]:
        """Create an applicant group

        Creates an applicant group.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_post_message: (required)
        :type applicant_group_post_message: ApplicantGroupPostMessage
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

        _param = self._create_applicant_group_serialize(
            applicant_group_post_message=applicant_group_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApplicantGroupMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def create_applicant_group_without_preload_content(
        self,
        applicant_group_post_message: ApplicantGroupPostMessage,
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
        """Create an applicant group

        Creates an applicant group.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_post_message: (required)
        :type applicant_group_post_message: ApplicantGroupPostMessage
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

        _param = self._create_applicant_group_serialize(
            applicant_group_post_message=applicant_group_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ApplicantGroupMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_applicant_group_serialize(
        self,
        applicant_group_post_message,
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
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if applicant_group_post_message is not None:
            _body_params = applicant_group_post_message


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
            method='POST',
            resource_path='/v1/applicants/groups',
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
    def create_applicant_note(
        self,
        applicant_id: StrictInt,
        note_post_message: NotePostMessage,
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
    ) -> NoteMessage:
        """Create an applicant note

        Creates an applicant note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> -  `View` `Edit`

        :param applicant_id: (required)
        :type applicant_id: int
        :param note_post_message: (required)
        :type note_post_message: NotePostMessage
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

        _param = self._create_applicant_note_serialize(
            applicant_id=applicant_id,
            note_post_message=note_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def create_applicant_note_with_http_info(
        self,
        applicant_id: StrictInt,
        note_post_message: NotePostMessage,
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
    ) -> ApiResponse[NoteMessage]:
        """Create an applicant note

        Creates an applicant note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> -  `View` `Edit`

        :param applicant_id: (required)
        :type applicant_id: int
        :param note_post_message: (required)
        :type note_post_message: NotePostMessage
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

        _param = self._create_applicant_note_serialize(
            applicant_id=applicant_id,
            note_post_message=note_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def create_applicant_note_without_preload_content(
        self,
        applicant_id: StrictInt,
        note_post_message: NotePostMessage,
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
        """Create an applicant note

        Creates an applicant note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> -  `View` `Edit`

        :param applicant_id: (required)
        :type applicant_id: int
        :param note_post_message: (required)
        :type note_post_message: NotePostMessage
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

        _param = self._create_applicant_note_serialize(
            applicant_id=applicant_id,
            note_post_message=note_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_applicant_note_serialize(
        self,
        applicant_id,
        note_post_message,
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
        if applicant_id is not None:
            _path_params['applicantId'] = applicant_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if note_post_message is not None:
            _body_params = note_post_message


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
            method='POST',
            resource_path='/v1/applicants/{applicantId}/notes',
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
    def create_application_group_note(
        self,
        applicant_group_id: StrictInt,
        note_post_message: NotePostMessage,
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
    ) -> NoteMessage:
        """Create an applicant group note

        Creates an applicant group note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param note_post_message: (required)
        :type note_post_message: NotePostMessage
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

        _param = self._create_application_group_note_serialize(
            applicant_group_id=applicant_group_id,
            note_post_message=note_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def create_application_group_note_with_http_info(
        self,
        applicant_group_id: StrictInt,
        note_post_message: NotePostMessage,
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
    ) -> ApiResponse[NoteMessage]:
        """Create an applicant group note

        Creates an applicant group note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param note_post_message: (required)
        :type note_post_message: NotePostMessage
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

        _param = self._create_application_group_note_serialize(
            applicant_group_id=applicant_group_id,
            note_post_message=note_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def create_application_group_note_without_preload_content(
        self,
        applicant_group_id: StrictInt,
        note_post_message: NotePostMessage,
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
        """Create an applicant group note

        Creates an applicant group note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param note_post_message: (required)
        :type note_post_message: NotePostMessage
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

        _param = self._create_application_group_note_serialize(
            applicant_group_id=applicant_group_id,
            note_post_message=note_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_application_group_note_serialize(
        self,
        applicant_group_id,
        note_post_message,
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
        if applicant_group_id is not None:
            _path_params['applicantGroupId'] = applicant_group_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if note_post_message is not None:
            _body_params = note_post_message


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
            method='POST',
            resource_path='/v1/applicants/groups/{applicantGroupId}/notes',
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
    def get_all_applicant_notes(
        self,
        applicant_id: StrictInt,
        updateddatetimefrom: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[Optional[StrictInt], Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
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
    ) -> List[NoteMessage]:
        """Retrieve all applicant notes

        Retrieves all applicant notes.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
        :param updateddatetimefrom: Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimefrom: datetime
        :param updateddatetimeto: Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimeto: datetime
        :param lastupdatedbyuserid: Filters results to only notes that were last updated by the specified user identifier.
        :type lastupdatedbyuserid: int
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

        _param = self._get_all_applicant_notes_serialize(
            applicant_id=applicant_id,
            updateddatetimefrom=updateddatetimefrom,
            updateddatetimeto=updateddatetimeto,
            lastupdatedbyuserid=lastupdatedbyuserid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[NoteMessage]",
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
    def get_all_applicant_notes_with_http_info(
        self,
        applicant_id: StrictInt,
        updateddatetimefrom: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[Optional[StrictInt], Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
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
    ) -> ApiResponse[List[NoteMessage]]:
        """Retrieve all applicant notes

        Retrieves all applicant notes.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
        :param updateddatetimefrom: Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimefrom: datetime
        :param updateddatetimeto: Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimeto: datetime
        :param lastupdatedbyuserid: Filters results to only notes that were last updated by the specified user identifier.
        :type lastupdatedbyuserid: int
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

        _param = self._get_all_applicant_notes_serialize(
            applicant_id=applicant_id,
            updateddatetimefrom=updateddatetimefrom,
            updateddatetimeto=updateddatetimeto,
            lastupdatedbyuserid=lastupdatedbyuserid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[NoteMessage]",
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
    def get_all_applicant_notes_without_preload_content(
        self,
        applicant_id: StrictInt,
        updateddatetimefrom: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[Optional[StrictInt], Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
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
        """Retrieve all applicant notes

        Retrieves all applicant notes.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
        :param updateddatetimefrom: Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimefrom: datetime
        :param updateddatetimeto: Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimeto: datetime
        :param lastupdatedbyuserid: Filters results to only notes that were last updated by the specified user identifier.
        :type lastupdatedbyuserid: int
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

        _param = self._get_all_applicant_notes_serialize(
            applicant_id=applicant_id,
            updateddatetimefrom=updateddatetimefrom,
            updateddatetimeto=updateddatetimeto,
            lastupdatedbyuserid=lastupdatedbyuserid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[NoteMessage]",
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


    def _get_all_applicant_notes_serialize(
        self,
        applicant_id,
        updateddatetimefrom,
        updateddatetimeto,
        lastupdatedbyuserid,
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
        if applicant_id is not None:
            _path_params['applicantId'] = applicant_id
        # process the query parameters
        if updateddatetimefrom is not None:
            if isinstance(updateddatetimefrom, datetime):
                _query_params.append(
                    (
                        'updateddatetimefrom',
                        updateddatetimefrom.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('updateddatetimefrom', updateddatetimefrom))
            
        if updateddatetimeto is not None:
            if isinstance(updateddatetimeto, datetime):
                _query_params.append(
                    (
                        'updateddatetimeto',
                        updateddatetimeto.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('updateddatetimeto', updateddatetimeto))
            
        if lastupdatedbyuserid is not None:
            
            _query_params.append(('lastupdatedbyuserid', lastupdatedbyuserid))
            
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
            resource_path='/v1/applicants/{applicantId}/notes',
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
    def get_applicant_by_id(
        self,
        applicant_id: StrictInt,
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
    ) -> ApplicantMessage:
        """Retrieve an applicant

        Retrieves an applicant.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
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

        _param = self._get_applicant_by_id_serialize(
            applicant_id=applicant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_applicant_by_id_with_http_info(
        self,
        applicant_id: StrictInt,
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
    ) -> ApiResponse[ApplicantMessage]:
        """Retrieve an applicant

        Retrieves an applicant.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
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

        _param = self._get_applicant_by_id_serialize(
            applicant_id=applicant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_applicant_by_id_without_preload_content(
        self,
        applicant_id: StrictInt,
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
        """Retrieve an applicant

        Retrieves an applicant.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
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

        _param = self._get_applicant_by_id_serialize(
            applicant_id=applicant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_applicant_by_id_serialize(
        self,
        applicant_id,
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
        if applicant_id is not None:
            _path_params['applicantId'] = applicant_id
        # process the query parameters
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
            resource_path='/v1/applicants/{applicantId}',
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
    def get_applicant_group_by_id(
        self,
        applicant_group_id: StrictInt,
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
    ) -> ApplicantGroupMessage:
        """Retrieve an applicant group

        Retrieves an applicant group.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
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

        _param = self._get_applicant_group_by_id_serialize(
            applicant_group_id=applicant_group_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantGroupMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_applicant_group_by_id_with_http_info(
        self,
        applicant_group_id: StrictInt,
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
    ) -> ApiResponse[ApplicantGroupMessage]:
        """Retrieve an applicant group

        Retrieves an applicant group.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
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

        _param = self._get_applicant_group_by_id_serialize(
            applicant_group_id=applicant_group_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantGroupMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_applicant_group_by_id_without_preload_content(
        self,
        applicant_group_id: StrictInt,
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
        """Retrieve an applicant group

        Retrieves an applicant group.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
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

        _param = self._get_applicant_group_by_id_serialize(
            applicant_group_id=applicant_group_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantGroupMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_applicant_group_by_id_serialize(
        self,
        applicant_group_id,
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
        if applicant_group_id is not None:
            _path_params['applicantGroupId'] = applicant_group_id
        # process the query parameters
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
            resource_path='/v1/applicants/groups/{applicantGroupId}',
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
    def get_applicant_group_note_by_note_id(
        self,
        applicant_group_id: StrictInt,
        note_id: StrictInt,
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
    ) -> NoteMessage:
        """Retrieve an applicant group note

        Retrieves an applicant group note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param note_id: (required)
        :type note_id: int
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

        _param = self._get_applicant_group_note_by_note_id_serialize(
            applicant_group_id=applicant_group_id,
            note_id=note_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_applicant_group_note_by_note_id_with_http_info(
        self,
        applicant_group_id: StrictInt,
        note_id: StrictInt,
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
    ) -> ApiResponse[NoteMessage]:
        """Retrieve an applicant group note

        Retrieves an applicant group note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param note_id: (required)
        :type note_id: int
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

        _param = self._get_applicant_group_note_by_note_id_serialize(
            applicant_group_id=applicant_group_id,
            note_id=note_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_applicant_group_note_by_note_id_without_preload_content(
        self,
        applicant_group_id: StrictInt,
        note_id: StrictInt,
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
        """Retrieve an applicant group note

        Retrieves an applicant group note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param note_id: (required)
        :type note_id: int
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

        _param = self._get_applicant_group_note_by_note_id_serialize(
            applicant_group_id=applicant_group_id,
            note_id=note_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_applicant_group_note_by_note_id_serialize(
        self,
        applicant_group_id,
        note_id,
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
        if applicant_group_id is not None:
            _path_params['applicantGroupId'] = applicant_group_id
        if note_id is not None:
            _path_params['noteId'] = note_id
        # process the query parameters
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
            resource_path='/v1/applicants/groups/{applicantGroupId}/notes/{noteId}',
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
    def get_applicant_group_notes(
        self,
        applicant_group_id: StrictInt,
        updateddatetimefrom: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[Optional[StrictInt], Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
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
    ) -> List[NoteMessage]:
        """Retrieve all applicant group notes

        Retrieves all applicant group notes.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param updateddatetimefrom: Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimefrom: datetime
        :param updateddatetimeto: Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimeto: datetime
        :param lastupdatedbyuserid: Filters results to only notes that were last updated by the specified user identifier.
        :type lastupdatedbyuserid: int
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

        _param = self._get_applicant_group_notes_serialize(
            applicant_group_id=applicant_group_id,
            updateddatetimefrom=updateddatetimefrom,
            updateddatetimeto=updateddatetimeto,
            lastupdatedbyuserid=lastupdatedbyuserid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[NoteMessage]",
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
    def get_applicant_group_notes_with_http_info(
        self,
        applicant_group_id: StrictInt,
        updateddatetimefrom: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[Optional[StrictInt], Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
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
    ) -> ApiResponse[List[NoteMessage]]:
        """Retrieve all applicant group notes

        Retrieves all applicant group notes.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param updateddatetimefrom: Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimefrom: datetime
        :param updateddatetimeto: Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimeto: datetime
        :param lastupdatedbyuserid: Filters results to only notes that were last updated by the specified user identifier.
        :type lastupdatedbyuserid: int
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

        _param = self._get_applicant_group_notes_serialize(
            applicant_group_id=applicant_group_id,
            updateddatetimefrom=updateddatetimefrom,
            updateddatetimeto=updateddatetimeto,
            lastupdatedbyuserid=lastupdatedbyuserid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[NoteMessage]",
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
    def get_applicant_group_notes_without_preload_content(
        self,
        applicant_group_id: StrictInt,
        updateddatetimefrom: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        updateddatetimeto: Annotated[Optional[datetime], Field(description="Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.")] = None,
        lastupdatedbyuserid: Annotated[Optional[StrictInt], Field(description="Filters results to only notes that were last updated by the specified user identifier.")] = None,
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
        """Retrieve all applicant group notes

        Retrieves all applicant group notes.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param updateddatetimefrom: Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimefrom: datetime
        :param updateddatetimeto: Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS.
        :type updateddatetimeto: datetime
        :param lastupdatedbyuserid: Filters results to only notes that were last updated by the specified user identifier.
        :type lastupdatedbyuserid: int
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

        _param = self._get_applicant_group_notes_serialize(
            applicant_group_id=applicant_group_id,
            updateddatetimefrom=updateddatetimefrom,
            updateddatetimeto=updateddatetimeto,
            lastupdatedbyuserid=lastupdatedbyuserid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[NoteMessage]",
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


    def _get_applicant_group_notes_serialize(
        self,
        applicant_group_id,
        updateddatetimefrom,
        updateddatetimeto,
        lastupdatedbyuserid,
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
        if applicant_group_id is not None:
            _path_params['applicantGroupId'] = applicant_group_id
        # process the query parameters
        if updateddatetimefrom is not None:
            if isinstance(updateddatetimefrom, datetime):
                _query_params.append(
                    (
                        'updateddatetimefrom',
                        updateddatetimefrom.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('updateddatetimefrom', updateddatetimefrom))
            
        if updateddatetimeto is not None:
            if isinstance(updateddatetimeto, datetime):
                _query_params.append(
                    (
                        'updateddatetimeto',
                        updateddatetimeto.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('updateddatetimeto', updateddatetimeto))
            
        if lastupdatedbyuserid is not None:
            
            _query_params.append(('lastupdatedbyuserid', lastupdatedbyuserid))
            
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
            resource_path='/v1/applicants/groups/{applicantGroupId}/notes',
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
    def get_applicant_groups(
        self,
        entitytype: Annotated[Optional[StrictStr], Field(description="Filters results to any applicant groups associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.")] = None,
        applicationgroupstatuses: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the applicant group status. If no status is specified, applicant groups in any status will be returned.")] = None,
        unitids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to applicant groups associated to any of the specified rental property unit identifiers.")] = None,
        name: Annotated[Optional[StrictStr], Field(description="Filters results to applicant groups that includes applicants whose name *contains* the specified value.")] = None,
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
    ) -> List[ApplicantGroupMessage]:
        """Retrieve all applicant groups

        Retrieves all applicant groups.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param entitytype: Filters results to any applicant groups associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.
        :type entitytype: str
        :param entityid: Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.
        :type entityid: int
        :param applicationgroupstatuses: Filters results by the applicant group status. If no status is specified, applicant groups in any status will be returned.
        :type applicationgroupstatuses: List[str]
        :param unitids: Filters results to applicant groups associated to any of the specified rental property unit identifiers.
        :type unitids: List[int]
        :param name: Filters results to applicant groups that includes applicants whose name *contains* the specified value.
        :type name: str
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

        _param = self._get_applicant_groups_serialize(
            entitytype=entitytype,
            entityid=entityid,
            applicationgroupstatuses=applicationgroupstatuses,
            unitids=unitids,
            name=name,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ApplicantGroupMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def get_applicant_groups_with_http_info(
        self,
        entitytype: Annotated[Optional[StrictStr], Field(description="Filters results to any applicant groups associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.")] = None,
        applicationgroupstatuses: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the applicant group status. If no status is specified, applicant groups in any status will be returned.")] = None,
        unitids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to applicant groups associated to any of the specified rental property unit identifiers.")] = None,
        name: Annotated[Optional[StrictStr], Field(description="Filters results to applicant groups that includes applicants whose name *contains* the specified value.")] = None,
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
    ) -> ApiResponse[List[ApplicantGroupMessage]]:
        """Retrieve all applicant groups

        Retrieves all applicant groups.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param entitytype: Filters results to any applicant groups associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.
        :type entitytype: str
        :param entityid: Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.
        :type entityid: int
        :param applicationgroupstatuses: Filters results by the applicant group status. If no status is specified, applicant groups in any status will be returned.
        :type applicationgroupstatuses: List[str]
        :param unitids: Filters results to applicant groups associated to any of the specified rental property unit identifiers.
        :type unitids: List[int]
        :param name: Filters results to applicant groups that includes applicants whose name *contains* the specified value.
        :type name: str
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

        _param = self._get_applicant_groups_serialize(
            entitytype=entitytype,
            entityid=entityid,
            applicationgroupstatuses=applicationgroupstatuses,
            unitids=unitids,
            name=name,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ApplicantGroupMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def get_applicant_groups_without_preload_content(
        self,
        entitytype: Annotated[Optional[StrictStr], Field(description="Filters results to any applicant groups associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.")] = None,
        applicationgroupstatuses: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the applicant group status. If no status is specified, applicant groups in any status will be returned.")] = None,
        unitids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to applicant groups associated to any of the specified rental property unit identifiers.")] = None,
        name: Annotated[Optional[StrictStr], Field(description="Filters results to applicant groups that includes applicants whose name *contains* the specified value.")] = None,
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
        """Retrieve all applicant groups

        Retrieves all applicant groups.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param entitytype: Filters results to any applicant groups associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.
        :type entitytype: str
        :param entityid: Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.
        :type entityid: int
        :param applicationgroupstatuses: Filters results by the applicant group status. If no status is specified, applicant groups in any status will be returned.
        :type applicationgroupstatuses: List[str]
        :param unitids: Filters results to applicant groups associated to any of the specified rental property unit identifiers.
        :type unitids: List[int]
        :param name: Filters results to applicant groups that includes applicants whose name *contains* the specified value.
        :type name: str
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

        _param = self._get_applicant_groups_serialize(
            entitytype=entitytype,
            entityid=entityid,
            applicationgroupstatuses=applicationgroupstatuses,
            unitids=unitids,
            name=name,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ApplicantGroupMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_applicant_groups_serialize(
        self,
        entitytype,
        entityid,
        applicationgroupstatuses,
        unitids,
        name,
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
            'applicationgroupstatuses': 'multi',
            'unitids': 'multi',
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
        # process the query parameters
        if entitytype is not None:
            
            _query_params.append(('entitytype', entitytype))
            
        if entityid is not None:
            
            _query_params.append(('entityid', entityid))
            
        if applicationgroupstatuses is not None:
            
            _query_params.append(('applicationgroupstatuses', applicationgroupstatuses))
            
        if unitids is not None:
            
            _query_params.append(('unitids', unitids))
            
        if name is not None:
            
            _query_params.append(('name', name))
            
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
            resource_path='/v1/applicants/groups',
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
    def get_applicant_note_by_id(
        self,
        applicant_id: StrictInt,
        note_id: StrictInt,
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
    ) -> NoteMessage:
        """Retrieve an applicant note

        Retrieves an applicant note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
        :param note_id: (required)
        :type note_id: int
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

        _param = self._get_applicant_note_by_id_serialize(
            applicant_id=applicant_id,
            note_id=note_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_applicant_note_by_id_with_http_info(
        self,
        applicant_id: StrictInt,
        note_id: StrictInt,
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
    ) -> ApiResponse[NoteMessage]:
        """Retrieve an applicant note

        Retrieves an applicant note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
        :param note_id: (required)
        :type note_id: int
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

        _param = self._get_applicant_note_by_id_serialize(
            applicant_id=applicant_id,
            note_id=note_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_applicant_note_by_id_without_preload_content(
        self,
        applicant_id: StrictInt,
        note_id: StrictInt,
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
        """Retrieve an applicant note

        Retrieves an applicant note.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
        :param note_id: (required)
        :type note_id: int
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

        _param = self._get_applicant_note_by_id_serialize(
            applicant_id=applicant_id,
            note_id=note_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_applicant_note_by_id_serialize(
        self,
        applicant_id,
        note_id,
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
        if applicant_id is not None:
            _path_params['applicantId'] = applicant_id
        if note_id is not None:
            _path_params['noteId'] = note_id
        # process the query parameters
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
            resource_path='/v1/applicants/{applicantId}/notes/{noteId}',
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
    def get_applicants(
        self,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters results to any applicant associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.")] = None,
        applicationstatuses: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the applicant application status. If no status is specified, applicants with an application in any status will be returned.")] = None,
        unitids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to applicants associated to any of the specified rental property unit identifiers.")] = None,
        name: Annotated[Optional[StrictStr], Field(description="Filters results to applicants whose name *contains* the specified value.")] = None,
        email: Annotated[Optional[StrictStr], Field(description="Filters results to applicants whose email *contains* the specified value")] = None,
        applicationsubmittedstartdate: Annotated[Optional[datetime], Field(description="Filters results to any applicant who submitted an application on or after the date specified.")] = None,
        applicationsubmittedenddate: Annotated[Optional[datetime], Field(description="Filters results to any applicant who submitted an application on or prior to the date specified.")] = None,
        lastupdatedfrom: Annotated[Optional[datetime], Field(description="Filters results to any applicants that were updated on or after the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[Optional[datetime], Field(description="Filters results to any applicants that were updated on or before the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
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
    ) -> List[ApplicantMessage]:
        """Retrieve all applicants

        Retrieves all applicants.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param entityid: Filters results to any applicant associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.
        :type entityid: int
        :param entitytype: Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.
        :type entitytype: str
        :param applicationstatuses: Filters results by the applicant application status. If no status is specified, applicants with an application in any status will be returned.
        :type applicationstatuses: List[str]
        :param unitids: Filters results to applicants associated to any of the specified rental property unit identifiers.
        :type unitids: List[int]
        :param name: Filters results to applicants whose name *contains* the specified value.
        :type name: str
        :param email: Filters results to applicants whose email *contains* the specified value
        :type email: str
        :param applicationsubmittedstartdate: Filters results to any applicant who submitted an application on or after the date specified.
        :type applicationsubmittedstartdate: datetime
        :param applicationsubmittedenddate: Filters results to any applicant who submitted an application on or prior to the date specified.
        :type applicationsubmittedenddate: datetime
        :param lastupdatedfrom: Filters results to any applicants that were updated on or after the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
        :type lastupdatedfrom: datetime
        :param lastupdatedto: Filters results to any applicants that were updated on or before the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
        :type lastupdatedto: datetime
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

        _param = self._get_applicants_serialize(
            entityid=entityid,
            entitytype=entitytype,
            applicationstatuses=applicationstatuses,
            unitids=unitids,
            name=name,
            email=email,
            applicationsubmittedstartdate=applicationsubmittedstartdate,
            applicationsubmittedenddate=applicationsubmittedenddate,
            lastupdatedfrom=lastupdatedfrom,
            lastupdatedto=lastupdatedto,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ApplicantMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def get_applicants_with_http_info(
        self,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters results to any applicant associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.")] = None,
        applicationstatuses: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the applicant application status. If no status is specified, applicants with an application in any status will be returned.")] = None,
        unitids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to applicants associated to any of the specified rental property unit identifiers.")] = None,
        name: Annotated[Optional[StrictStr], Field(description="Filters results to applicants whose name *contains* the specified value.")] = None,
        email: Annotated[Optional[StrictStr], Field(description="Filters results to applicants whose email *contains* the specified value")] = None,
        applicationsubmittedstartdate: Annotated[Optional[datetime], Field(description="Filters results to any applicant who submitted an application on or after the date specified.")] = None,
        applicationsubmittedenddate: Annotated[Optional[datetime], Field(description="Filters results to any applicant who submitted an application on or prior to the date specified.")] = None,
        lastupdatedfrom: Annotated[Optional[datetime], Field(description="Filters results to any applicants that were updated on or after the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[Optional[datetime], Field(description="Filters results to any applicants that were updated on or before the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
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
    ) -> ApiResponse[List[ApplicantMessage]]:
        """Retrieve all applicants

        Retrieves all applicants.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param entityid: Filters results to any applicant associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.
        :type entityid: int
        :param entitytype: Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.
        :type entitytype: str
        :param applicationstatuses: Filters results by the applicant application status. If no status is specified, applicants with an application in any status will be returned.
        :type applicationstatuses: List[str]
        :param unitids: Filters results to applicants associated to any of the specified rental property unit identifiers.
        :type unitids: List[int]
        :param name: Filters results to applicants whose name *contains* the specified value.
        :type name: str
        :param email: Filters results to applicants whose email *contains* the specified value
        :type email: str
        :param applicationsubmittedstartdate: Filters results to any applicant who submitted an application on or after the date specified.
        :type applicationsubmittedstartdate: datetime
        :param applicationsubmittedenddate: Filters results to any applicant who submitted an application on or prior to the date specified.
        :type applicationsubmittedenddate: datetime
        :param lastupdatedfrom: Filters results to any applicants that were updated on or after the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
        :type lastupdatedfrom: datetime
        :param lastupdatedto: Filters results to any applicants that were updated on or before the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
        :type lastupdatedto: datetime
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

        _param = self._get_applicants_serialize(
            entityid=entityid,
            entitytype=entitytype,
            applicationstatuses=applicationstatuses,
            unitids=unitids,
            name=name,
            email=email,
            applicationsubmittedstartdate=applicationsubmittedstartdate,
            applicationsubmittedenddate=applicationsubmittedenddate,
            lastupdatedfrom=lastupdatedfrom,
            lastupdatedto=lastupdatedto,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ApplicantMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def get_applicants_without_preload_content(
        self,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters results to any applicant associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.")] = None,
        applicationstatuses: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the applicant application status. If no status is specified, applicants with an application in any status will be returned.")] = None,
        unitids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to applicants associated to any of the specified rental property unit identifiers.")] = None,
        name: Annotated[Optional[StrictStr], Field(description="Filters results to applicants whose name *contains* the specified value.")] = None,
        email: Annotated[Optional[StrictStr], Field(description="Filters results to applicants whose email *contains* the specified value")] = None,
        applicationsubmittedstartdate: Annotated[Optional[datetime], Field(description="Filters results to any applicant who submitted an application on or after the date specified.")] = None,
        applicationsubmittedenddate: Annotated[Optional[datetime], Field(description="Filters results to any applicant who submitted an application on or prior to the date specified.")] = None,
        lastupdatedfrom: Annotated[Optional[datetime], Field(description="Filters results to any applicants that were updated on or after the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[Optional[datetime], Field(description="Filters results to any applicants that were updated on or before the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
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
        """Retrieve all applicants

        Retrieves all applicants.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param entityid: Filters results to any applicant associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.
        :type entityid: int
        :param entitytype: Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified.
        :type entitytype: str
        :param applicationstatuses: Filters results by the applicant application status. If no status is specified, applicants with an application in any status will be returned.
        :type applicationstatuses: List[str]
        :param unitids: Filters results to applicants associated to any of the specified rental property unit identifiers.
        :type unitids: List[int]
        :param name: Filters results to applicants whose name *contains* the specified value.
        :type name: str
        :param email: Filters results to applicants whose email *contains* the specified value
        :type email: str
        :param applicationsubmittedstartdate: Filters results to any applicant who submitted an application on or after the date specified.
        :type applicationsubmittedstartdate: datetime
        :param applicationsubmittedenddate: Filters results to any applicant who submitted an application on or prior to the date specified.
        :type applicationsubmittedenddate: datetime
        :param lastupdatedfrom: Filters results to any applicants that were updated on or after the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
        :type lastupdatedfrom: datetime
        :param lastupdatedto: Filters results to any applicants that were updated on or before the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
        :type lastupdatedto: datetime
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

        _param = self._get_applicants_serialize(
            entityid=entityid,
            entitytype=entitytype,
            applicationstatuses=applicationstatuses,
            unitids=unitids,
            name=name,
            email=email,
            applicationsubmittedstartdate=applicationsubmittedstartdate,
            applicationsubmittedenddate=applicationsubmittedenddate,
            lastupdatedfrom=lastupdatedfrom,
            lastupdatedto=lastupdatedto,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ApplicantMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_applicants_serialize(
        self,
        entityid,
        entitytype,
        applicationstatuses,
        unitids,
        name,
        email,
        applicationsubmittedstartdate,
        applicationsubmittedenddate,
        lastupdatedfrom,
        lastupdatedto,
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
            'applicationstatuses': 'multi',
            'unitids': 'multi',
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
        # process the query parameters
        if entityid is not None:
            
            _query_params.append(('entityid', entityid))
            
        if entitytype is not None:
            
            _query_params.append(('entitytype', entitytype))
            
        if applicationstatuses is not None:
            
            _query_params.append(('applicationstatuses', applicationstatuses))
            
        if unitids is not None:
            
            _query_params.append(('unitids', unitids))
            
        if name is not None:
            
            _query_params.append(('name', name))
            
        if email is not None:
            
            _query_params.append(('email', email))
            
        if applicationsubmittedstartdate is not None:
            if isinstance(applicationsubmittedstartdate, datetime):
                _query_params.append(
                    (
                        'applicationsubmittedstartdate',
                        applicationsubmittedstartdate.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('applicationsubmittedstartdate', applicationsubmittedstartdate))
            
        if applicationsubmittedenddate is not None:
            if isinstance(applicationsubmittedenddate, datetime):
                _query_params.append(
                    (
                        'applicationsubmittedenddate',
                        applicationsubmittedenddate.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('applicationsubmittedenddate', applicationsubmittedenddate))
            
        if lastupdatedfrom is not None:
            if isinstance(lastupdatedfrom, datetime):
                _query_params.append(
                    (
                        'lastupdatedfrom',
                        lastupdatedfrom.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('lastupdatedfrom', lastupdatedfrom))
            
        if lastupdatedto is not None:
            if isinstance(lastupdatedto, datetime):
                _query_params.append(
                    (
                        'lastupdatedto',
                        lastupdatedto.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('lastupdatedto', lastupdatedto))
            
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
            resource_path='/v1/applicants',
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
    def get_application_for_applicant_by_id(
        self,
        applicant_id: StrictInt,
        application_id: StrictInt,
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
    ) -> ApplicationMessage:
        """Retrieve an application

        Retrieves an application.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
        :param application_id: (required)
        :type application_id: int
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

        _param = self._get_application_for_applicant_by_id_serialize(
            applicant_id=applicant_id,
            application_id=application_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicationMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_application_for_applicant_by_id_with_http_info(
        self,
        applicant_id: StrictInt,
        application_id: StrictInt,
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
    ) -> ApiResponse[ApplicationMessage]:
        """Retrieve an application

        Retrieves an application.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
        :param application_id: (required)
        :type application_id: int
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

        _param = self._get_application_for_applicant_by_id_serialize(
            applicant_id=applicant_id,
            application_id=application_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicationMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def get_application_for_applicant_by_id_without_preload_content(
        self,
        applicant_id: StrictInt,
        application_id: StrictInt,
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
        """Retrieve an application

        Retrieves an application.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
        :param application_id: (required)
        :type application_id: int
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

        _param = self._get_application_for_applicant_by_id_serialize(
            applicant_id=applicant_id,
            application_id=application_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicationMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_application_for_applicant_by_id_serialize(
        self,
        applicant_id,
        application_id,
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
        if applicant_id is not None:
            _path_params['applicantId'] = applicant_id
        if application_id is not None:
            _path_params['applicationId'] = application_id
        # process the query parameters
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
            resource_path='/v1/applicants/{applicantId}/applications/{applicationId}',
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
    def get_applications_for_applicant(
        self,
        applicant_id: StrictInt,
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
    ) -> List[ApplicationMessage]:
        """Retrieve all applications

        Retrieves all the applications for a given applicant.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
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

        _param = self._get_applications_for_applicant_serialize(
            applicant_id=applicant_id,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ApplicationMessage]",
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
    def get_applications_for_applicant_with_http_info(
        self,
        applicant_id: StrictInt,
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
    ) -> ApiResponse[List[ApplicationMessage]]:
        """Retrieve all applications

        Retrieves all the applications for a given applicant.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
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

        _param = self._get_applications_for_applicant_serialize(
            applicant_id=applicant_id,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ApplicationMessage]",
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
    def get_applications_for_applicant_without_preload_content(
        self,
        applicant_id: StrictInt,
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
        """Retrieve all applications

        Retrieves all the applications for a given applicant.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View`

        :param applicant_id: (required)
        :type applicant_id: int
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

        _param = self._get_applications_for_applicant_serialize(
            applicant_id=applicant_id,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ApplicationMessage]",
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


    def _get_applications_for_applicant_serialize(
        self,
        applicant_id,
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
        if applicant_id is not None:
            _path_params['applicantId'] = applicant_id
        # process the query parameters
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
            resource_path='/v1/applicants/{applicantId}/applications',
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
    def update_applicant(
        self,
        applicant_id: StrictInt,
        applicant_put_message: ApplicantPutMessage,
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
    ) -> ApplicantMessage:
        """Update an applicant

        Updates an applicant.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_id: (required)
        :type applicant_id: int
        :param applicant_put_message: (required)
        :type applicant_put_message: ApplicantPutMessage
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

        _param = self._update_applicant_serialize(
            applicant_id=applicant_id,
            applicant_put_message=applicant_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def update_applicant_with_http_info(
        self,
        applicant_id: StrictInt,
        applicant_put_message: ApplicantPutMessage,
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
    ) -> ApiResponse[ApplicantMessage]:
        """Update an applicant

        Updates an applicant.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_id: (required)
        :type applicant_id: int
        :param applicant_put_message: (required)
        :type applicant_put_message: ApplicantPutMessage
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

        _param = self._update_applicant_serialize(
            applicant_id=applicant_id,
            applicant_put_message=applicant_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def update_applicant_without_preload_content(
        self,
        applicant_id: StrictInt,
        applicant_put_message: ApplicantPutMessage,
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
        """Update an applicant

        Updates an applicant.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_id: (required)
        :type applicant_id: int
        :param applicant_put_message: (required)
        :type applicant_put_message: ApplicantPutMessage
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

        _param = self._update_applicant_serialize(
            applicant_id=applicant_id,
            applicant_put_message=applicant_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_applicant_serialize(
        self,
        applicant_id,
        applicant_put_message,
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
        if applicant_id is not None:
            _path_params['applicantId'] = applicant_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if applicant_put_message is not None:
            _body_params = applicant_put_message


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
            resource_path='/v1/applicants/{applicantId}',
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
    def update_applicant_group(
        self,
        applicant_group_id: StrictInt,
        applicant_group_put_message: ApplicantGroupPutMessage,
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
    ) -> ApplicantGroupMessage:
        """Update an applicant group

        Updates an applicant group.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param applicant_group_put_message: (required)
        :type applicant_group_put_message: ApplicantGroupPutMessage
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

        _param = self._update_applicant_group_serialize(
            applicant_group_id=applicant_group_id,
            applicant_group_put_message=applicant_group_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantGroupMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def update_applicant_group_with_http_info(
        self,
        applicant_group_id: StrictInt,
        applicant_group_put_message: ApplicantGroupPutMessage,
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
    ) -> ApiResponse[ApplicantGroupMessage]:
        """Update an applicant group

        Updates an applicant group.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param applicant_group_put_message: (required)
        :type applicant_group_put_message: ApplicantGroupPutMessage
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

        _param = self._update_applicant_group_serialize(
            applicant_group_id=applicant_group_id,
            applicant_group_put_message=applicant_group_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantGroupMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def update_applicant_group_without_preload_content(
        self,
        applicant_group_id: StrictInt,
        applicant_group_put_message: ApplicantGroupPutMessage,
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
        """Update an applicant group

        Updates an applicant group.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param applicant_group_put_message: (required)
        :type applicant_group_put_message: ApplicantGroupPutMessage
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

        _param = self._update_applicant_group_serialize(
            applicant_group_id=applicant_group_id,
            applicant_group_put_message=applicant_group_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicantGroupMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_applicant_group_serialize(
        self,
        applicant_group_id,
        applicant_group_put_message,
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
        if applicant_group_id is not None:
            _path_params['applicantGroupId'] = applicant_group_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if applicant_group_put_message is not None:
            _body_params = applicant_group_put_message


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
            resource_path='/v1/applicants/groups/{applicantGroupId}',
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
    def update_application(
        self,
        applicant_id: StrictInt,
        application_id: StrictInt,
        application_put_message: ApplicationPutMessage,
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
    ) -> ApplicationMessage:
        """Update an application

        Updates a rental application.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_id: (required)
        :type applicant_id: int
        :param application_id: (required)
        :type application_id: int
        :param application_put_message: (required)
        :type application_put_message: ApplicationPutMessage
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

        _param = self._update_application_serialize(
            applicant_id=applicant_id,
            application_id=application_id,
            application_put_message=application_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicationMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def update_application_with_http_info(
        self,
        applicant_id: StrictInt,
        application_id: StrictInt,
        application_put_message: ApplicationPutMessage,
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
    ) -> ApiResponse[ApplicationMessage]:
        """Update an application

        Updates a rental application.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_id: (required)
        :type applicant_id: int
        :param application_id: (required)
        :type application_id: int
        :param application_put_message: (required)
        :type application_put_message: ApplicationPutMessage
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

        _param = self._update_application_serialize(
            applicant_id=applicant_id,
            application_id=application_id,
            application_put_message=application_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicationMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def update_application_without_preload_content(
        self,
        applicant_id: StrictInt,
        application_id: StrictInt,
        application_put_message: ApplicationPutMessage,
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
        """Update an application

        Updates a rental application.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_id: (required)
        :type applicant_id: int
        :param application_id: (required)
        :type application_id: int
        :param application_put_message: (required)
        :type application_put_message: ApplicationPutMessage
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

        _param = self._update_application_serialize(
            applicant_id=applicant_id,
            application_id=application_id,
            application_put_message=application_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicationMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_application_serialize(
        self,
        applicant_id,
        application_id,
        application_put_message,
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
        if applicant_id is not None:
            _path_params['applicantId'] = applicant_id
        if application_id is not None:
            _path_params['applicationId'] = application_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if application_put_message is not None:
            _body_params = application_put_message


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
            resource_path='/v1/applicants/{applicantId}/applications/{applicationId}',
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
    def update_application_group_note(
        self,
        applicant_group_id: StrictInt,
        note_id: StrictInt,
        note_put_message: NotePutMessage,
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
    ) -> NoteMessage:
        """Update an applicant group note

        Updates an applicant group note.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param note_id: (required)
        :type note_id: int
        :param note_put_message: (required)
        :type note_put_message: NotePutMessage
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

        _param = self._update_application_group_note_serialize(
            applicant_group_id=applicant_group_id,
            note_id=note_id,
            note_put_message=note_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def update_application_group_note_with_http_info(
        self,
        applicant_group_id: StrictInt,
        note_id: StrictInt,
        note_put_message: NotePutMessage,
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
    ) -> ApiResponse[NoteMessage]:
        """Update an applicant group note

        Updates an applicant group note.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param note_id: (required)
        :type note_id: int
        :param note_put_message: (required)
        :type note_put_message: NotePutMessage
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

        _param = self._update_application_group_note_serialize(
            applicant_group_id=applicant_group_id,
            note_id=note_id,
            note_put_message=note_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
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
    def update_application_group_note_without_preload_content(
        self,
        applicant_group_id: StrictInt,
        note_id: StrictInt,
        note_put_message: NotePutMessage,
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
        """Update an applicant group note

        Updates an applicant group note.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Rentals > Applicants</span> - `View` `Edit`

        :param applicant_group_id: (required)
        :type applicant_group_id: int
        :param note_id: (required)
        :type note_id: int
        :param note_put_message: (required)
        :type note_put_message: NotePutMessage
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

        _param = self._update_application_group_note_serialize(
            applicant_group_id=applicant_group_id,
            note_id=note_id,
            note_put_message=note_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NoteMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_application_group_note_serialize(
        self,
        applicant_group_id,
        note_id,
        note_put_message,
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
        if applicant_group_id is not None:
            _path_params['applicantGroupId'] = applicant_group_id
        if note_id is not None:
            _path_params['noteId'] = note_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if note_put_message is not None:
            _body_params = note_put_message


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
            resource_path='/v1/applicants/groups/{applicantGroupId}/notes/{noteId}',
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


