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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.charge_recurring_transaction_post_message import ChargeRecurringTransactionPostMessage
from openapi_client.models.charge_recurring_transaction_put_message import ChargeRecurringTransactionPutMessage
from openapi_client.models.lease_cosigner_post_message import LeaseCosignerPostMessage
from openapi_client.models.lease_rent_post_message import LeaseRentPostMessage
from openapi_client.models.rental_tenant_renewal_post_message import RentalTenantRenewalPostMessage
from typing import Optional, Set
from typing_extensions import Self

class LeaseRenewalPostMessage(BaseModel):
    """
    LeaseRenewalPostMessage
    """ # noqa: E501
    lease_type: StrictStr = Field(description="Describes the type of lease.", alias="LeaseType")
    lease_to_date: Optional[date] = Field(default=None, description="End date of the lease. This is required if `LeaseType` is `Fixed` or `FixedWithRollover`", alias="LeaseToDate")
    automatically_move_out_tenants: Optional[StrictBool] = Field(default=None, description="Indicates whether to automatically move out all tenants assigned to the lease and set the lease status to past when the lease ends.", alias="AutomaticallyMoveOutTenants")
    rent: LeaseRentPostMessage = Field(description="The rent for the lease.", alias="Rent")
    cosigners: Optional[List[LeaseCosignerPostMessage]] = Field(default=None, description="List of the cosigners to create on the lease.", alias="Cosigners")
    tenant_ids: Optional[List[StrictInt]] = Field(default=None, description="Unique identifiers of existing tenants to include on the lease. The request must include at least one tenant in this property OR the `Tenants` property.", alias="TenantIds")
    tenants: Optional[List[RentalTenantRenewalPostMessage]] = Field(default=None, description="List of new tenants to create on the lease. The request must include at least one tenant in this property OR the `TenantIds` property.", alias="Tenants")
    send_welcome_email: StrictBool = Field(description="Indicates whether to send a welcome email to all tenants on the lease inviting them to the resident center website.", alias="SendWelcomeEmail")
    recurring_charges_to_stop: Optional[List[StrictInt]] = Field(default=None, description="Unique identifiers of existing recurring charges on the lease to stop.", alias="RecurringChargesToStop")
    recurring_charges_to_create: Optional[List[ChargeRecurringTransactionPostMessage]] = Field(default=None, description="List of new recurring charges to create.", alias="RecurringChargesToCreate")
    recurring_charges_to_update: Optional[List[ChargeRecurringTransactionPutMessage]] = Field(default=None, description="List of existing recurring charges to update.", alias="RecurringChargesToUpdate")
    __properties: ClassVar[List[str]] = ["LeaseType", "LeaseToDate", "AutomaticallyMoveOutTenants", "Rent", "Cosigners", "TenantIds", "Tenants", "SendWelcomeEmail", "RecurringChargesToStop", "RecurringChargesToCreate", "RecurringChargesToUpdate"]

    @field_validator('lease_type')
    def lease_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Fixed', 'FixedWithRollover', 'AtWill']):
            raise ValueError("must be one of enum values ('Fixed', 'FixedWithRollover', 'AtWill')")
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
        """Create an instance of LeaseRenewalPostMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rent
        if self.rent:
            _dict['Rent'] = self.rent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in cosigners (list)
        _items = []
        if self.cosigners:
            for _item_cosigners in self.cosigners:
                if _item_cosigners:
                    _items.append(_item_cosigners.to_dict())
            _dict['Cosigners'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tenants (list)
        _items = []
        if self.tenants:
            for _item_tenants in self.tenants:
                if _item_tenants:
                    _items.append(_item_tenants.to_dict())
            _dict['Tenants'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recurring_charges_to_create (list)
        _items = []
        if self.recurring_charges_to_create:
            for _item_recurring_charges_to_create in self.recurring_charges_to_create:
                if _item_recurring_charges_to_create:
                    _items.append(_item_recurring_charges_to_create.to_dict())
            _dict['RecurringChargesToCreate'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recurring_charges_to_update (list)
        _items = []
        if self.recurring_charges_to_update:
            for _item_recurring_charges_to_update in self.recurring_charges_to_update:
                if _item_recurring_charges_to_update:
                    _items.append(_item_recurring_charges_to_update.to_dict())
            _dict['RecurringChargesToUpdate'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LeaseRenewalPostMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LeaseType": obj.get("LeaseType"),
            "LeaseToDate": obj.get("LeaseToDate"),
            "AutomaticallyMoveOutTenants": obj.get("AutomaticallyMoveOutTenants"),
            "Rent": LeaseRentPostMessage.from_dict(obj["Rent"]) if obj.get("Rent") is not None else None,
            "Cosigners": [LeaseCosignerPostMessage.from_dict(_item) for _item in obj["Cosigners"]] if obj.get("Cosigners") is not None else None,
            "TenantIds": obj.get("TenantIds"),
            "Tenants": [RentalTenantRenewalPostMessage.from_dict(_item) for _item in obj["Tenants"]] if obj.get("Tenants") is not None else None,
            "SendWelcomeEmail": obj.get("SendWelcomeEmail"),
            "RecurringChargesToStop": obj.get("RecurringChargesToStop"),
            "RecurringChargesToCreate": [ChargeRecurringTransactionPostMessage.from_dict(_item) for _item in obj["RecurringChargesToCreate"]] if obj.get("RecurringChargesToCreate") is not None else None,
            "RecurringChargesToUpdate": [ChargeRecurringTransactionPutMessage.from_dict(_item) for _item in obj["RecurringChargesToUpdate"]] if obj.get("RecurringChargesToUpdate") is not None else None
        })
        return _obj


