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

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from openapi_client.models.gl_account_balance_message import GLAccountBalanceMessage
from openapi_client.models.gl_account_message import GLAccountMessage
from openapi_client.models.gl_account_post_message import GLAccountPostMessage
from openapi_client.models.gl_account_put_message import GLAccountPutMessage
from openapi_client.models.general_journal_entry_post_message import GeneralJournalEntryPostMessage
from openapi_client.models.general_journal_entry_put_message import GeneralJournalEntryPutMessage
from openapi_client.models.general_ledger_message import GeneralLedgerMessage
from openapi_client.models.general_ledger_transaction_message import GeneralLedgerTransactionMessage

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class GeneralLedgerApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_general_journal_entry(
        self,
        general_journal_entry_post_message: GeneralJournalEntryPostMessage,
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
    ) -> GeneralLedgerTransactionMessage:
        """Create a general journal entry

        Creates a general journal entry.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View` `Edit`

        :param general_journal_entry_post_message: (required)
        :type general_journal_entry_post_message: GeneralJournalEntryPostMessage
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

        _param = self._create_general_journal_entry_serialize(
            general_journal_entry_post_message=general_journal_entry_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "GeneralLedgerTransactionMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def create_general_journal_entry_with_http_info(
        self,
        general_journal_entry_post_message: GeneralJournalEntryPostMessage,
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
    ) -> ApiResponse[GeneralLedgerTransactionMessage]:
        """Create a general journal entry

        Creates a general journal entry.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View` `Edit`

        :param general_journal_entry_post_message: (required)
        :type general_journal_entry_post_message: GeneralJournalEntryPostMessage
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

        _param = self._create_general_journal_entry_serialize(
            general_journal_entry_post_message=general_journal_entry_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "GeneralLedgerTransactionMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def create_general_journal_entry_without_preload_content(
        self,
        general_journal_entry_post_message: GeneralJournalEntryPostMessage,
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
        """Create a general journal entry

        Creates a general journal entry.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View` `Edit`

        :param general_journal_entry_post_message: (required)
        :type general_journal_entry_post_message: GeneralJournalEntryPostMessage
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

        _param = self._create_general_journal_entry_serialize(
            general_journal_entry_post_message=general_journal_entry_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "GeneralLedgerTransactionMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_general_journal_entry_serialize(
        self,
        general_journal_entry_post_message,
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
        if general_journal_entry_post_message is not None:
            _body_params = general_journal_entry_post_message


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
            resource_path='/v1/generalledger/journalentries',
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
    def create_general_ledger_account(
        self,
        gl_account_post_message: GLAccountPostMessage,
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
    ) -> GLAccountMessage:
        """Create a general ledger account

        Creates a general ledger account.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View` `Edit`

        :param gl_account_post_message: (required)
        :type gl_account_post_message: GLAccountPostMessage
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

        _param = self._create_general_ledger_account_serialize(
            gl_account_post_message=gl_account_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "GLAccountMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def create_general_ledger_account_with_http_info(
        self,
        gl_account_post_message: GLAccountPostMessage,
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
    ) -> ApiResponse[GLAccountMessage]:
        """Create a general ledger account

        Creates a general ledger account.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View` `Edit`

        :param gl_account_post_message: (required)
        :type gl_account_post_message: GLAccountPostMessage
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

        _param = self._create_general_ledger_account_serialize(
            gl_account_post_message=gl_account_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "GLAccountMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def create_general_ledger_account_without_preload_content(
        self,
        gl_account_post_message: GLAccountPostMessage,
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
        """Create a general ledger account

        Creates a general ledger account.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View` `Edit`

        :param gl_account_post_message: (required)
        :type gl_account_post_message: GLAccountPostMessage
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

        _param = self._create_general_ledger_account_serialize(
            gl_account_post_message=gl_account_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "GLAccountMessage",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
            '415': "ApiErrorResponse",
            '422': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_general_ledger_account_serialize(
        self,
        gl_account_post_message,
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
        if gl_account_post_message is not None:
            _body_params = gl_account_post_message


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
            resource_path='/v1/glaccounts',
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
    def get_all_gl_accounts(
        self,
        accounttypes: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the specified general ledger account types.")] = None,
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
    ) -> List[GLAccountMessage]:
        """Retrieve all general ledger accounts

        Retrieves a list of general ledger accounts.<br /><br />General ledger accounts are used to categorize transactions for accounting purposes.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View`

        :param accounttypes: Filters results by the specified general ledger account types.
        :type accounttypes: List[str]
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

        _param = self._get_all_gl_accounts_serialize(
            accounttypes=accounttypes,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GLAccountMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def get_all_gl_accounts_with_http_info(
        self,
        accounttypes: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the specified general ledger account types.")] = None,
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
    ) -> ApiResponse[List[GLAccountMessage]]:
        """Retrieve all general ledger accounts

        Retrieves a list of general ledger accounts.<br /><br />General ledger accounts are used to categorize transactions for accounting purposes.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View`

        :param accounttypes: Filters results by the specified general ledger account types.
        :type accounttypes: List[str]
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

        _param = self._get_all_gl_accounts_serialize(
            accounttypes=accounttypes,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GLAccountMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
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
    def get_all_gl_accounts_without_preload_content(
        self,
        accounttypes: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the specified general ledger account types.")] = None,
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
        """Retrieve all general ledger accounts

        Retrieves a list of general ledger accounts.<br /><br />General ledger accounts are used to categorize transactions for accounting purposes.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View`

        :param accounttypes: Filters results by the specified general ledger account types.
        :type accounttypes: List[str]
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

        _param = self._get_all_gl_accounts_serialize(
            accounttypes=accounttypes,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GLAccountMessage]",
            '400': "ApiErrorResponse",
            '401': "ApiErrorResponse",
            '403': "ApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_all_gl_accounts_serialize(
        self,
        accounttypes,
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
            'accounttypes': 'multi',
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
        if accounttypes is not None:
            
            _query_params.append(('accounttypes', accounttypes))
            
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
            resource_path='/v1/glaccounts',
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
    def get_all_transactions(
        self,
        startdate: Annotated[date, Field(description="Filters results to any transaction whose date is greater than or equal to the specified value.")],
        enddate: Annotated[date, Field(description="Filters results to any transaction whose date is less than or equal to the specified value.")],
        glaccountids: Annotated[List[StrictInt], Field(description="Filters results to transactions whose general ledger account belongs to the specified set of general ledger account ids.")],
        selectionentityid: Annotated[Optional[StrictInt], Field(description="Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType.")] = None,
        selectionentitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that SelectionEntityId refers to.")] = None,
        selectionentityunitid: Annotated[Optional[StrictInt], Field(description="Filters results to any transaction containing journal lines for the unitId specified. Only applicable when the SelectionEntityType is Rentals or Associations.")] = None,
        lastupdatedfrom: Annotated[Optional[datetime], Field(description="Filters results to any transactions that were updated on or after the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[Optional[datetime], Field(description="Filters results to any transactions that were updated on or before the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
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
    ) -> List[GeneralLedgerTransactionMessage]:
        """Retrieve all general ledger transactions

        Retrieves a list of general ledger transactions.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View`

        :param startdate: Filters results to any transaction whose date is greater than or equal to the specified value. (required)
        :type startdate: date
        :param enddate: Filters results to any transaction whose date is less than or equal to the specified value. (required)
        :type enddate: date
        :param glaccountids: Filters results to transactions whose general ledger account belongs to the specified set of general ledger account ids. (required)
        :type glaccountids: List[int]
        :param selectionentityid: Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType.
        :type selectionentityid: int
        :param selectionentitytype: Specifies the type of entity that SelectionEntityId refers to.
        :type selectionentitytype: str
        :param selectionentityunitid: Filters results to any transaction containing journal lines for the unitId specified. Only applicable when the SelectionEntityType is Rentals or Associations.
        :type selectionentityunitid: int
        :param lastupdatedfrom: Filters results to any transactions that were updated on or after the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
        :type lastupdatedfrom: datetime
        :param lastupdatedto: Filters results to any transactions that were updated on or before the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
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

        _param = self._get_all_transactions_serialize(
            startdate=startdate,
            enddate=enddate,
            glaccountids=glaccountids,
            selectionentityid=selectionentityid,
            selectionentitytype=selectionentitytype,
            selectionentityunitid=selectionentityunitid,
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
            '200': "List[GeneralLedgerTransactionMessage]",
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
    def get_all_transactions_with_http_info(
        self,
        startdate: Annotated[date, Field(description="Filters results to any transaction whose date is greater than or equal to the specified value.")],
        enddate: Annotated[date, Field(description="Filters results to any transaction whose date is less than or equal to the specified value.")],
        glaccountids: Annotated[List[StrictInt], Field(description="Filters results to transactions whose general ledger account belongs to the specified set of general ledger account ids.")],
        selectionentityid: Annotated[Optional[StrictInt], Field(description="Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType.")] = None,
        selectionentitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that SelectionEntityId refers to.")] = None,
        selectionentityunitid: Annotated[Optional[StrictInt], Field(description="Filters results to any transaction containing journal lines for the unitId specified. Only applicable when the SelectionEntityType is Rentals or Associations.")] = None,
        lastupdatedfrom: Annotated[Optional[datetime], Field(description="Filters results to any transactions that were updated on or after the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[Optional[datetime], Field(description="Filters results to any transactions that were updated on or before the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
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
    ) -> ApiResponse[List[GeneralLedgerTransactionMessage]]:
        """Retrieve all general ledger transactions

        Retrieves a list of general ledger transactions.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View`

        :param startdate: Filters results to any transaction whose date is greater than or equal to the specified value. (required)
        :type startdate: date
        :param enddate: Filters results to any transaction whose date is less than or equal to the specified value. (required)
        :type enddate: date
        :param glaccountids: Filters results to transactions whose general ledger account belongs to the specified set of general ledger account ids. (required)
        :type glaccountids: List[int]
        :param selectionentityid: Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType.
        :type selectionentityid: int
        :param selectionentitytype: Specifies the type of entity that SelectionEntityId refers to.
        :type selectionentitytype: str
        :param selectionentityunitid: Filters results to any transaction containing journal lines for the unitId specified. Only applicable when the SelectionEntityType is Rentals or Associations.
        :type selectionentityunitid: int
        :param lastupdatedfrom: Filters results to any transactions that were updated on or after the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
        :type lastupdatedfrom: datetime
        :param lastupdatedto: Filters results to any transactions that were updated on or before the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
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

        _param = self._get_all_transactions_serialize(
            startdate=startdate,
            enddate=enddate,
            glaccountids=glaccountids,
            selectionentityid=selectionentityid,
            selectionentitytype=selectionentitytype,
            selectionentityunitid=selectionentityunitid,
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
            '200': "List[GeneralLedgerTransactionMessage]",
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
    def get_all_transactions_without_preload_content(
        self,
        startdate: Annotated[date, Field(description="Filters results to any transaction whose date is greater than or equal to the specified value.")],
        enddate: Annotated[date, Field(description="Filters results to any transaction whose date is less than or equal to the specified value.")],
        glaccountids: Annotated[List[StrictInt], Field(description="Filters results to transactions whose general ledger account belongs to the specified set of general ledger account ids.")],
        selectionentityid: Annotated[Optional[StrictInt], Field(description="Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType.")] = None,
        selectionentitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that SelectionEntityId refers to.")] = None,
        selectionentityunitid: Annotated[Optional[StrictInt], Field(description="Filters results to any transaction containing journal lines for the unitId specified. Only applicable when the SelectionEntityType is Rentals or Associations.")] = None,
        lastupdatedfrom: Annotated[Optional[datetime], Field(description="Filters results to any transactions that were updated on or after the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
        lastupdatedto: Annotated[Optional[datetime], Field(description="Filters results to any transactions that were updated on or before the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.")] = None,
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
        """Retrieve all general ledger transactions

        Retrieves a list of general ledger transactions.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View`

        :param startdate: Filters results to any transaction whose date is greater than or equal to the specified value. (required)
        :type startdate: date
        :param enddate: Filters results to any transaction whose date is less than or equal to the specified value. (required)
        :type enddate: date
        :param glaccountids: Filters results to transactions whose general ledger account belongs to the specified set of general ledger account ids. (required)
        :type glaccountids: List[int]
        :param selectionentityid: Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType.
        :type selectionentityid: int
        :param selectionentitytype: Specifies the type of entity that SelectionEntityId refers to.
        :type selectionentitytype: str
        :param selectionentityunitid: Filters results to any transaction containing journal lines for the unitId specified. Only applicable when the SelectionEntityType is Rentals or Associations.
        :type selectionentityunitid: int
        :param lastupdatedfrom: Filters results to any transactions that were updated on or after the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
        :type lastupdatedfrom: datetime
        :param lastupdatedto: Filters results to any transactions that were updated on or before the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ.
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

        _param = self._get_all_transactions_serialize(
            startdate=startdate,
            enddate=enddate,
            glaccountids=glaccountids,
            selectionentityid=selectionentityid,
            selectionentitytype=selectionentitytype,
            selectionentityunitid=selectionentityunitid,
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
            '200': "List[GeneralLedgerTransactionMessage]",
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


    def _get_all_transactions_serialize(
        self,
        startdate,
        enddate,
        glaccountids,
        selectionentityid,
        selectionentitytype,
        selectionentityunitid,
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
            'glaccountids': 'multi',
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
        if selectionentityid is not None:
            
            _query_params.append(('selectionentityid', selectionentityid))
            
        if selectionentitytype is not None:
            
            _query_params.append(('selectionentitytype', selectionentitytype))
            
        if startdate is not None:
            if isinstance(startdate, date):
                _query_params.append(
                    (
                        'startdate',
                        startdate.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('startdate', startdate))
            
        if enddate is not None:
            if isinstance(enddate, date):
                _query_params.append(
                    (
                        'enddate',
                        enddate.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('enddate', enddate))
            
        if glaccountids is not None:
            
            _query_params.append(('glaccountids', glaccountids))
            
        if selectionentityunitid is not None:
            
            _query_params.append(('selectionentityunitid', selectionentityunitid))
            
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
            resource_path='/v1/generalledger/transactions',
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
    def get_general_ledger_entries(
        self,
        accountingbasis: Annotated[StrictStr, Field(description="The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.")],
        glaccountids: Annotated[List[StrictInt], Field(description="Filters results to entries whose general ledger account belongs to the specified set of general ledger account ids.")],
        startdate: Annotated[date, Field(description="Filters results to any entries whose start date is greater than or equal to the specified value.")],
        enddate: Annotated[date, Field(description="Filters results to any entries whose end date is less than or equal to the specified value.")],
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that `EntityId` field refers to.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters results to any general ledger entry containing line items associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
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
    ) -> List[GeneralLedgerMessage]:
        """Retrieve all general ledger entries

        Retrieves all general ledger entries              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View`

        :param accountingbasis: The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened. (required)
        :type accountingbasis: str
        :param glaccountids: Filters results to entries whose general ledger account belongs to the specified set of general ledger account ids. (required)
        :type glaccountids: List[int]
        :param startdate: Filters results to any entries whose start date is greater than or equal to the specified value. (required)
        :type startdate: date
        :param enddate: Filters results to any entries whose end date is less than or equal to the specified value. (required)
        :type enddate: date
        :param entitytype: Specifies the type of entity that `EntityId` field refers to.
        :type entitytype: str
        :param entityid: Filters results to any general ledger entry containing line items associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.
        :type entityid: int
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

        _param = self._get_general_ledger_entries_serialize(
            accountingbasis=accountingbasis,
            glaccountids=glaccountids,
            startdate=startdate,
            enddate=enddate,
            entitytype=entitytype,
            entityid=entityid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GeneralLedgerMessage]",
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
    def get_general_ledger_entries_with_http_info(
        self,
        accountingbasis: Annotated[StrictStr, Field(description="The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.")],
        glaccountids: Annotated[List[StrictInt], Field(description="Filters results to entries whose general ledger account belongs to the specified set of general ledger account ids.")],
        startdate: Annotated[date, Field(description="Filters results to any entries whose start date is greater than or equal to the specified value.")],
        enddate: Annotated[date, Field(description="Filters results to any entries whose end date is less than or equal to the specified value.")],
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that `EntityId` field refers to.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters results to any general ledger entry containing line items associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
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
    ) -> ApiResponse[List[GeneralLedgerMessage]]:
        """Retrieve all general ledger entries

        Retrieves all general ledger entries              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View`

        :param accountingbasis: The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened. (required)
        :type accountingbasis: str
        :param glaccountids: Filters results to entries whose general ledger account belongs to the specified set of general ledger account ids. (required)
        :type glaccountids: List[int]
        :param startdate: Filters results to any entries whose start date is greater than or equal to the specified value. (required)
        :type startdate: date
        :param enddate: Filters results to any entries whose end date is less than or equal to the specified value. (required)
        :type enddate: date
        :param entitytype: Specifies the type of entity that `EntityId` field refers to.
        :type entitytype: str
        :param entityid: Filters results to any general ledger entry containing line items associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.
        :type entityid: int
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

        _param = self._get_general_ledger_entries_serialize(
            accountingbasis=accountingbasis,
            glaccountids=glaccountids,
            startdate=startdate,
            enddate=enddate,
            entitytype=entitytype,
            entityid=entityid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GeneralLedgerMessage]",
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
    def get_general_ledger_entries_without_preload_content(
        self,
        accountingbasis: Annotated[StrictStr, Field(description="The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.")],
        glaccountids: Annotated[List[StrictInt], Field(description="Filters results to entries whose general ledger account belongs to the specified set of general ledger account ids.")],
        startdate: Annotated[date, Field(description="Filters results to any entries whose start date is greater than or equal to the specified value.")],
        enddate: Annotated[date, Field(description="Filters results to any entries whose end date is less than or equal to the specified value.")],
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that `EntityId` field refers to.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters results to any general ledger entry containing line items associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.")] = None,
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
        """Retrieve all general ledger entries

        Retrieves all general ledger entries              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View`

        :param accountingbasis: The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened. (required)
        :type accountingbasis: str
        :param glaccountids: Filters results to entries whose general ledger account belongs to the specified set of general ledger account ids. (required)
        :type glaccountids: List[int]
        :param startdate: Filters results to any entries whose start date is greater than or equal to the specified value. (required)
        :type startdate: date
        :param enddate: Filters results to any entries whose end date is less than or equal to the specified value. (required)
        :type enddate: date
        :param entitytype: Specifies the type of entity that `EntityId` field refers to.
        :type entitytype: str
        :param entityid: Filters results to any general ledger entry containing line items associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references.
        :type entityid: int
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

        _param = self._get_general_ledger_entries_serialize(
            accountingbasis=accountingbasis,
            glaccountids=glaccountids,
            startdate=startdate,
            enddate=enddate,
            entitytype=entitytype,
            entityid=entityid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GeneralLedgerMessage]",
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


    def _get_general_ledger_entries_serialize(
        self,
        accountingbasis,
        glaccountids,
        startdate,
        enddate,
        entitytype,
        entityid,
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
            'glaccountids': 'multi',
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
        if accountingbasis is not None:
            
            _query_params.append(('accountingbasis', accountingbasis))
            
        if entitytype is not None:
            
            _query_params.append(('entitytype', entitytype))
            
        if entityid is not None:
            
            _query_params.append(('entityid', entityid))
            
        if glaccountids is not None:
            
            _query_params.append(('glaccountids', glaccountids))
            
        if startdate is not None:
            if isinstance(startdate, date):
                _query_params.append(
                    (
                        'startdate',
                        startdate.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('startdate', startdate))
            
        if enddate is not None:
            if isinstance(enddate, date):
                _query_params.append(
                    (
                        'enddate',
                        enddate.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('enddate', enddate))
            
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
            resource_path='/v1/generalledger',
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
    def get_gl_account_balances(
        self,
        accountingbasis: Annotated[StrictStr, Field(description="The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.")],
        asofdate: Annotated[date, Field(description="Indicates the end date through which the balances will be calculated. This will include all transactions in your account until this specified date.")],
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that `EntityId` field refers to.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters transactions used in calculating the general ledger account balances to only those containing journal lines for with the specified entity id value. The entity id specified must be of the type specified in `EntityType`.")] = None,
        glaccountids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to the specified set of general ledger account identifiers.")] = None,
        aggregatebalancesbyunitid: Annotated[Optional[StrictBool], Field(description="Indicates whether to aggregate the AccountingEntityBalances by unit identifier in the response. If the value is set to true the AccountingEntityBalances will be aggregated by AccountingEntity.Unit.Id otherwise the response will have the balances aggregated by AccountingEntity.Id.")] = None,
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
    ) -> List[GLAccountBalanceMessage]:
        """Retrieve all general ledger account balances

        Retrieves all general ledger account balances as of a given date. The response includes the total balance of each account along with the subtotals for any accounting entities (company, associations or rental properties) that have transactions assigned to the account.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View`

        :param accountingbasis: The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened. (required)
        :type accountingbasis: str
        :param asofdate: Indicates the end date through which the balances will be calculated. This will include all transactions in your account until this specified date. (required)
        :type asofdate: date
        :param entitytype: Specifies the type of entity that `EntityId` field refers to.
        :type entitytype: str
        :param entityid: Filters transactions used in calculating the general ledger account balances to only those containing journal lines for with the specified entity id value. The entity id specified must be of the type specified in `EntityType`.
        :type entityid: int
        :param glaccountids: Filters results to the specified set of general ledger account identifiers.
        :type glaccountids: List[int]
        :param aggregatebalancesbyunitid: Indicates whether to aggregate the AccountingEntityBalances by unit identifier in the response. If the value is set to true the AccountingEntityBalances will be aggregated by AccountingEntity.Unit.Id otherwise the response will have the balances aggregated by AccountingEntity.Id.
        :type aggregatebalancesbyunitid: bool
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

        _param = self._get_gl_account_balances_serialize(
            accountingbasis=accountingbasis,
            asofdate=asofdate,
            entitytype=entitytype,
            entityid=entityid,
            glaccountids=glaccountids,
            aggregatebalancesbyunitid=aggregatebalancesbyunitid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GLAccountBalanceMessage]",
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
    def get_gl_account_balances_with_http_info(
        self,
        accountingbasis: Annotated[StrictStr, Field(description="The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.")],
        asofdate: Annotated[date, Field(description="Indicates the end date through which the balances will be calculated. This will include all transactions in your account until this specified date.")],
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that `EntityId` field refers to.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters transactions used in calculating the general ledger account balances to only those containing journal lines for with the specified entity id value. The entity id specified must be of the type specified in `EntityType`.")] = None,
        glaccountids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to the specified set of general ledger account identifiers.")] = None,
        aggregatebalancesbyunitid: Annotated[Optional[StrictBool], Field(description="Indicates whether to aggregate the AccountingEntityBalances by unit identifier in the response. If the value is set to true the AccountingEntityBalances will be aggregated by AccountingEntity.Unit.Id otherwise the response will have the balances aggregated by AccountingEntity.Id.")] = None,
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
    ) -> ApiResponse[List[GLAccountBalanceMessage]]:
        """Retrieve all general ledger account balances

        Retrieves all general ledger account balances as of a given date. The response includes the total balance of each account along with the subtotals for any accounting entities (company, associations or rental properties) that have transactions assigned to the account.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View`

        :param accountingbasis: The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened. (required)
        :type accountingbasis: str
        :param asofdate: Indicates the end date through which the balances will be calculated. This will include all transactions in your account until this specified date. (required)
        :type asofdate: date
        :param entitytype: Specifies the type of entity that `EntityId` field refers to.
        :type entitytype: str
        :param entityid: Filters transactions used in calculating the general ledger account balances to only those containing journal lines for with the specified entity id value. The entity id specified must be of the type specified in `EntityType`.
        :type entityid: int
        :param glaccountids: Filters results to the specified set of general ledger account identifiers.
        :type glaccountids: List[int]
        :param aggregatebalancesbyunitid: Indicates whether to aggregate the AccountingEntityBalances by unit identifier in the response. If the value is set to true the AccountingEntityBalances will be aggregated by AccountingEntity.Unit.Id otherwise the response will have the balances aggregated by AccountingEntity.Id.
        :type aggregatebalancesbyunitid: bool
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

        _param = self._get_gl_account_balances_serialize(
            accountingbasis=accountingbasis,
            asofdate=asofdate,
            entitytype=entitytype,
            entityid=entityid,
            glaccountids=glaccountids,
            aggregatebalancesbyunitid=aggregatebalancesbyunitid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GLAccountBalanceMessage]",
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
    def get_gl_account_balances_without_preload_content(
        self,
        accountingbasis: Annotated[StrictStr, Field(description="The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.")],
        asofdate: Annotated[date, Field(description="Indicates the end date through which the balances will be calculated. This will include all transactions in your account until this specified date.")],
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that `EntityId` field refers to.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters transactions used in calculating the general ledger account balances to only those containing journal lines for with the specified entity id value. The entity id specified must be of the type specified in `EntityType`.")] = None,
        glaccountids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to the specified set of general ledger account identifiers.")] = None,
        aggregatebalancesbyunitid: Annotated[Optional[StrictBool], Field(description="Indicates whether to aggregate the AccountingEntityBalances by unit identifier in the response. If the value is set to true the AccountingEntityBalances will be aggregated by AccountingEntity.Unit.Id otherwise the response will have the balances aggregated by AccountingEntity.Id.")] = None,
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
        """Retrieve all general ledger account balances

        Retrieves all general ledger account balances as of a given date. The response includes the total balance of each account along with the subtotals for any accounting entities (company, associations or rental properties) that have transactions assigned to the account.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View`

        :param accountingbasis: The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened. (required)
        :type accountingbasis: str
        :param asofdate: Indicates the end date through which the balances will be calculated. This will include all transactions in your account until this specified date. (required)
        :type asofdate: date
        :param entitytype: Specifies the type of entity that `EntityId` field refers to.
        :type entitytype: str
        :param entityid: Filters transactions used in calculating the general ledger account balances to only those containing journal lines for with the specified entity id value. The entity id specified must be of the type specified in `EntityType`.
        :type entityid: int
        :param glaccountids: Filters results to the specified set of general ledger account identifiers.
        :type glaccountids: List[int]
        :param aggregatebalancesbyunitid: Indicates whether to aggregate the AccountingEntityBalances by unit identifier in the response. If the value is set to true the AccountingEntityBalances will be aggregated by AccountingEntity.Unit.Id otherwise the response will have the balances aggregated by AccountingEntity.Id.
        :type aggregatebalancesbyunitid: bool
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

        _param = self._get_gl_account_balances_serialize(
            accountingbasis=accountingbasis,
            asofdate=asofdate,
            entitytype=entitytype,
            entityid=entityid,
            glaccountids=glaccountids,
            aggregatebalancesbyunitid=aggregatebalancesbyunitid,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GLAccountBalanceMessage]",
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


    def _get_gl_account_balances_serialize(
        self,
        accountingbasis,
        asofdate,
        entitytype,
        entityid,
        glaccountids,
        aggregatebalancesbyunitid,
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
            'glaccountids': 'multi',
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
            
        if glaccountids is not None:
            
            _query_params.append(('glaccountids', glaccountids))
            
        if accountingbasis is not None:
            
            _query_params.append(('accountingbasis', accountingbasis))
            
        if asofdate is not None:
            if isinstance(asofdate, date):
                _query_params.append(
                    (
                        'asofdate',
                        asofdate.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('asofdate', asofdate))
            
        if aggregatebalancesbyunitid is not None:
            
            _query_params.append(('aggregatebalancesbyunitid', aggregatebalancesbyunitid))
            
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
            resource_path='/v1/glaccounts/balances',
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
    def get_gl_account_by_id(
        self,
        gl_account_id: Annotated[StrictInt, Field(description="The general ledger account identifier.")],
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
    ) -> GLAccountMessage:
        """Retrieve a general ledger account

        Retrieves a specific general ledger account.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View`

        :param gl_account_id: The general ledger account identifier. (required)
        :type gl_account_id: int
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

        _param = self._get_gl_account_by_id_serialize(
            gl_account_id=gl_account_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GLAccountMessage",
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
    def get_gl_account_by_id_with_http_info(
        self,
        gl_account_id: Annotated[StrictInt, Field(description="The general ledger account identifier.")],
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
    ) -> ApiResponse[GLAccountMessage]:
        """Retrieve a general ledger account

        Retrieves a specific general ledger account.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View`

        :param gl_account_id: The general ledger account identifier. (required)
        :type gl_account_id: int
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

        _param = self._get_gl_account_by_id_serialize(
            gl_account_id=gl_account_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GLAccountMessage",
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
    def get_gl_account_by_id_without_preload_content(
        self,
        gl_account_id: Annotated[StrictInt, Field(description="The general ledger account identifier.")],
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
        """Retrieve a general ledger account

        Retrieves a specific general ledger account.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View`

        :param gl_account_id: The general ledger account identifier. (required)
        :type gl_account_id: int
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

        _param = self._get_gl_account_by_id_serialize(
            gl_account_id=gl_account_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GLAccountMessage",
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


    def _get_gl_account_by_id_serialize(
        self,
        gl_account_id,
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
        if gl_account_id is not None:
            _path_params['glAccountId'] = gl_account_id
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
            resource_path='/v1/glaccounts/{glAccountId}',
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
    def get_transaction_by_id(
        self,
        transaction_id: Annotated[StrictInt, Field(description="The general ledger transaction identifier.")],
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
    ) -> GeneralLedgerTransactionMessage:
        """Retrieve a general ledger transaction

        Retrieves a specific general ledger transaction.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View`

        :param transaction_id: The general ledger transaction identifier. (required)
        :type transaction_id: int
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

        _param = self._get_transaction_by_id_serialize(
            transaction_id=transaction_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GeneralLedgerTransactionMessage",
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
    def get_transaction_by_id_with_http_info(
        self,
        transaction_id: Annotated[StrictInt, Field(description="The general ledger transaction identifier.")],
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
    ) -> ApiResponse[GeneralLedgerTransactionMessage]:
        """Retrieve a general ledger transaction

        Retrieves a specific general ledger transaction.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View`

        :param transaction_id: The general ledger transaction identifier. (required)
        :type transaction_id: int
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

        _param = self._get_transaction_by_id_serialize(
            transaction_id=transaction_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GeneralLedgerTransactionMessage",
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
    def get_transaction_by_id_without_preload_content(
        self,
        transaction_id: Annotated[StrictInt, Field(description="The general ledger transaction identifier.")],
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
        """Retrieve a general ledger transaction

        Retrieves a specific general ledger transaction.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View`

        :param transaction_id: The general ledger transaction identifier. (required)
        :type transaction_id: int
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

        _param = self._get_transaction_by_id_serialize(
            transaction_id=transaction_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GeneralLedgerTransactionMessage",
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


    def _get_transaction_by_id_serialize(
        self,
        transaction_id,
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
        if transaction_id is not None:
            _path_params['transactionId'] = transaction_id
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
            resource_path='/v1/generalledger/transactions/{transactionId}',
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
    def update_general_journal_entry(
        self,
        journal_entry_id: StrictInt,
        general_journal_entry_put_message: GeneralJournalEntryPutMessage,
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
    ) -> GeneralLedgerTransactionMessage:
        """Update a general journal entry

        Updates a general journal entry.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View` `Edit`

        :param journal_entry_id: (required)
        :type journal_entry_id: int
        :param general_journal_entry_put_message: (required)
        :type general_journal_entry_put_message: GeneralJournalEntryPutMessage
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

        _param = self._update_general_journal_entry_serialize(
            journal_entry_id=journal_entry_id,
            general_journal_entry_put_message=general_journal_entry_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GeneralLedgerTransactionMessage",
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
    def update_general_journal_entry_with_http_info(
        self,
        journal_entry_id: StrictInt,
        general_journal_entry_put_message: GeneralJournalEntryPutMessage,
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
    ) -> ApiResponse[GeneralLedgerTransactionMessage]:
        """Update a general journal entry

        Updates a general journal entry.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View` `Edit`

        :param journal_entry_id: (required)
        :type journal_entry_id: int
        :param general_journal_entry_put_message: (required)
        :type general_journal_entry_put_message: GeneralJournalEntryPutMessage
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

        _param = self._update_general_journal_entry_serialize(
            journal_entry_id=journal_entry_id,
            general_journal_entry_put_message=general_journal_entry_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GeneralLedgerTransactionMessage",
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
    def update_general_journal_entry_without_preload_content(
        self,
        journal_entry_id: StrictInt,
        general_journal_entry_put_message: GeneralJournalEntryPutMessage,
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
        """Update a general journal entry

        Updates a general journal entry.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Transactions</span> - `View` `Edit`

        :param journal_entry_id: (required)
        :type journal_entry_id: int
        :param general_journal_entry_put_message: (required)
        :type general_journal_entry_put_message: GeneralJournalEntryPutMessage
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

        _param = self._update_general_journal_entry_serialize(
            journal_entry_id=journal_entry_id,
            general_journal_entry_put_message=general_journal_entry_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GeneralLedgerTransactionMessage",
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


    def _update_general_journal_entry_serialize(
        self,
        journal_entry_id,
        general_journal_entry_put_message,
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
        if journal_entry_id is not None:
            _path_params['journalEntryId'] = journal_entry_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if general_journal_entry_put_message is not None:
            _body_params = general_journal_entry_put_message


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
            resource_path='/v1/generalledger/journalentries/{journalEntryId}',
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
    def update_gl_account(
        self,
        gl_account_id: StrictInt,
        gl_account_put_message: GLAccountPutMessage,
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
    ) -> GLAccountMessage:
        """Update a general ledger account

        Updates a general ledger account.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View` `Edit`

        :param gl_account_id: (required)
        :type gl_account_id: int
        :param gl_account_put_message: (required)
        :type gl_account_put_message: GLAccountPutMessage
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

        _param = self._update_gl_account_serialize(
            gl_account_id=gl_account_id,
            gl_account_put_message=gl_account_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GLAccountMessage",
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
    def update_gl_account_with_http_info(
        self,
        gl_account_id: StrictInt,
        gl_account_put_message: GLAccountPutMessage,
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
    ) -> ApiResponse[GLAccountMessage]:
        """Update a general ledger account

        Updates a general ledger account.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View` `Edit`

        :param gl_account_id: (required)
        :type gl_account_id: int
        :param gl_account_put_message: (required)
        :type gl_account_put_message: GLAccountPutMessage
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

        _param = self._update_gl_account_serialize(
            gl_account_id=gl_account_id,
            gl_account_put_message=gl_account_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GLAccountMessage",
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
    def update_gl_account_without_preload_content(
        self,
        gl_account_id: StrictInt,
        gl_account_put_message: GLAccountPutMessage,
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
        """Update a general ledger account

        Updates a general ledger account.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Accounting > General Ledger Accounts</span> - `View` `Edit`

        :param gl_account_id: (required)
        :type gl_account_id: int
        :param gl_account_put_message: (required)
        :type gl_account_put_message: GLAccountPutMessage
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

        _param = self._update_gl_account_serialize(
            gl_account_id=gl_account_id,
            gl_account_put_message=gl_account_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GLAccountMessage",
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


    def _update_gl_account_serialize(
        self,
        gl_account_id,
        gl_account_put_message,
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
        if gl_account_id is not None:
            _path_params['glAccountId'] = gl_account_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if gl_account_put_message is not None:
            _body_params = gl_account_put_message


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
            resource_path='/v1/glaccounts/{glAccountId}',
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


