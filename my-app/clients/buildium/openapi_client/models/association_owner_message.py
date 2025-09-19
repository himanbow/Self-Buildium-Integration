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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.address_message import AddressMessage
from openapi_client.models.association_owner_board_term_message import AssociationOwnerBoardTermMessage
from openapi_client.models.association_ownership_account_message import AssociationOwnershipAccountMessage
from openapi_client.models.emergency_contact_message import EmergencyContactMessage
from openapi_client.models.phone_number_message import PhoneNumberMessage
from openapi_client.models.vehicle_message import VehicleMessage
from typing import Optional, Set
from typing_extensions import Self

class AssociationOwnerMessage(BaseModel):
    """
    This object represents an owner of a unit(s) that exists within a home owner association.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier.", alias="Id")
    first_name: Optional[StrictStr] = Field(default=None, description="First name.", alias="FirstName")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name.", alias="LastName")
    email: Optional[StrictStr] = Field(default=None, description="Email.", alias="Email")
    alternate_email: Optional[StrictStr] = Field(default=None, description="Alternate email.", alias="AlternateEmail")
    phone_numbers: Optional[List[PhoneNumberMessage]] = Field(default=None, description="List of phone numbers of the association user.", alias="PhoneNumbers")
    primary_address: Optional[AddressMessage] = Field(default=None, description="Primary address.", alias="PrimaryAddress")
    alternate_address: Optional[AddressMessage] = Field(default=None, description="Alternate address.", alias="AlternateAddress")
    comment: Optional[StrictStr] = Field(default=None, description="General comments.", alias="Comment")
    emergency_contact: Optional[EmergencyContactMessage] = Field(default=None, description="Emergency contact information.", alias="EmergencyContact")
    ownership_accounts: Optional[List[AssociationOwnershipAccountMessage]] = Field(default=None, description="List of associated ownership accounts.", alias="OwnershipAccounts")
    mailing_preference: Optional[StrictStr] = Field(default=None, description="Indicates the association owner's mailing preference.", alias="MailingPreference")
    vehicles: Optional[List[VehicleMessage]] = Field(default=None, description="List of vehicles associated with the association owner.", alias="Vehicles")
    occupies_unit: Optional[StrictBool] = Field(default=None, description="Indicates if the association owner occupies a unit(s) within the association.", alias="OccupiesUnit")
    board_member_terms: Optional[List[AssociationOwnerBoardTermMessage]] = Field(default=None, description="List of Board Member Terms for the given Association Owner(s)", alias="BoardMemberTerms")
    created_date_time: Optional[datetime] = Field(default=None, description="Date and time the association owner was created.", alias="CreatedDateTime")
    tax_id: Optional[StrictStr] = Field(default=None, description="Taxpayer identification number. Examples of United States identification numbers are Social Security number or a Employer Identification Number.", alias="TaxId")
    delinquency_status: Optional[StrictStr] = Field(default=None, description="Indicates the delinquency status of the association owner.", alias="DelinquencyStatus")
    __properties: ClassVar[List[str]] = ["Id", "FirstName", "LastName", "Email", "AlternateEmail", "PhoneNumbers", "PrimaryAddress", "AlternateAddress", "Comment", "EmergencyContact", "OwnershipAccounts", "MailingPreference", "Vehicles", "OccupiesUnit", "BoardMemberTerms", "CreatedDateTime", "TaxId", "DelinquencyStatus"]

    @field_validator('mailing_preference')
    def mailing_preference_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PrimaryAddress', 'AlternateAddress']):
            raise ValueError("must be one of enum values ('PrimaryAddress', 'AlternateAddress')")
        return value

    @field_validator('delinquency_status')
    def delinquency_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NoDelinquency', 'InCollections', 'InForeclosure', 'Foreclosed']):
            raise ValueError("must be one of enum values ('NoDelinquency', 'InCollections', 'InForeclosure', 'Foreclosed')")
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
        """Create an instance of AssociationOwnerMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in phone_numbers (list)
        _items = []
        if self.phone_numbers:
            for _item_phone_numbers in self.phone_numbers:
                if _item_phone_numbers:
                    _items.append(_item_phone_numbers.to_dict())
            _dict['PhoneNumbers'] = _items
        # override the default output from pydantic by calling `to_dict()` of primary_address
        if self.primary_address:
            _dict['PrimaryAddress'] = self.primary_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of alternate_address
        if self.alternate_address:
            _dict['AlternateAddress'] = self.alternate_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of emergency_contact
        if self.emergency_contact:
            _dict['EmergencyContact'] = self.emergency_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ownership_accounts (list)
        _items = []
        if self.ownership_accounts:
            for _item_ownership_accounts in self.ownership_accounts:
                if _item_ownership_accounts:
                    _items.append(_item_ownership_accounts.to_dict())
            _dict['OwnershipAccounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vehicles (list)
        _items = []
        if self.vehicles:
            for _item_vehicles in self.vehicles:
                if _item_vehicles:
                    _items.append(_item_vehicles.to_dict())
            _dict['Vehicles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in board_member_terms (list)
        _items = []
        if self.board_member_terms:
            for _item_board_member_terms in self.board_member_terms:
                if _item_board_member_terms:
                    _items.append(_item_board_member_terms.to_dict())
            _dict['BoardMemberTerms'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssociationOwnerMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "FirstName": obj.get("FirstName"),
            "LastName": obj.get("LastName"),
            "Email": obj.get("Email"),
            "AlternateEmail": obj.get("AlternateEmail"),
            "PhoneNumbers": [PhoneNumberMessage.from_dict(_item) for _item in obj["PhoneNumbers"]] if obj.get("PhoneNumbers") is not None else None,
            "PrimaryAddress": AddressMessage.from_dict(obj["PrimaryAddress"]) if obj.get("PrimaryAddress") is not None else None,
            "AlternateAddress": AddressMessage.from_dict(obj["AlternateAddress"]) if obj.get("AlternateAddress") is not None else None,
            "Comment": obj.get("Comment"),
            "EmergencyContact": EmergencyContactMessage.from_dict(obj["EmergencyContact"]) if obj.get("EmergencyContact") is not None else None,
            "OwnershipAccounts": [AssociationOwnershipAccountMessage.from_dict(_item) for _item in obj["OwnershipAccounts"]] if obj.get("OwnershipAccounts") is not None else None,
            "MailingPreference": obj.get("MailingPreference"),
            "Vehicles": [VehicleMessage.from_dict(_item) for _item in obj["Vehicles"]] if obj.get("Vehicles") is not None else None,
            "OccupiesUnit": obj.get("OccupiesUnit"),
            "BoardMemberTerms": [AssociationOwnerBoardTermMessage.from_dict(_item) for _item in obj["BoardMemberTerms"]] if obj.get("BoardMemberTerms") is not None else None,
            "CreatedDateTime": obj.get("CreatedDateTime"),
            "TaxId": obj.get("TaxId"),
            "DelinquencyStatus": obj.get("DelinquencyStatus")
        })
        return _obj


