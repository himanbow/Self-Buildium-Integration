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
from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.work_order_message import WorkOrderMessage
from openapi_client.models.work_order_post_message import WorkOrderPostMessage
from openapi_client.models.work_order_put_message import WorkOrderPutMessage

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class WorkOrdersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_work_order(
        self,
        work_order_post_message: WorkOrderPostMessage,
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
    ) -> WorkOrderMessage:
        """Create a work order

        Creates a work order.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View` `Edit`

        :param work_order_post_message: (required)
        :type work_order_post_message: WorkOrderPostMessage
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

        _param = self._create_work_order_serialize(
            work_order_post_message=work_order_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "WorkOrderMessage",
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
    def create_work_order_with_http_info(
        self,
        work_order_post_message: WorkOrderPostMessage,
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
    ) -> ApiResponse[WorkOrderMessage]:
        """Create a work order

        Creates a work order.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View` `Edit`

        :param work_order_post_message: (required)
        :type work_order_post_message: WorkOrderPostMessage
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

        _param = self._create_work_order_serialize(
            work_order_post_message=work_order_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "WorkOrderMessage",
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
    def create_work_order_without_preload_content(
        self,
        work_order_post_message: WorkOrderPostMessage,
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
        """Create a work order

        Creates a work order.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View` `Edit`

        :param work_order_post_message: (required)
        :type work_order_post_message: WorkOrderPostMessage
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

        _param = self._create_work_order_serialize(
            work_order_post_message=work_order_post_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "WorkOrderMessage",
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


    def _create_work_order_serialize(
        self,
        work_order_post_message,
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
        if work_order_post_message is not None:
            _body_params = work_order_post_message


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
            resource_path='/v1/workorders',
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
    def get_all_work_orders(
        self,
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters results to any work order associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        statuses: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the status of the task associated with the work order. If no status is specified, work orders with any status will be returned.")] = None,
        type: Annotated[Optional[StrictStr], Field(description="Filters results to any work order with an associated task with the task type specified.")] = None,
        unitid: Annotated[Optional[StrictInt], Field(description="Filters results to any work order associated with the unit identifier.")] = None,
        unitagreementid: Annotated[Optional[StrictInt], Field(description="Filters results to any work order associated with the unit agreement identifier specified.")] = None,
        lastupdatedfrom: Annotated[Optional[date], Field(description="Filters results to any work orders were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        lastupdatedto: Annotated[Optional[date], Field(description="Filters results to any work orders were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedatefrom: Annotated[Optional[date], Field(description="Filters results to any work orders with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedateto: Annotated[Optional[date], Field(description="Filters results to any work orders with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        taskcategoryid: Annotated[Optional[StrictInt], Field(description="Filters results to any work orders whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.")] = None,
        priorities: Annotated[Optional[List[StrictStr]], Field(description="Filters results to any work orders that have been assigned to the specified staff user identifier.")] = None,
        assignedtoid: Annotated[Optional[StrictInt], Field(description="Filters results to any work orders that have been assigned to the specified staff user identifier.")] = None,
        vendorids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to any work orders that have been assigned to the specified vendor identifier.")] = None,
        amountfrom: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filters results to any work orders whose total amounts are equal or greater than the specified amount.")] = None,
        amountto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filters results to any work orders whose total amounts are equal or less than the specified amount.")] = None,
        isbilled: Annotated[Optional[StrictBool], Field(description="Filters results to work orders that have an associated bill.")] = None,
        title: Annotated[Optional[StrictStr], Field(description="Filters results to any work orders whose title *contains* the specified value.")] = None,
        taskids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to work orders that have an associated to a task in the specified list.")] = None,
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
    ) -> List[WorkOrderMessage]:
        """Retrieve all work orders

        Retrieves a list of work orders.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View`

        :param entitytype: Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.
        :type entitytype: str
        :param entityid: Filters results to any work order associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.
        :type entityid: int
        :param statuses: Filters results by the status of the task associated with the work order. If no status is specified, work orders with any status will be returned.
        :type statuses: List[str]
        :param type: Filters results to any work order with an associated task with the task type specified.
        :type type: str
        :param unitid: Filters results to any work order associated with the unit identifier.
        :type unitid: int
        :param unitagreementid: Filters results to any work order associated with the unit agreement identifier specified.
        :type unitagreementid: int
        :param lastupdatedfrom: Filters results to any work orders were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.
        :type lastupdatedfrom: date
        :param lastupdatedto: Filters results to any work orders were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.
        :type lastupdatedto: date
        :param duedatefrom: Filters results to any work orders with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.
        :type duedatefrom: date
        :param duedateto: Filters results to any work orders with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.
        :type duedateto: date
        :param taskcategoryid: Filters results to any work orders whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.
        :type taskcategoryid: int
        :param priorities: Filters results to any work orders that have been assigned to the specified staff user identifier.
        :type priorities: List[str]
        :param assignedtoid: Filters results to any work orders that have been assigned to the specified staff user identifier.
        :type assignedtoid: int
        :param vendorids: Filters results to any work orders that have been assigned to the specified vendor identifier.
        :type vendorids: List[int]
        :param amountfrom: Filters results to any work orders whose total amounts are equal or greater than the specified amount.
        :type amountfrom: float
        :param amountto: Filters results to any work orders whose total amounts are equal or less than the specified amount.
        :type amountto: float
        :param isbilled: Filters results to work orders that have an associated bill.
        :type isbilled: bool
        :param title: Filters results to any work orders whose title *contains* the specified value.
        :type title: str
        :param taskids: Filters results to work orders that have an associated to a task in the specified list.
        :type taskids: List[int]
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

        _param = self._get_all_work_orders_serialize(
            entitytype=entitytype,
            entityid=entityid,
            statuses=statuses,
            type=type,
            unitid=unitid,
            unitagreementid=unitagreementid,
            lastupdatedfrom=lastupdatedfrom,
            lastupdatedto=lastupdatedto,
            duedatefrom=duedatefrom,
            duedateto=duedateto,
            taskcategoryid=taskcategoryid,
            priorities=priorities,
            assignedtoid=assignedtoid,
            vendorids=vendorids,
            amountfrom=amountfrom,
            amountto=amountto,
            isbilled=isbilled,
            title=title,
            taskids=taskids,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[WorkOrderMessage]",
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
    def get_all_work_orders_with_http_info(
        self,
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters results to any work order associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        statuses: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the status of the task associated with the work order. If no status is specified, work orders with any status will be returned.")] = None,
        type: Annotated[Optional[StrictStr], Field(description="Filters results to any work order with an associated task with the task type specified.")] = None,
        unitid: Annotated[Optional[StrictInt], Field(description="Filters results to any work order associated with the unit identifier.")] = None,
        unitagreementid: Annotated[Optional[StrictInt], Field(description="Filters results to any work order associated with the unit agreement identifier specified.")] = None,
        lastupdatedfrom: Annotated[Optional[date], Field(description="Filters results to any work orders were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        lastupdatedto: Annotated[Optional[date], Field(description="Filters results to any work orders were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedatefrom: Annotated[Optional[date], Field(description="Filters results to any work orders with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedateto: Annotated[Optional[date], Field(description="Filters results to any work orders with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        taskcategoryid: Annotated[Optional[StrictInt], Field(description="Filters results to any work orders whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.")] = None,
        priorities: Annotated[Optional[List[StrictStr]], Field(description="Filters results to any work orders that have been assigned to the specified staff user identifier.")] = None,
        assignedtoid: Annotated[Optional[StrictInt], Field(description="Filters results to any work orders that have been assigned to the specified staff user identifier.")] = None,
        vendorids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to any work orders that have been assigned to the specified vendor identifier.")] = None,
        amountfrom: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filters results to any work orders whose total amounts are equal or greater than the specified amount.")] = None,
        amountto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filters results to any work orders whose total amounts are equal or less than the specified amount.")] = None,
        isbilled: Annotated[Optional[StrictBool], Field(description="Filters results to work orders that have an associated bill.")] = None,
        title: Annotated[Optional[StrictStr], Field(description="Filters results to any work orders whose title *contains* the specified value.")] = None,
        taskids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to work orders that have an associated to a task in the specified list.")] = None,
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
    ) -> ApiResponse[List[WorkOrderMessage]]:
        """Retrieve all work orders

        Retrieves a list of work orders.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View`

        :param entitytype: Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.
        :type entitytype: str
        :param entityid: Filters results to any work order associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.
        :type entityid: int
        :param statuses: Filters results by the status of the task associated with the work order. If no status is specified, work orders with any status will be returned.
        :type statuses: List[str]
        :param type: Filters results to any work order with an associated task with the task type specified.
        :type type: str
        :param unitid: Filters results to any work order associated with the unit identifier.
        :type unitid: int
        :param unitagreementid: Filters results to any work order associated with the unit agreement identifier specified.
        :type unitagreementid: int
        :param lastupdatedfrom: Filters results to any work orders were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.
        :type lastupdatedfrom: date
        :param lastupdatedto: Filters results to any work orders were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.
        :type lastupdatedto: date
        :param duedatefrom: Filters results to any work orders with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.
        :type duedatefrom: date
        :param duedateto: Filters results to any work orders with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.
        :type duedateto: date
        :param taskcategoryid: Filters results to any work orders whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.
        :type taskcategoryid: int
        :param priorities: Filters results to any work orders that have been assigned to the specified staff user identifier.
        :type priorities: List[str]
        :param assignedtoid: Filters results to any work orders that have been assigned to the specified staff user identifier.
        :type assignedtoid: int
        :param vendorids: Filters results to any work orders that have been assigned to the specified vendor identifier.
        :type vendorids: List[int]
        :param amountfrom: Filters results to any work orders whose total amounts are equal or greater than the specified amount.
        :type amountfrom: float
        :param amountto: Filters results to any work orders whose total amounts are equal or less than the specified amount.
        :type amountto: float
        :param isbilled: Filters results to work orders that have an associated bill.
        :type isbilled: bool
        :param title: Filters results to any work orders whose title *contains* the specified value.
        :type title: str
        :param taskids: Filters results to work orders that have an associated to a task in the specified list.
        :type taskids: List[int]
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

        _param = self._get_all_work_orders_serialize(
            entitytype=entitytype,
            entityid=entityid,
            statuses=statuses,
            type=type,
            unitid=unitid,
            unitagreementid=unitagreementid,
            lastupdatedfrom=lastupdatedfrom,
            lastupdatedto=lastupdatedto,
            duedatefrom=duedatefrom,
            duedateto=duedateto,
            taskcategoryid=taskcategoryid,
            priorities=priorities,
            assignedtoid=assignedtoid,
            vendorids=vendorids,
            amountfrom=amountfrom,
            amountto=amountto,
            isbilled=isbilled,
            title=title,
            taskids=taskids,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[WorkOrderMessage]",
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
    def get_all_work_orders_without_preload_content(
        self,
        entitytype: Annotated[Optional[StrictStr], Field(description="Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.")] = None,
        entityid: Annotated[Optional[StrictInt], Field(description="Filters results to any work order associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.")] = None,
        statuses: Annotated[Optional[List[StrictStr]], Field(description="Filters results by the status of the task associated with the work order. If no status is specified, work orders with any status will be returned.")] = None,
        type: Annotated[Optional[StrictStr], Field(description="Filters results to any work order with an associated task with the task type specified.")] = None,
        unitid: Annotated[Optional[StrictInt], Field(description="Filters results to any work order associated with the unit identifier.")] = None,
        unitagreementid: Annotated[Optional[StrictInt], Field(description="Filters results to any work order associated with the unit agreement identifier specified.")] = None,
        lastupdatedfrom: Annotated[Optional[date], Field(description="Filters results to any work orders were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        lastupdatedto: Annotated[Optional[date], Field(description="Filters results to any work orders were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedatefrom: Annotated[Optional[date], Field(description="Filters results to any work orders with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        duedateto: Annotated[Optional[date], Field(description="Filters results to any work orders with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.")] = None,
        taskcategoryid: Annotated[Optional[StrictInt], Field(description="Filters results to any work orders whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.")] = None,
        priorities: Annotated[Optional[List[StrictStr]], Field(description="Filters results to any work orders that have been assigned to the specified staff user identifier.")] = None,
        assignedtoid: Annotated[Optional[StrictInt], Field(description="Filters results to any work orders that have been assigned to the specified staff user identifier.")] = None,
        vendorids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to any work orders that have been assigned to the specified vendor identifier.")] = None,
        amountfrom: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filters results to any work orders whose total amounts are equal or greater than the specified amount.")] = None,
        amountto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filters results to any work orders whose total amounts are equal or less than the specified amount.")] = None,
        isbilled: Annotated[Optional[StrictBool], Field(description="Filters results to work orders that have an associated bill.")] = None,
        title: Annotated[Optional[StrictStr], Field(description="Filters results to any work orders whose title *contains* the specified value.")] = None,
        taskids: Annotated[Optional[List[StrictInt]], Field(description="Filters results to work orders that have an associated to a task in the specified list.")] = None,
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
        """Retrieve all work orders

        Retrieves a list of work orders.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View`

        :param entitytype: Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated.
        :type entitytype: str
        :param entityid: Filters results to any work order associated with the specified entity id value. The value must be of the type specified in the `EntityType` field.
        :type entityid: int
        :param statuses: Filters results by the status of the task associated with the work order. If no status is specified, work orders with any status will be returned.
        :type statuses: List[str]
        :param type: Filters results to any work order with an associated task with the task type specified.
        :type type: str
        :param unitid: Filters results to any work order associated with the unit identifier.
        :type unitid: int
        :param unitagreementid: Filters results to any work order associated with the unit agreement identifier specified.
        :type unitagreementid: int
        :param lastupdatedfrom: Filters results to any work orders were updated on or after the specified date. The value must be formatted as YYYY-MM-DD.
        :type lastupdatedfrom: date
        :param lastupdatedto: Filters results to any work orders were updated on or before the specified date. The value must be formatted as YYYY-MM-DD.
        :type lastupdatedto: date
        :param duedatefrom: Filters results to any work orders with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD.
        :type duedatefrom: date
        :param duedateto: Filters results to any work orders with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD.
        :type duedateto: date
        :param taskcategoryid: Filters results to any work orders whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned.
        :type taskcategoryid: int
        :param priorities: Filters results to any work orders that have been assigned to the specified staff user identifier.
        :type priorities: List[str]
        :param assignedtoid: Filters results to any work orders that have been assigned to the specified staff user identifier.
        :type assignedtoid: int
        :param vendorids: Filters results to any work orders that have been assigned to the specified vendor identifier.
        :type vendorids: List[int]
        :param amountfrom: Filters results to any work orders whose total amounts are equal or greater than the specified amount.
        :type amountfrom: float
        :param amountto: Filters results to any work orders whose total amounts are equal or less than the specified amount.
        :type amountto: float
        :param isbilled: Filters results to work orders that have an associated bill.
        :type isbilled: bool
        :param title: Filters results to any work orders whose title *contains* the specified value.
        :type title: str
        :param taskids: Filters results to work orders that have an associated to a task in the specified list.
        :type taskids: List[int]
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

        _param = self._get_all_work_orders_serialize(
            entitytype=entitytype,
            entityid=entityid,
            statuses=statuses,
            type=type,
            unitid=unitid,
            unitagreementid=unitagreementid,
            lastupdatedfrom=lastupdatedfrom,
            lastupdatedto=lastupdatedto,
            duedatefrom=duedatefrom,
            duedateto=duedateto,
            taskcategoryid=taskcategoryid,
            priorities=priorities,
            assignedtoid=assignedtoid,
            vendorids=vendorids,
            amountfrom=amountfrom,
            amountto=amountto,
            isbilled=isbilled,
            title=title,
            taskids=taskids,
            orderby=orderby,
            offset=offset,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[WorkOrderMessage]",
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


    def _get_all_work_orders_serialize(
        self,
        entitytype,
        entityid,
        statuses,
        type,
        unitid,
        unitagreementid,
        lastupdatedfrom,
        lastupdatedto,
        duedatefrom,
        duedateto,
        taskcategoryid,
        priorities,
        assignedtoid,
        vendorids,
        amountfrom,
        amountto,
        isbilled,
        title,
        taskids,
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
            'statuses': 'multi',
            'priorities': 'multi',
            'vendorids': 'multi',
            'taskids': 'multi',
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
            
        if statuses is not None:
            
            _query_params.append(('statuses', statuses))
            
        if type is not None:
            
            _query_params.append(('type', type))
            
        if unitid is not None:
            
            _query_params.append(('unitid', unitid))
            
        if unitagreementid is not None:
            
            _query_params.append(('unitagreementid', unitagreementid))
            
        if lastupdatedfrom is not None:
            if isinstance(lastupdatedfrom, date):
                _query_params.append(
                    (
                        'lastupdatedfrom',
                        lastupdatedfrom.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('lastupdatedfrom', lastupdatedfrom))
            
        if lastupdatedto is not None:
            if isinstance(lastupdatedto, date):
                _query_params.append(
                    (
                        'lastupdatedto',
                        lastupdatedto.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('lastupdatedto', lastupdatedto))
            
        if duedatefrom is not None:
            if isinstance(duedatefrom, date):
                _query_params.append(
                    (
                        'duedatefrom',
                        duedatefrom.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('duedatefrom', duedatefrom))
            
        if duedateto is not None:
            if isinstance(duedateto, date):
                _query_params.append(
                    (
                        'duedateto',
                        duedateto.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('duedateto', duedateto))
            
        if taskcategoryid is not None:
            
            _query_params.append(('taskcategoryid', taskcategoryid))
            
        if priorities is not None:
            
            _query_params.append(('priorities', priorities))
            
        if assignedtoid is not None:
            
            _query_params.append(('assignedtoid', assignedtoid))
            
        if vendorids is not None:
            
            _query_params.append(('vendorids', vendorids))
            
        if amountfrom is not None:
            
            _query_params.append(('amountfrom', amountfrom))
            
        if amountto is not None:
            
            _query_params.append(('amountto', amountto))
            
        if isbilled is not None:
            
            _query_params.append(('isbilled', isbilled))
            
        if title is not None:
            
            _query_params.append(('title', title))
            
        if taskids is not None:
            
            _query_params.append(('taskids', taskids))
            
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
            resource_path='/v1/workorders',
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
    def get_work_order_by_id(
        self,
        work_order_id: StrictInt,
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
    ) -> WorkOrderMessage:
        """Retrieve a work order

        Retrieves a specific work order.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View`

        :param work_order_id: (required)
        :type work_order_id: int
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

        _param = self._get_work_order_by_id_serialize(
            work_order_id=work_order_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorkOrderMessage",
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
    def get_work_order_by_id_with_http_info(
        self,
        work_order_id: StrictInt,
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
    ) -> ApiResponse[WorkOrderMessage]:
        """Retrieve a work order

        Retrieves a specific work order.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View`

        :param work_order_id: (required)
        :type work_order_id: int
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

        _param = self._get_work_order_by_id_serialize(
            work_order_id=work_order_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorkOrderMessage",
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
    def get_work_order_by_id_without_preload_content(
        self,
        work_order_id: StrictInt,
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
        """Retrieve a work order

        Retrieves a specific work order.  <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View`

        :param work_order_id: (required)
        :type work_order_id: int
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

        _param = self._get_work_order_by_id_serialize(
            work_order_id=work_order_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorkOrderMessage",
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


    def _get_work_order_by_id_serialize(
        self,
        work_order_id,
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
        if work_order_id is not None:
            _path_params['workOrderId'] = work_order_id
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
            resource_path='/v1/workorders/{workOrderId}',
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
    def update_work_order(
        self,
        work_order_id: StrictInt,
        work_order_put_message: WorkOrderPutMessage,
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
    ) -> WorkOrderMessage:
        """Update a work order

        Updates a work order.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View` `Edit`

        :param work_order_id: (required)
        :type work_order_id: int
        :param work_order_put_message: (required)
        :type work_order_put_message: WorkOrderPutMessage
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

        _param = self._update_work_order_serialize(
            work_order_id=work_order_id,
            work_order_put_message=work_order_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorkOrderMessage",
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
    def update_work_order_with_http_info(
        self,
        work_order_id: StrictInt,
        work_order_put_message: WorkOrderPutMessage,
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
    ) -> ApiResponse[WorkOrderMessage]:
        """Update a work order

        Updates a work order.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View` `Edit`

        :param work_order_id: (required)
        :type work_order_id: int
        :param work_order_put_message: (required)
        :type work_order_put_message: WorkOrderPutMessage
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

        _param = self._update_work_order_serialize(
            work_order_id=work_order_id,
            work_order_put_message=work_order_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorkOrderMessage",
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
    def update_work_order_without_preload_content(
        self,
        work_order_id: StrictInt,
        work_order_put_message: WorkOrderPutMessage,
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
        """Update a work order

        Updates a work order.              <br /><br /><strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. <br />The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.              <br /><br /><h4>Required permission(s):</h4><span class=\"permissionBlock\">Maintenance > Work Orders</span> - `View` `Edit`

        :param work_order_id: (required)
        :type work_order_id: int
        :param work_order_put_message: (required)
        :type work_order_put_message: WorkOrderPutMessage
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

        _param = self._update_work_order_serialize(
            work_order_id=work_order_id,
            work_order_put_message=work_order_put_message,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorkOrderMessage",
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


    def _update_work_order_serialize(
        self,
        work_order_id,
        work_order_put_message,
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
        if work_order_id is not None:
            _path_params['workOrderId'] = work_order_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if work_order_put_message is not None:
            _body_params = work_order_put_message


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
            resource_path='/v1/workorders/{workOrderId}',
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


