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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.file_sharing_account_message import FileSharingAccountMessage
from openapi_client.models.file_sharing_association_message import FileSharingAssociationMessage
from openapi_client.models.file_sharing_association_owner_message import FileSharingAssociationOwnerMessage
from openapi_client.models.file_sharing_association_unit_message import FileSharingAssociationUnitMessage
from openapi_client.models.file_sharing_committee_message import FileSharingCommitteeMessage
from openapi_client.models.file_sharing_lease_message import FileSharingLeaseMessage
from openapi_client.models.file_sharing_ownership_account_message import FileSharingOwnershipAccountMessage
from openapi_client.models.file_sharing_rental_message import FileSharingRentalMessage
from openapi_client.models.file_sharing_rental_owner_message import FileSharingRentalOwnerMessage
from openapi_client.models.file_sharing_rental_unit_mesage import FileSharingRentalUnitMesage
from openapi_client.models.file_sharing_tenant_message import FileSharingTenantMessage
from openapi_client.models.file_sharing_vendor_message import FileSharingVendorMessage
from typing import Optional, Set
from typing_extensions import Self

class FileSharingMessage(BaseModel):
    """
    FileSharingMessage
    """ # noqa: E501
    account: Optional[FileSharingAccountMessage] = Field(default=None, description="Account file sharing settings.", alias="Account")
    rental: Optional[FileSharingRentalMessage] = Field(default=None, description="Rental file sharing settings.", alias="Rental")
    rental_unit: Optional[FileSharingRentalUnitMesage] = Field(default=None, description="Rental unit file sharing settings.", alias="RentalUnit")
    lease: Optional[FileSharingLeaseMessage] = Field(default=None, description="Lease file sharing settings.", alias="Lease")
    tenant: Optional[FileSharingTenantMessage] = Field(default=None, description="Tenant file sharing settings.", alias="Tenant")
    rental_owner: Optional[FileSharingRentalOwnerMessage] = Field(default=None, description="Rental owner file sharing settings.", alias="RentalOwner")
    association: Optional[FileSharingAssociationMessage] = Field(default=None, description="Association file sharing settings.", alias="Association")
    association_unit: Optional[FileSharingAssociationUnitMessage] = Field(default=None, description="Association unit file sharing settings.", alias="AssociationUnit")
    ownership_account: Optional[FileSharingOwnershipAccountMessage] = Field(default=None, description="Ownership account file sharing settings.", alias="OwnershipAccount")
    association_owner: Optional[FileSharingAssociationOwnerMessage] = Field(default=None, description="Association owner file sharing settings.", alias="AssociationOwner")
    vendor: Optional[FileSharingVendorMessage] = Field(default=None, description="Vendor file sharing settings.", alias="Vendor")
    committee: Optional[FileSharingCommitteeMessage] = Field(default=None, description="Committee file sharing settings.", alias="Committee")
    __properties: ClassVar[List[str]] = ["Account", "Rental", "RentalUnit", "Lease", "Tenant", "RentalOwner", "Association", "AssociationUnit", "OwnershipAccount", "AssociationOwner", "Vendor", "Committee"]

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
        """Create an instance of FileSharingMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['Account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rental
        if self.rental:
            _dict['Rental'] = self.rental.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rental_unit
        if self.rental_unit:
            _dict['RentalUnit'] = self.rental_unit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lease
        if self.lease:
            _dict['Lease'] = self.lease.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant
        if self.tenant:
            _dict['Tenant'] = self.tenant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rental_owner
        if self.rental_owner:
            _dict['RentalOwner'] = self.rental_owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of association
        if self.association:
            _dict['Association'] = self.association.to_dict()
        # override the default output from pydantic by calling `to_dict()` of association_unit
        if self.association_unit:
            _dict['AssociationUnit'] = self.association_unit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ownership_account
        if self.ownership_account:
            _dict['OwnershipAccount'] = self.ownership_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of association_owner
        if self.association_owner:
            _dict['AssociationOwner'] = self.association_owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vendor
        if self.vendor:
            _dict['Vendor'] = self.vendor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of committee
        if self.committee:
            _dict['Committee'] = self.committee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileSharingMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Account": FileSharingAccountMessage.from_dict(obj["Account"]) if obj.get("Account") is not None else None,
            "Rental": FileSharingRentalMessage.from_dict(obj["Rental"]) if obj.get("Rental") is not None else None,
            "RentalUnit": FileSharingRentalUnitMesage.from_dict(obj["RentalUnit"]) if obj.get("RentalUnit") is not None else None,
            "Lease": FileSharingLeaseMessage.from_dict(obj["Lease"]) if obj.get("Lease") is not None else None,
            "Tenant": FileSharingTenantMessage.from_dict(obj["Tenant"]) if obj.get("Tenant") is not None else None,
            "RentalOwner": FileSharingRentalOwnerMessage.from_dict(obj["RentalOwner"]) if obj.get("RentalOwner") is not None else None,
            "Association": FileSharingAssociationMessage.from_dict(obj["Association"]) if obj.get("Association") is not None else None,
            "AssociationUnit": FileSharingAssociationUnitMessage.from_dict(obj["AssociationUnit"]) if obj.get("AssociationUnit") is not None else None,
            "OwnershipAccount": FileSharingOwnershipAccountMessage.from_dict(obj["OwnershipAccount"]) if obj.get("OwnershipAccount") is not None else None,
            "AssociationOwner": FileSharingAssociationOwnerMessage.from_dict(obj["AssociationOwner"]) if obj.get("AssociationOwner") is not None else None,
            "Vendor": FileSharingVendorMessage.from_dict(obj["Vendor"]) if obj.get("Vendor") is not None else None,
            "Committee": FileSharingCommitteeMessage.from_dict(obj["Committee"]) if obj.get("Committee") is not None else None
        })
        return _obj


