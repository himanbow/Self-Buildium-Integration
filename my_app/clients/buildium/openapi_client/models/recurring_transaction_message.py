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
from openapi_client.models.recurring_transaction_line_message import RecurringTransactionLineMessage
from typing import Optional, Set
from typing_extensions import Self

class RecurringTransactionMessage(BaseModel):
    """
    RecurringTransactionMessage
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The unique identifier for the recurring transaction schedule.", alias="Id")
    transaction_type: Optional[StrictStr] = Field(default=None, description="Indicates the type of transaction to be applied to the ledger.", alias="TransactionType")
    is_expired: Optional[StrictBool] = Field(default=None, description="Indicates if the recurring transaction schedule has expired.", alias="IsExpired")
    rent_id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the scheduled Rent entity. This field is only applicable for `Charge` transaction types.", alias="RentId")
    offsetting_gl_account_id: Optional[StrictInt] = Field(default=None, description="Offsetting general ledger account identifier. The offsetting general ledger account acts as the expense account. Note, this field is only applicable for `Credit` transaction types.", alias="OffsettingGLAccountId")
    lines: Optional[List[RecurringTransactionLineMessage]] = Field(default=None, description="Line items describing how the transaction is to be allocated when it is processed.", alias="Lines")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total amount of the recurring transaction.", alias="Amount")
    memo: Optional[StrictStr] = Field(default=None, description="Memo associated with the recurring transaction.", alias="Memo")
    first_occurrence_date: Optional[date] = Field(default=None, description="The date the first occurrence of this transaction was processed.", alias="FirstOccurrenceDate")
    next_occurrence_date: Optional[date] = Field(default=None, description="The next date the scheduled transaction will be processed.", alias="NextOccurrenceDate")
    post_days_in_advance: Optional[StrictInt] = Field(default=None, description="The number of days ahead of the transaction date the transaction will post on the lease ledger. This setting is used to add the transaction to the ledger ahead of it's due date for visibility. For example, if the `FirstOccurrenceDate` is set to 8/10/2022 and this value is set to 5 then the charge will added to the ledger on 8/5/2022, but will have transaction date of 8/10/2022.", alias="PostDaysInAdvance")
    frequency: Optional[StrictStr] = Field(default=None, description="Indicates the frequency at which the recurring transaction is processed.", alias="Frequency")
    duration: Optional[StrictStr] = Field(default=None, description="Specifies the period of time/occurrences the recurring transaction will be processed. Note, if the `Frequency` field is set to `OneTime` this field should be set to `NULL` as any submitted value will be ignored.", alias="Duration")
    __properties: ClassVar[List[str]] = ["Id", "TransactionType", "IsExpired", "RentId", "OffsettingGLAccountId", "Lines", "Amount", "Memo", "FirstOccurrenceDate", "NextOccurrenceDate", "PostDaysInAdvance", "Frequency", "Duration"]

    @field_validator('transaction_type')
    def transaction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Bill', 'Check', 'Charge', 'Payment', 'Credit', 'Refund', 'ApplyDeposit', 'ElectronicFundsTransfer', 'Other', 'Deposit', 'GeneralJournalEntry', 'OwnerContribution', 'ReversePayment', 'ReverseElectronicFundsTransfer', 'VendorCredit', 'RentalApplicationFeePayment', 'ReverseRentalApplicationFeePayment', 'ReverseOwnerContribution', 'VendorRefund', 'UnreversedPayment', 'UnreversedElectronicFundsTransfer', 'UnreversedOwnerContribution', 'UnreversedRentalApplicationFeePayment']):
            raise ValueError("must be one of enum values ('Bill', 'Check', 'Charge', 'Payment', 'Credit', 'Refund', 'ApplyDeposit', 'ElectronicFundsTransfer', 'Other', 'Deposit', 'GeneralJournalEntry', 'OwnerContribution', 'ReversePayment', 'ReverseElectronicFundsTransfer', 'VendorCredit', 'RentalApplicationFeePayment', 'ReverseRentalApplicationFeePayment', 'ReverseOwnerContribution', 'VendorRefund', 'UnreversedPayment', 'UnreversedElectronicFundsTransfer', 'UnreversedOwnerContribution', 'UnreversedRentalApplicationFeePayment')")
        return value

    @field_validator('frequency')
    def frequency_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Monthly', 'Weekly', 'Every2Weeks', 'Quarterly', 'Yearly', 'Every2Months', 'Daily', 'Every6Months', 'OneTime']):
            raise ValueError("must be one of enum values ('Monthly', 'Weekly', 'Every2Weeks', 'Quarterly', 'Yearly', 'Every2Months', 'Daily', 'Every6Months', 'OneTime')")
        return value

    @field_validator('duration')
    def duration_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Unspecified', 'UntilEndOfTerm', 'SpecificNumber', 'SpecificDate']):
            raise ValueError("must be one of enum values ('Unspecified', 'UntilEndOfTerm', 'SpecificNumber', 'SpecificDate')")
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
        """Create an instance of RecurringTransactionMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item_lines in self.lines:
                if _item_lines:
                    _items.append(_item_lines.to_dict())
            _dict['Lines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecurringTransactionMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "TransactionType": obj.get("TransactionType"),
            "IsExpired": obj.get("IsExpired"),
            "RentId": obj.get("RentId"),
            "OffsettingGLAccountId": obj.get("OffsettingGLAccountId"),
            "Lines": [RecurringTransactionLineMessage.from_dict(_item) for _item in obj["Lines"]] if obj.get("Lines") is not None else None,
            "Amount": obj.get("Amount"),
            "Memo": obj.get("Memo"),
            "FirstOccurrenceDate": obj.get("FirstOccurrenceDate"),
            "NextOccurrenceDate": obj.get("NextOccurrenceDate"),
            "PostDaysInAdvance": obj.get("PostDaysInAdvance"),
            "Frequency": obj.get("Frequency"),
            "Duration": obj.get("Duration")
        })
        return _obj


