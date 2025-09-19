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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.work_order_entry_contact_message import WorkOrderEntryContactMessage
from openapi_client.models.work_order_line_item_message import WorkOrderLineItemMessage
from openapi_client.models.work_order_task_message import WorkOrderTaskMessage
from typing import Optional, Set
from typing_extensions import Self

class WorkOrderMessage(BaseModel):
    """
    WorkOrderMessage
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Work order unique identifier.", alias="Id")
    task: Optional[WorkOrderTaskMessage] = Field(default=None, description="Task information related to the work order.", alias="Task")
    title: Optional[StrictStr] = Field(default=None, description="Work order title.", alias="Title")
    due_date: Optional[date] = Field(default=None, description="Work order due date.", alias="DueDate")
    priority: Optional[StrictStr] = Field(default=None, description="Work order  priority.", alias="Priority")
    status: Optional[StrictStr] = Field(default=None, description="Work order status.", alias="Status")
    work_details: Optional[StrictStr] = Field(default=None, description="Description of the work order.", alias="WorkDetails")
    invoice_number: Optional[StrictStr] = Field(default=None, description="The invoice or reference number that the vendor assigned to the invoice.", alias="InvoiceNumber")
    chargeable_to: Optional[StrictStr] = Field(default=None, description="A description of the entity that will be charged for the work.", alias="ChargeableTo")
    entry_allowed: Optional[StrictStr] = Field(default=None, description="Indicates whether entry has been allowed to the unit.", alias="EntryAllowed")
    entry_notes: Optional[StrictStr] = Field(default=None, description="Notes specific to entering the unit.", alias="EntryNotes")
    vendor_id: Optional[StrictInt] = Field(default=None, description="Vendor unique identifier.", alias="VendorId")
    vendor_notes: Optional[StrictStr] = Field(default=None, description="Notes specific to the vendor.", alias="VendorNotes")
    entry_contact: Optional[WorkOrderEntryContactMessage] = Field(default=None, description="Entry contact for the work order", alias="EntryContact")
    entry_contacts: Optional[List[WorkOrderEntryContactMessage]] = Field(default=None, description="A collection of all entry contacts for the work order", alias="EntryContacts")
    bill_transaction_id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the bill related to this work order. This field will be `null` if no bill is related to this work order.  If the BillTransactionIds field is available, please refer to that field instead of this one going forward.", alias="BillTransactionId")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount of the work order.", alias="Amount")
    line_items: Optional[List[WorkOrderLineItemMessage]] = Field(default=None, description="A collection of line items associated with the work order.", alias="LineItems")
    __properties: ClassVar[List[str]] = ["Id", "Task", "Title", "DueDate", "Priority", "Status", "WorkDetails", "InvoiceNumber", "ChargeableTo", "EntryAllowed", "EntryNotes", "VendorId", "VendorNotes", "EntryContact", "EntryContacts", "BillTransactionId", "Amount", "LineItems"]

    @field_validator('priority')
    def priority_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Unknown', 'Low', 'Normal', 'High']):
            raise ValueError("must be one of enum values ('Unknown', 'Low', 'Normal', 'High')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Unknown', 'New', 'InProgress', 'Completed', 'Deferred', 'Closed']):
            raise ValueError("must be one of enum values ('Unknown', 'New', 'InProgress', 'Completed', 'Deferred', 'Closed')")
        return value

    @field_validator('entry_allowed')
    def entry_allowed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Unknown', 'Yes', 'No']):
            raise ValueError("must be one of enum values ('Unknown', 'Yes', 'No')")
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
        """Create an instance of WorkOrderMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of task
        if self.task:
            _dict['Task'] = self.task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entry_contact
        if self.entry_contact:
            _dict['EntryContact'] = self.entry_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entry_contacts (list)
        _items = []
        if self.entry_contacts:
            for _item_entry_contacts in self.entry_contacts:
                if _item_entry_contacts:
                    _items.append(_item_entry_contacts.to_dict())
            _dict['EntryContacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['LineItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkOrderMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "Task": WorkOrderTaskMessage.from_dict(obj["Task"]) if obj.get("Task") is not None else None,
            "Title": obj.get("Title"),
            "DueDate": obj.get("DueDate"),
            "Priority": obj.get("Priority"),
            "Status": obj.get("Status"),
            "WorkDetails": obj.get("WorkDetails"),
            "InvoiceNumber": obj.get("InvoiceNumber"),
            "ChargeableTo": obj.get("ChargeableTo"),
            "EntryAllowed": obj.get("EntryAllowed"),
            "EntryNotes": obj.get("EntryNotes"),
            "VendorId": obj.get("VendorId"),
            "VendorNotes": obj.get("VendorNotes"),
            "EntryContact": WorkOrderEntryContactMessage.from_dict(obj["EntryContact"]) if obj.get("EntryContact") is not None else None,
            "EntryContacts": [WorkOrderEntryContactMessage.from_dict(_item) for _item in obj["EntryContacts"]] if obj.get("EntryContacts") is not None else None,
            "BillTransactionId": obj.get("BillTransactionId"),
            "Amount": obj.get("Amount"),
            "LineItems": [WorkOrderLineItemMessage.from_dict(_item) for _item in obj["LineItems"]] if obj.get("LineItems") is not None else None
        })
        return _obj


