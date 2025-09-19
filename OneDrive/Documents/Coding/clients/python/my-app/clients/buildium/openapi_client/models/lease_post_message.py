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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.lease_cosigner_post_message import LeaseCosignerPostMessage
from openapi_client.models.lease_rent_post_message import LeaseRentPostMessage
from openapi_client.models.lease_security_deposit_post_message import LeaseSecurityDepositPostMessage
from openapi_client.models.rental_tenant_put_message import RentalTenantPutMessage
from typing import Optional, Set
from typing_extensions import Self

class LeasePostMessage(BaseModel):
    """
    LeasePostMessage
    """ # noqa: E501
    lease_type: StrictStr = Field(description="Describes the type of lease.<br /><br />  `AtWill` leases are month-to-month leases. Setting a lease as at will tells Buildium when the tenant's lease initially started, but since there is no lease end date, Buildium will never move the lease to expired, and it will continue to post any automatic transactions (like recurring monthly rent charges or late fees) until you manually end the lease.  <br /><br />  `Fixed` leases are leases that have specific start and end dates.When the end date occurs, the lease will move from active to expired, and any transactions set to post automatically(like recurring monthly rent charges or late fees) will stop posting.  <br /><br />  `FixedWithRollover` leases are similar to fixed leases, but instead of Buildium moving this lease to expired as of the end date, it will move the lease to an at will status, which tells Buildium to continue posting monthly rent charges, late fees for you until you manually end the lease.", alias="LeaseType")
    unit_id: StrictInt = Field(description="Unit unique identifier associated with the lease.", alias="UnitId")
    lease_from_date: date = Field(description="Start date of the lease.", alias="LeaseFromDate")
    lease_to_date: Optional[date] = Field(default=None, description="End date of the lease.", alias="LeaseToDate")
    send_welcome_email: StrictBool = Field(description="Indicates whether to send a welcome email to all tenants on the lease inviting them to the resident center website.", alias="SendWelcomeEmail")
    tenants: Optional[List[RentalTenantPutMessage]] = Field(default=None, description="List of new tenants to add to the lease. The list cannot exceed five tenants.", alias="Tenants")
    tenant_ids: Optional[List[StrictInt]] = Field(default=None, description="List of identifiers for existing tenants to add to the lease. The list cannot exceed five tenants.", alias="TenantIds")
    applicant_ids: Optional[List[StrictInt]] = Field(default=None, description="List of identifiers for applicants to become tenants on the lease. Identifiers must refer to applicants with a Status of `Approved`. The list cannot exceed five applicants.", alias="ApplicantIds")
    cosigners: Optional[List[LeaseCosignerPostMessage]] = Field(default=None, description="List of the cosigners on the lease.", alias="Cosigners")
    rent: Optional[LeaseRentPostMessage] = Field(default=None, description="Rent charge on the post message", alias="Rent")
    security_deposit: Optional[LeaseSecurityDepositPostMessage] = Field(default=None, description="The security deposit.", alias="SecurityDeposit")
    prorated_first_month_rent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Prorated rent charged for the first month of the lease. Must be null if the lease begins on the first day of a month.", alias="ProratedFirstMonthRent")
    prorated_last_month_rent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Prorated rent charged for the last month of the lease. Must be null if the lease ends on the last day of a month.", alias="ProratedLastMonthRent")
    __properties: ClassVar[List[str]] = ["LeaseType", "UnitId", "LeaseFromDate", "LeaseToDate", "SendWelcomeEmail", "Tenants", "TenantIds", "ApplicantIds", "Cosigners", "Rent", "SecurityDeposit", "ProratedFirstMonthRent", "ProratedLastMonthRent"]

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
        """Create an instance of LeasePostMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tenants (list)
        _items = []
        if self.tenants:
            for _item_tenants in self.tenants:
                if _item_tenants:
                    _items.append(_item_tenants.to_dict())
            _dict['Tenants'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cosigners (list)
        _items = []
        if self.cosigners:
            for _item_cosigners in self.cosigners:
                if _item_cosigners:
                    _items.append(_item_cosigners.to_dict())
            _dict['Cosigners'] = _items
        # override the default output from pydantic by calling `to_dict()` of rent
        if self.rent:
            _dict['Rent'] = self.rent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security_deposit
        if self.security_deposit:
            _dict['SecurityDeposit'] = self.security_deposit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LeasePostMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LeaseType": obj.get("LeaseType"),
            "UnitId": obj.get("UnitId"),
            "LeaseFromDate": obj.get("LeaseFromDate"),
            "LeaseToDate": obj.get("LeaseToDate"),
            "SendWelcomeEmail": obj.get("SendWelcomeEmail"),
            "Tenants": [RentalTenantPutMessage.from_dict(_item) for _item in obj["Tenants"]] if obj.get("Tenants") is not None else None,
            "TenantIds": obj.get("TenantIds"),
            "ApplicantIds": obj.get("ApplicantIds"),
            "Cosigners": [LeaseCosignerPostMessage.from_dict(_item) for _item in obj["Cosigners"]] if obj.get("Cosigners") is not None else None,
            "Rent": LeaseRentPostMessage.from_dict(obj["Rent"]) if obj.get("Rent") is not None else None,
            "SecurityDeposit": LeaseSecurityDepositPostMessage.from_dict(obj["SecurityDeposit"]) if obj.get("SecurityDeposit") is not None else None,
            "ProratedFirstMonthRent": obj.get("ProratedFirstMonthRent"),
            "ProratedLastMonthRent": obj.get("ProratedLastMonthRent")
        })
        return _obj


