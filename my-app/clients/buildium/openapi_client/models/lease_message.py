# coding: utf-8

"""
    Open API, powered by Buildium

      # Introduction  ### Welcome!    Welcome to Buildium’s API—a powerful, RESTful programming interface that lets you leverage valuable Buildium data.    Using HTTP requests, you can create integrations with applications that specialize in accounting, lead tracking, and more. Enjoy greater flexibility, transparency, and control over your business!      ### What's in this Guide?    This guide is full of simple, easy-to-follow instructions that’ll help you use Buildium’s API like a pro.    Topics include:    * choosing the right resources for your use case  * making HTTP requests to any resource  * understanding data and response codes    <br />    # Getting Started  Excited to get going? We’ll walk you through the setup process.  >  **Note:** To take advantage of the Buildium Open API you must have a <a target=\"_blank\" href=\"https://www.buildium.com/pricing/\">**Premium Subscription**</a>.    ## Account Configuration  Before you can use Buildium’s API, you’ll need to make some tweaks to your account settings.    <br />    ### Enabling the API  In order to start creating your keys and making requests, you’ll need to enable the API.      >  **Tip:** You’ll need an administrator user role with access to ***Application settings*** to set things up properly.    <br />    ​ **Let's Begin!**    1. Sign in to your [Buildium](https://signin.managebuilding.com/manager/public/authentication/login?ReturnUrl=%2Fmanager%2F) account from your browser.    2. Open the ***Settings*** menu and click ***Application settings***.    3. Under ***System preferences***, click ***Api settings***. A modal will appear.    4. Click the ***Open API*** toggle to turn it on. Then click ***Save***.    <video width=\"100%\" autoplay loop muted>    <source src=\"enable_open_api.mp4\" type=\"video/mp4\" />  </video>      Congratulations! Your account's enabled. Now, you’re ready to start managing API keys.  <br />  <br />  If you are having issues enabling the API within your account you can submit a [Support](#section/API-Overview/Support) request for assistance.    <br />      ## API Keys  Account-level API keys authenticate every request and keep things secure.    API keys have two components: a “client ID” and a “secret”.    * **Client IDs** are similar to usernames. They’re used to identify your Buildium account and are safe to share.  * **Secrets** are similar to passwords. They must be kept confidential.    Whenever you make a request, you’ll need the API key’s client ID and secret. If you forget it, make a mistake, or try to use information that’s linked to a deleted key, the API will return a `401` response code.    >  **Tip:** We compiled a list of best practices that detail how securely store API keys. [Give it a read](#section/Getting-Started/Keeping-API-Keys-Safe)!    ## Creating API Keys  Now that the Open APi is enabled, you’ll be able to create API keys. You’re almost there!    >  **Tip:** You’ll need an administrator user role to complete this step, too.    <br />    **How to create an API key**    1. Sign in to your [Buildium](https://signin.managebuilding.com/manager/public/authentication/login?ReturnUrl=%2Fmanager%2F) account from your browser.    2. Open the ***Settings*** menu and click ***Developer Tools***. The page will open automatically.    3. Click the ***Create API Key*** button. A modal will appear.    4. Enter a clear, memorable name and description for your API key. It’ll make it easier to locate the right key when you make a request. Once finished, click **Next**.    5. Now, choose which pieces of Buildium data you want this API key to have access to by marking the corresponding checkboxes. Once finished, click **Next**.    6. You successfully created an API key!    > **Important:** This is your only chance to record the secret. Make sure it’s stored somewhere secure! If it’s forgotten, you’ll need to delete this key and start from scratch.    <br />    <video width=\"100%\" autoplay loop muted>    <source src=\"generate_open_api_key.mp4\" type=\"video/mp4\" />  </video>    <br />    You have now successfully created an API key and have everything you need to  send requests to the Buildium API!    Before moving on to [making your first request](#section/Getting-Started/How-to-Make-a-Request) please review [Keeping your Keys Safe](#section/Getting-Started/Keeping-your-Keys-Safe) for an overview on securely storing your API keys.    <br />  If you are having issues creating API keys you can submit a [Support](#section/API-Overview/Support) request for assistance.  <br />      ## Keeping API Keys Safe    Based on their permissions, API keys could have full access to your account’s Buildium data. It’s important that you only grant access to trusted applications, securely record secrets, and consider a password manager to stay organized.      ### Recommended Practices    - Avoid hard-coding client IDs and secrets inside source files.  - Avoid storing client IDs and secrets in any files that may be committed to source control, particularly cloud-based source control platforms.  - Apply restrictions to client IDs and secrets shared with your staff. You can restrict a key to particular Buildium entities or to read-only access (GET resources only).  - Avoid sharing client IDs and secrets across public, insecure platforms.  - Establish a process to regularly recreate your client IDs and secrets from your Buildium account.    <br />    <br />    ## How to Make a Request    You’ve done a great job setting up your account, Now, we’ll walk you through how to access your data. It’s very straightforward and should only take a few minutes!      > **Tip:** Looking for the right HTTP client? If you’re just getting started, we recommend Postman.      <br />    ### Let's Get Started!    #### Step 1: Get Your API Key    If you haven't yet done so, obtain your API key client ID and secret from your Buildium account. Your API key is how the Buildium API authenticates requests and ensures only you can access your data.    See [Getting Started](#section/Getting-Started) for a deeper dive into enabling the API and creating keys.    #### Step 2: Install a HTTP client  The Buildium API supports any standard HTTP client. If you're looking for a user-friendly HTTP client application, we recommend [Postman](https://www.postman.com/product/api-client) – it allows you to access the Buildium API without writing code. We’ll use Postman for our example below to demonstrate sending an API request.      #### Step 3: Make a Sample Request    Let's dive in and make a simple request to get all the [Rental Properties](#operation/RentalsGetAllGLAccounts) response message now includes the property `IsBankAccount`. This is a boolean property that indicates whether the general ledger account is also a bank account.  * A `Country` property has been added to all Address messages. This property contains an enumeration indicating the country of the address.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.cosigner_message import CosignerMessage
from openapi_client.models.lease_account_detail_message import LeaseAccountDetailMessage
from openapi_client.models.lease_move_out_data_message import LeaseMoveOutDataMessage
from openapi_client.models.lease_tenant_message import LeaseTenantMessage
from typing import Optional, Set
from typing_extensions import Self

class LeaseMessage(BaseModel):
    """
    This object represents a rental property lease.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Lease unique identifier.", alias="Id")
    property_id: Optional[StrictInt] = Field(default=None, description="Rental property unique identifier.", alias="PropertyId")
    unit_id: Optional[StrictInt] = Field(default=None, description="Unit unique identifier.", alias="UnitId")
    unit_number: Optional[StrictStr] = Field(default=None, description="Unit number specified in the lease.", alias="UnitNumber")
    lease_from_date: Optional[date] = Field(default=None, description="Start date of the lease.", alias="LeaseFromDate")
    lease_to_date: Optional[date] = Field(default=None, description="End date of the lease.", alias="LeaseToDate")
    lease_type: Optional[StrictStr] = Field(default=None, description="Describes the type of lease.", alias="LeaseType")
    lease_status: Optional[StrictStr] = Field(default=None, description="Indicates the status of the lease.", alias="LeaseStatus")
    is_eviction_pending: Optional[StrictBool] = Field(default=None, description="Indicates whether the lease has an eviction pending.", alias="IsEvictionPending")
    term_type: Optional[StrictStr] = Field(default=None, description="Describes the term type of the lease.", alias="TermType")
    renewal_offer_status: Optional[StrictStr] = Field(default=None, description="Describes the status of the renewal offer. Null if no renewal offer exists.", alias="RenewalOfferStatus")
    current_tenants: Optional[List[TenantMessage]] = Field(default=None, description="List of the current tenants on the lease.", alias="CurrentTenants")
    current_number_of_occupants: Optional[StrictInt] = Field(default=None, description="Count of current tenants.", alias="CurrentNumberOfOccupants")
    account_details: Optional[LeaseAccountDetailMessage] = Field(default=None, description="Financial details of the lease.", alias="AccountDetails")
    cosigners: Optional[List[CosignerMessage]] = Field(default=None, description="List of the cosigners on the lease.", alias="Cosigners")
    automatically_move_out_tenants: Optional[StrictBool] = Field(default=None, description="Indicates whether to automatically move out all tenants assigned to the lease and set the lease status to past when the lease ends.", alias="AutomaticallyMoveOutTenants")
    created_date_time: Optional[datetime] = Field(default=None, description="Date and time the lease was created.", alias="CreatedDateTime")
    last_updated_date_time: Optional[datetime] = Field(default=None, description="The date and time the lease was last updated.", alias="LastUpdatedDateTime")
    move_out_data: Optional[List[LeaseMoveOutDataMessage]] = Field(default=None, description="Move out data of lease", alias="MoveOutData")
    payment_due_day: Optional[StrictInt] = Field(default=None, description="Day of the month payment is due.", alias="PaymentDueDay")
    tenants: Optional[List[LeaseTenantMessage]] = Field(default=None, description="List of all tenants ever associated with the lease", alias="Tenants")
    __properties: ClassVar[List[str]] = ["Id", "PropertyId", "UnitId", "UnitNumber", "LeaseFromDate", "LeaseToDate", "LeaseType", "LeaseStatus", "IsEvictionPending", "TermType", "RenewalOfferStatus", "CurrentTenants", "CurrentNumberOfOccupants", "AccountDetails", "Cosigners", "AutomaticallyMoveOutTenants", "CreatedDateTime", "LastUpdatedDateTime", "MoveOutData", "PaymentDueDay", "Tenants"]

    @field_validator('lease_type')
    def lease_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['None', 'Fixed', 'FixedWithRollover', 'AtWill']):
            raise ValueError("must be one of enum values ('None', 'Fixed', 'FixedWithRollover', 'AtWill')")
        return value

    @field_validator('lease_status')
    def lease_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Active', 'Past', 'Future']):
            raise ValueError("must be one of enum values ('Active', 'Past', 'Future')")
        return value

    @field_validator('term_type')
    def term_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MonthToMonth', 'Standard', 'Owner']):
            raise ValueError("must be one of enum values ('MonthToMonth', 'Standard', 'Owner')")
        return value

    @field_validator('renewal_offer_status')
    def renewal_offer_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NotSet', 'NotStarted', 'Generated', 'Declined', 'Renewed', 'Draft', 'Unsigned', 'PartiallySigned', 'Countersign', 'Activated', 'Sent', 'Accepted']):
            raise ValueError("must be one of enum values ('NotSet', 'NotStarted', 'Generated', 'Declined', 'Renewed', 'Draft', 'Unsigned', 'PartiallySigned', 'Countersign', 'Activated', 'Sent', 'Accepted')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LeaseMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in current_tenants (list)
        _items = []
        if self.current_tenants:
            for _item_current_tenants in self.current_tenants:
                if _item_current_tenants:
                    _items.append(_item_current_tenants.to_dict())
            _dict['CurrentTenants'] = _items
        # override the default output from pydantic by calling `to_dict()` of account_details
        if self.account_details:
            _dict['AccountDetails'] = self.account_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in cosigners (list)
        _items = []
        if self.cosigners:
            for _item_cosigners in self.cosigners:
                if _item_cosigners:
                    _items.append(_item_cosigners.to_dict())
            _dict['Cosigners'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in move_out_data (list)
        _items = []
        if self.move_out_data:
            for _item_move_out_data in self.move_out_data:
                if _item_move_out_data:
                    _items.append(_item_move_out_data.to_dict())
            _dict['MoveOutData'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tenants (list)
        _items = []
        if self.tenants:
            for _item_tenants in self.tenants:
                if _item_tenants:
                    _items.append(_item_tenants.to_dict())
            _dict['Tenants'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LeaseMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "PropertyId": obj.get("PropertyId"),
            "UnitId": obj.get("UnitId"),
            "UnitNumber": obj.get("UnitNumber"),
            "LeaseFromDate": obj.get("LeaseFromDate"),
            "LeaseToDate": obj.get("LeaseToDate"),
            "LeaseType": obj.get("LeaseType"),
            "LeaseStatus": obj.get("LeaseStatus"),
            "IsEvictionPending": obj.get("IsEvictionPending"),
            "TermType": obj.get("TermType"),
            "RenewalOfferStatus": obj.get("RenewalOfferStatus"),
            "CurrentTenants": [TenantMessage.from_dict(_item) for _item in obj["CurrentTenants"]] if obj.get("CurrentTenants") is not None else None,
            "CurrentNumberOfOccupants": obj.get("CurrentNumberOfOccupants"),
            "AccountDetails": LeaseAccountDetailMessage.from_dict(obj["AccountDetails"]) if obj.get("AccountDetails") is not None else None,
            "Cosigners": [CosignerMessage.from_dict(_item) for _item in obj["Cosigners"]] if obj.get("Cosigners") is not None else None,
            "AutomaticallyMoveOutTenants": obj.get("AutomaticallyMoveOutTenants"),
            "CreatedDateTime": obj.get("CreatedDateTime"),
            "LastUpdatedDateTime": obj.get("LastUpdatedDateTime"),
            "MoveOutData": [LeaseMoveOutDataMessage.from_dict(_item) for _item in obj["MoveOutData"]] if obj.get("MoveOutData") is not None else None,
            "PaymentDueDay": obj.get("PaymentDueDay"),
            "Tenants": [LeaseTenantMessage.from_dict(_item) for _item in obj["Tenants"]] if obj.get("Tenants") is not None else None
        })
        return _obj

from openapi_client.models.tenant_message import TenantMessage
# TODO: Rewrite to not use raise_errors
LeaseMessage.model_rebuild(raise_errors=False)

