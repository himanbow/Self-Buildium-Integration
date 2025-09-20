# coding: utf-8

# flake8: noqa

"""
    Open API, powered by Buildium

      # Introduction  ### Welcome!    Welcome to Buildium’s API—a powerful, RESTful programming interface that lets you leverage valuable Buildium data.    Using HTTP requests, you can create integrations with applications that specialize in accounting, lead tracking, and more. Enjoy greater flexibility, transparency, and control over your business!      ### What's in this Guide?    This guide is full of simple, easy-to-follow instructions that’ll help you use Buildium’s API like a pro.    Topics include:    * choosing the right resources for your use case  * making HTTP requests to any resource  * understanding data and response codes    <br />    # Getting Started  Excited to get going? We’ll walk you through the setup process.  >  **Note:** To take advantage of the Buildium Open API you must have a <a target=\"_blank\" href=\"https://www.buildium.com/pricing/\">**Premium Subscription**</a>.    ## Account Configuration  Before you can use Buildium’s API, you’ll need to make some tweaks to your account settings.    <br />    ### Enabling the API  In order to start creating your keys and making requests, you’ll need to enable the API.      >  **Tip:** You’ll need an administrator user role with access to ***Application settings*** to set things up properly.    <br />    ​ **Let's Begin!**    1. Sign in to your [Buildium](https://signin.managebuilding.com/manager/public/authentication/login?ReturnUrl=%2Fmanager%2F) account from your browser.    2. Open the ***Settings*** menu and click ***Application settings***.    3. Under ***System preferences***, click ***Api settings***. A modal will appear.    4. Click the ***Open API*** toggle to turn it on. Then click ***Save***.    <video width=\"100%\" autoplay loop muted>    <source src=\"enable_open_api.mp4\" type=\"video/mp4\" />  </video>      Congratulations! Your account's enabled. Now, you’re ready to start managing API keys.  <br />  <br />  If you are having issues enabling the API within your account you can submit a [Support](#section/API-Overview/Support) request for assistance.    <br />      ## API Keys  Account-level API keys authenticate every request and keep things secure.    API keys have two components: a “client ID” and a “secret”.    * **Client IDs** are similar to usernames. They’re used to identify your Buildium account and are safe to share.  * **Secrets** are similar to passwords. They must be kept confidential.    Whenever you make a request, you’ll need the API key’s client ID and secret. If you forget it, make a mistake, or try to use information that’s linked to a deleted key, the API will return a `401` response code.    >  **Tip:** We compiled a list of best practices that detail how securely store API keys. [Give it a read](#section/Getting-Started/Keeping-API-Keys-Safe)!    ## Creating API Keys  Now that the Open APi is enabled, you’ll be able to create API keys. You’re almost there!    >  **Tip:** You’ll need an administrator user role to complete this step, too.    <br />    **How to create an API key**    1. Sign in to your [Buildium](https://signin.managebuilding.com/manager/public/authentication/login?ReturnUrl=%2Fmanager%2F) account from your browser.    2. Open the ***Settings*** menu and click ***Developer Tools***. The page will open automatically.    3. Click the ***Create API Key*** button. A modal will appear.    4. Enter a clear, memorable name and description for your API key. It’ll make it easier to locate the right key when you make a request. Once finished, click **Next**.    5. Now, choose which pieces of Buildium data you want this API key to have access to by marking the corresponding checkboxes. Once finished, click **Next**.    6. You successfully created an API key!    > **Important:** This is your only chance to record the secret. Make sure it’s stored somewhere secure! If it’s forgotten, you’ll need to delete this key and start from scratch.    <br />    <video width=\"100%\" autoplay loop muted>    <source src=\"generate_open_api_key.mp4\" type=\"video/mp4\" />  </video>    <br />    You have now successfully created an API key and have everything you need to  send requests to the Buildium API!    Before moving on to [making your first request](#section/Getting-Started/How-to-Make-a-Request) please review [Keeping your Keys Safe](#section/Getting-Started/Keeping-your-Keys-Safe) for an overview on securely storing your API keys.    <br />  If you are having issues creating API keys you can submit a [Support](#section/API-Overview/Support) request for assistance.  <br />      ## Keeping API Keys Safe    Based on their permissions, API keys could have full access to your account’s Buildium data. It’s important that you only grant access to trusted applications, securely record secrets, and consider a password manager to stay organized.      ### Recommended Practices    - Avoid hard-coding client IDs and secrets inside source files.  - Avoid storing client IDs and secrets in any files that may be committed to source control, particularly cloud-based source control platforms.  - Apply restrictions to client IDs and secrets shared with your staff. You can restrict a key to particular Buildium entities or to read-only access (GET resources only).  - Avoid sharing client IDs and secrets across public, insecure platforms.  - Establish a process to regularly recreate your client IDs and secrets from your Buildium account.    <br />    <br />    ## How to Make a Request    You’ve done a great job setting up your account, Now, we’ll walk you through how to access your data. It’s very straightforward and should only take a few minutes!      > **Tip:** Looking for the right HTTP client? If you’re just getting started, we recommend Postman.      <br />    ### Let's Get Started!    #### Step 1: Get Your API Key    If you haven't yet done so, obtain your API key client ID and secret from your Buildium account. Your API key is how the Buildium API authenticates requests and ensures only you can access your data.    See [Getting Started](#section/Getting-Started) for a deeper dive into enabling the API and creating keys.    #### Step 2: Install a HTTP client  The Buildium API supports any standard HTTP client. If you're looking for a user-friendly HTTP client application, we recommend [Postman](https://www.postman.com/product/api-client) – it allows you to access the Buildium API without writing code. We’ll use Postman for our example below to demonstrate sending an API request.      #### Step 3: Make a Sample Request    Let's dive in and make a simple request to get all the [Rental Properties](#operation/RentalsGetAllGLAccounts) response message now includes the property `IsBankAccount`. This is a boolean property that indicates whether the general ledger account is also a bank account.  * A `Country` property has been added to all Address messages. This property contains an enumeration indicating the country of the address.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "AdministrationApi",
    "AppliancesApi",
    "ApplicantsApi",
    "ArchitecturalRequestsApi",
    "AssociationMeterReadingsApi",
    "AssociationOwnersApi",
    "AssociationTenantsApi",
    "AssociationUnitsApi",
    "AssociationsApi",
    "BankAccountsApi",
    "BillsApi",
    "BoardMembersApi",
    "BudgetsApi",
    "ClientLeadsApi",
    "CommunicationsApi",
    "ContactRequestsApi",
    "FilesApi",
    "GeneralLedgerApi",
    "LeaseTransactionsApi",
    "LeasesApi",
    "ListingsApi",
    "OwnershipAccountTransactionsApi",
    "OwnershipAccountsApi",
    "PropertyGroupsApi",
    "RentalAppliancesApi",
    "RentalMeterReadingsApi",
    "RentalOwnerRequestsApi",
    "RentalOwnersApi",
    "RentalPropertiesApi",
    "RentalTenantsApi",
    "RentalUnitsApi",
    "ResidentCenterApi",
    "ResidentRequestsApi",
    "TasksApi",
    "ToDoRequestsApi",
    "VendorsApi",
    "WorkOrdersApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "AccountInfoMessage",
    "AccountingEntityMessage",
    "AccountingEntityPatchMessage",
    "AccountingEntitySaveMessage",
    "AccountingLockPeriodMessage",
    "AccountingSettingsMessage",
    "AddressMessage",
    "AllTasksMessage",
    "AnnouncementMessage",
    "AnnouncementPostMessage",
    "AnnouncementSenderMessage",
    "ApiError",
    "ApiErrorResponse",
    "ApplianceMessage",
    "ApplicantApplicationMessage",
    "ApplicantGroupMessage",
    "ApplicantGroupPostMessage",
    "ApplicantGroupPutMessage",
    "ApplicantMessage",
    "ApplicantPostMessage",
    "ApplicantPutMessage",
    "ApplicationMessage",
    "ApplicationPutMessage",
    "ApplicationResponseFieldMessage",
    "ApplicationResponseMessage",
    "ApplicationSectionResponseMessage",
    "AppliedVendorCreditMessage",
    "ArchitecturalRequestsPostMessage",
    "AssociationApplianceMessage",
    "AssociationAppliancePostMessage",
    "AssociationAppliancePutMessage",
    "AssociationApplianceServiceHistoryMessage",
    "AssociationApplianceServiceHistoryPostMessage",
    "AssociationArchitecturalRequestFileMessage",
    "AssociationArchitecturalRequestMessage",
    "AssociationBoardMemberMessage",
    "AssociationBoardMemberPostMessage",
    "AssociationBoardMemberPutMessage",
    "AssociationMessage",
    "AssociationOwnerBoardTermMessage",
    "AssociationOwnerBoardTermPostMessage",
    "AssociationOwnerMessage",
    "AssociationOwnerPostMessage",
    "AssociationOwnerPutMessage",
    "AssociationOwnerToExistingOwnershipAccountPostMessage",
    "AssociationOwnerUnitOccupancyPutMessage",
    "AssociationOwnerUnitOccupancyStatusMessage",
    "AssociationOwnershipAccountMessage",
    "AssociationOwnershipAccountPostMessage",
    "AssociationOwnershipAccountPutMessage",
    "AssociationPostMessage",
    "AssociationPreferredVendorMessage",
    "AssociationPreferredVendorPutMessage",
    "AssociationPutMessage",
    "AssociationTaxInformationMessage",
    "AssociationTenantMessage",
    "AssociationTenantPostMessage",
    "AssociationTenantPutMessage",
    "AssociationUnitMessage",
    "AssociationUnitPutMessage",
    "AssociationUnitsPostMessage",
    "BankAccountCheckAccountingEntitySaveMessage",
    "BankAccountCheckFileMessage",
    "BankAccountCheckLineMessage",
    "BankAccountCheckLineSaveMessage",
    "BankAccountCheckMessage",
    "BankAccountCheckPayeeMessage",
    "BankAccountCheckPayeeSaveMessage",
    "BankAccountCheckPostMessage",
    "BankAccountCheckPutMessage",
    "BankAccountDepositLineMessage",
    "BankAccountDepositLineSaveMessage",
    "BankAccountDepositMessage",
    "BankAccountDepositPostMessage",
    "BankAccountDepositPutMessage",
    "BankAccountMessage",
    "BankAccountPostMessage",
    "BankAccountPutMessage",
    "BankAccountQuickDepositMessage",
    "BankAccountQuickDepositSaveMessage",
    "BankAccountReconciliationBalanceMessage",
    "BankAccountReconciliationBalancePutMessage",
    "BankAccountReconciliationMessage",
    "BankAccountReconciliationTransactionMessage",
    "BankAccountTransactionMessage",
    "BankAccountTransferAccountingEntitySaveMessage",
    "BankAccountTransferMessage",
    "BankAccountTransferSaveMessage",
    "BankAccountWithdrawalMessage",
    "BankAccountWithdrawalSaveMessage",
    "BankLockboxDataAssociationMessage",
    "BankLockboxDataAssociationOwnerMessage",
    "BankLockboxDataMessage",
    "BankLockboxDataOwnershipAccountMessage",
    "BankPendingReconciliationPostMessage",
    "BankReconciliationClearTransactionsPostMessage",
    "BankReconciliationClearedBalanceMessage",
    "BankReconciliationPutMessage",
    "BankReconciliationStatementBalanceMessage",
    "BankReconciliationUnclearTransactionsPostMessage",
    "BillFileMessage",
    "BillLineItemPatchMessage",
    "BillLineMessage",
    "BillLinePostMessage",
    "BillLinePutMessage",
    "BillMarkupMessage",
    "BillMarkupPatchMessage",
    "BillMarkupSaveMessage",
    "BillMessage",
    "BillPatchMessage",
    "BillPaymentAccountingEntityMessage",
    "BillPaymentLineMessage",
    "BillPaymentLinePostMessage",
    "BillPaymentMessage",
    "BillPaymentPostMessage",
    "BillPostMessage",
    "BillPutMessage",
    "BudgetDetailsMessage",
    "BudgetDetailsSaveMessage",
    "BudgetMessage",
    "BudgetMonthlyAmountsMessage",
    "BudgetMonthlyAmountsSaveMessage",
    "BudgetPostMessage",
    "BudgetPutMessage",
    "CCPaymentsMessage",
    "CCPaymentsPutMessage",
    "ChargeRecurringTransactionPostMessage",
    "ChargeRecurringTransactionPutMessage",
    "CheckPrintingInfoMessage",
    "CheckPrintingInfoPostMessage",
    "CheckPrintingInfoPutMessage",
    "ClientLeadCreditRequestMessage",
    "ClientLeadMessage",
    "ContactDetailMessage",
    "ContactDetailPhoneMessage",
    "ContactDetailSaveMessage",
    "ContactDetailSavePhoneMessage",
    "ContactInfoMessage",
    "ContactRequestTaskMessage",
    "ContactRequestTaskPostMessage",
    "ContactRequestTaskPutMessage",
    "CosignerMessage",
    "CreatedByUserMessage",
    "CreditRecurringTransactionPostMessage",
    "DepositDetailMessage",
    "EFTPaymentsMessage",
    "EFTPaymentsPutMessage",
    "EPaySettingsMessage",
    "EPaySettingsPutMessage",
    "ElectronicPaymentsMessage",
    "EmailMessage",
    "EmailPostMessage",
    "EmailRecipientMessage",
    "EmailSenderMessage",
    "EmergencyContactMessage",
    "FileCategoryMessage",
    "FileCategoryPostMessage",
    "FileCategoryPutMessage",
    "FileDownloadMessage",
    "FileEntityMessage",
    "FileMessage",
    "FileNamePostMessage",
    "FilePutMessage",
    "FileSharingAccountMessage",
    "FileSharingAccountPutMessage",
    "FileSharingAssociationMessage",
    "FileSharingAssociationOwnerMessage",
    "FileSharingAssociationOwnerPutMessage",
    "FileSharingAssociationPutMessage",
    "FileSharingAssociationUnitMessage",
    "FileSharingAssociationUnitPutMessage",
    "FileSharingCommitteeMessage",
    "FileSharingCommitteePutMessage",
    "FileSharingLeaseMessage",
    "FileSharingLeasePutMessage",
    "FileSharingMessage",
    "FileSharingOwnershipAccountMessage",
    "FileSharingOwnershipAccountPutMessage",
    "FileSharingPutMessage",
    "FileSharingRentalMessage",
    "FileSharingRentalOwnerMessage",
    "FileSharingRentalOwnerPutMessage",
    "FileSharingRentalPutMessage",
    "FileSharingRentalUnitMesage",
    "FileSharingRentalUnitPutMesage",
    "FileSharingTenantMessage",
    "FileSharingTenantPutMessage",
    "FileSharingVendorMessage",
    "FileSharingVendorPutMessage",
    "FileUploadPostMessage",
    "FileUploadTicketMessage",
    "GLAccountBalanceItemMessage",
    "GLAccountBalanceMessage",
    "GLAccountMessage",
    "GLAccountPostMessage",
    "GLAccountPutMessage",
    "GLTransactionMessageV1",
    "GeneralJournalEntryLineSaveMessage",
    "GeneralJournalEntryPostMessage",
    "GeneralJournalEntryPutMessage",
    "GeneralLedgerEntryMessage",
    "GeneralLedgerJournalLineMessage",
    "GeneralLedgerJournalMessage",
    "GeneralLedgerMessage",
    "GeneralLedgerTransactionMessage",
    "ImageReorderRequestPutMessage",
    "InsuredTenantMessage",
    "InternalTransactionStatusMessage",
    "JavaScriptEncoder",
    "JournalLineMessage",
    "JournalMessage",
    "JsonPatchOperation",
    "LastUpdatedByUserMessage",
    "LeaseAccountDetailMessage",
    "LeaseAutoAllocatedPaymentPostMessage",
    "LeaseChargeLineMessage",
    "LeaseChargeLineSaveMessage",
    "LeaseChargeMessage",
    "LeaseChargePostMessage",
    "LeaseChargePutMessage",
    "LeaseChargeRecurringTransactionMessage",
    "LeaseCosignerPostMessage",
    "LeaseLedgerCreditLinePostMessage",
    "LeaseLedgerCreditPostMessage",
    "LeaseLedgerDepositWithholdingLinePostMessage",
    "LeaseLedgerDepositWithholdingLinePutMessage",
    "LeaseLedgerDepositWithholdingPostMessage",
    "LeaseLedgerDepositWithholdingPutMessage",
    "LeaseLedgerPaymentLineSaveMessage",
    "LeaseLedgerPaymentPostMessage",
    "LeaseLedgerPaymentPutMessage",
    "LeaseLedgerRefundLineMessage",
    "LeaseLedgerRefundLinePostMessage",
    "LeaseLedgerRefundMessage",
    "LeaseLedgerRefundPostMessage",
    "LeaseLedgerReversePaymentNSFChargePostMessage",
    "LeaseLedgerReversePaymentOtherBankChargePostMessage",
    "LeaseLedgerReversePaymentPostMessage",
    "LeaseMessage",
    "LeaseMoveOutDataMessage",
    "LeaseMoveOutDataPostMessage",
    "LeaseOutstandingBalanceMessage",
    "LeasePostMessage",
    "LeasePutMessage",
    "LeaseRecurringCreditMessage",
    "LeaseRecurringPaymentMessage",
    "LeaseRenewalMessage",
    "LeaseRenewalPostMessage",
    "LeaseRentChargeMessage",
    "LeaseRentChargePostMessage",
    "LeaseRentMessage",
    "LeaseRentPostMessage",
    "LeaseSecurityDepositPostMessage",
    "LeaseTenantMessage",
    "LeaseTransactionMessage",
    "ListingContactMessage",
    "ListingContactSaveMessage",
    "ListingEntityFilePostMessage",
    "ListingFileMessage",
    "ListingMessage",
    "ListingPropertyMessage",
    "ListingPutMessage",
    "ListingUnitMessage",
    "LockPeriodSettingsGlobalMessage",
    "LockPeriodSettingsOverridesMessage",
    "LoggedByStaffUserMessage",
    "LookupMessage",
    "MailingTemplateMessage",
    "MeterReadingDetailMessage",
    "MeterReadingDetailPutMessage",
    "MeterReadingDetailsMessage",
    "MeterReadingDetailsPutMessage",
    "MeterReadingMessage",
    "MultipleBillPaymentsPostMessage",
    "NoteMessage",
    "NotePostMessage",
    "NotePutMessage",
    "OfflinePaymentsMessage",
    "OfflinePaymentsPutMessage",
    "OutstandingBalancesLineMessage",
    "OwnershipAccountAutoAllocatedPaymentPostMessage",
    "OwnershipAccountChargeRecurringTransactionMessage",
    "OwnershipAccountCreditLinePostMessage",
    "OwnershipAccountCreditPostMessage",
    "OwnershipAccountDepositWithholdingLinePostMessage",
    "OwnershipAccountDepositWithholdingLinePutMessage",
    "OwnershipAccountDepositWithholdingPostMessage",
    "OwnershipAccountDepositWithholdingPutMessage",
    "OwnershipAccountLedgerChargeLineMessage",
    "OwnershipAccountLedgerChargeLinesPutMessage",
    "OwnershipAccountLedgerChargeLinesSaveMessage",
    "OwnershipAccountLedgerChargeMessage",
    "OwnershipAccountLedgerChargePostMessage",
    "OwnershipAccountLedgerChargePutMessage",
    "OwnershipAccountLedgerPaymentLineSaveMessage",
    "OwnershipAccountLedgerPaymentPostMessage",
    "OwnershipAccountLedgerPaymentPutMessage",
    "OwnershipAccountOutstandingBalanceMessage",
    "OwnershipAccountRecurringCreditMessage",
    "OwnershipAccountRecurringPaymentMessage",
    "OwnershipAccountRefundLineMessage",
    "OwnershipAccountRefundLinesPostMessage",
    "OwnershipAccountRefundMessage",
    "OwnershipAccountRefundPostMessage",
    "OwnershipAccountTransactionMessage",
    "PaidByMessage",
    "PartialPaymentSettingsMessage",
    "PartialPaymentSettingsPatchMessage",
    "ParticipantMessage",
    "ParticipantResourceMessage",
    "PayeeMessage",
    "PaymentDetailMessage",
    "PaymentRecurringTransactionPostMessage",
    "PaymentTransactionsMessage",
    "PhoneLogMessage",
    "PhoneLogParticipantPostMessage",
    "PhoneLogParticipantUnitAgreementPostMessage",
    "PhoneLogPostMessage",
    "PhoneLogPutMessage",
    "PhoneNumberMessage",
    "PhoneNumbersMessage",
    "PropertyGroupMessage",
    "PropertyGroupPostMessage",
    "PropertyGroupPutMessage",
    "PropertyManagerMessage",
    "PropertyMessage",
    "RecurringTransactionLineMessage",
    "RecurringTransactionLinePostMessage",
    "RecurringTransactionMessage",
    "RentScheduleChargePostMessage",
    "RentScheduleChargePutMessage",
    "RentSchedulePostMessage",
    "RentSchedulePutMessage",
    "RentalApplianceMessage",
    "RentalAppliancePostMessage",
    "RentalAppliancePutMessage",
    "RentalApplianceServiceHistoryMessage",
    "RentalApplianceServiceHistoryPostMessage",
    "RentalFeaturesMessage",
    "RentalFeaturesPutMessage",
    "RentalImageMessage",
    "RentalImagePutMessage",
    "RentalMessage",
    "RentalOwnerContributionDataMessage",
    "RentalOwnerContributionDataPutMessage",
    "RentalOwnerContributionMessage",
    "RentalOwnerContributionPutMessage",
    "RentalOwnerContributionReminderMessage",
    "RentalOwnerContributionReminderPutMessage",
    "RentalOwnerMessage",
    "RentalOwnerPostMessage",
    "RentalOwnerPutMessage",
    "RentalOwnerRequestTaskMessage",
    "RentalOwnerRequestTaskPostMessage",
    "RentalOwnerRequestTaskPutMessage",
    "RentalOwnerTaxInformationMessage",
    "RentalPreferredVendorMessage",
    "RentalPreferredVendorPutMessage",
    "RentalPropertyPostMessage",
    "RentalPropertyPutMessage",
    "RentalPropertyUnitPostMessage",
    "RentalTenantPostMessage",
    "RentalTenantPutMessage",
    "RentalTenantRenewalPostMessage",
    "RentalUnitFeaturesMessage",
    "RentalUnitFeaturesPutMessage",
    "RentalUnitImageMessage",
    "RentalUnitImagePutMessage",
    "RentalUnitMessage",
    "RentalUnitPutMessage",
    "RentalUnitsPostMessage",
    "RentersInsurancePolicyMessage",
    "RequestedByUserEntityMessage",
    "ResidentCenterUserMessage",
    "ResidentCenterUserReferenceMessage",
    "ResidentRequestTaskMessage",
    "ResidentRequestTaskPostMessage",
    "ResidentRequestTaskPutMessage",
    "RetailCashPropertyMessage",
    "RetailCashUnitMessage",
    "RetailCashUserDataMessage",
    "RetailCashUserMessage",
    "RetailCashUserPutMessage",
    "SaveAddressMessage",
    "SaveEmergencyContactMessage",
    "TaskCategoryMessage",
    "TaskCategoryPutMessage",
    "TaskCategoryResponseMessage",
    "TaskCategorySaveMessage",
    "TaskHistoryFileMessage",
    "TaskHistoryFileUploadPostMessage",
    "TaskHistoryMessage",
    "TaskHistoryPutMessage",
    "TaskHistoryUserMessage",
    "TaskSubCategoryMessage",
    "TaxInformationPostMessage",
    "TaxInformationSaveMessage",
    "TenantMessage",
    "ToDoTaskMessage",
    "ToDoTaskPostMessage",
    "ToDoTaskPutMessage",
    "UndepositedFundsMessage",
    "UnitAgreementMessage",
    "UnitEntityMessage",
    "UserMessage",
    "UserRoleMessage",
    "VehicleMessage",
    "VendorCategoryMessage",
    "VendorCategorySaveMessage",
    "VendorCreditLineItemMessage",
    "VendorCreditLineItemPostMessage",
    "VendorCreditMessage",
    "VendorCreditPostMessage",
    "VendorInsuranceMessage",
    "VendorInsuranceSaveMessage",
    "VendorMessage",
    "VendorPostMessage",
    "VendorPutMessage",
    "VendorRefundLineMessage",
    "VendorRefundLinePostMessage",
    "VendorRefundMessage",
    "VendorRefundPostMessage",
    "VendorTaxInformationMessage",
    "VendorTransactionMessage",
    "VideoLinkRequestPostMessage",
    "WorkOrderEntryContactMessage",
    "WorkOrderEntryContactResourceMessage",
    "WorkOrderLineItemMessage",
    "WorkOrderLineItemSaveMessage",
    "WorkOrderMessage",
    "WorkOrderPostMessage",
    "WorkOrderPutMessage",
    "WorkOrderTaskMessage",
    "WorkOrderTaskPostMessage",
]

# import apis into sdk package
from openapi_client.api.administration_api import AdministrationApi as AdministrationApi
from openapi_client.api.appliances_api import AppliancesApi as AppliancesApi
from openapi_client.api.applicants_api import ApplicantsApi as ApplicantsApi
from openapi_client.api.architectural_requests_api import ArchitecturalRequestsApi as ArchitecturalRequestsApi
from openapi_client.api.association_meter_readings_api import AssociationMeterReadingsApi as AssociationMeterReadingsApi
from openapi_client.api.association_owners_api import AssociationOwnersApi as AssociationOwnersApi
from openapi_client.api.association_tenants_api import AssociationTenantsApi as AssociationTenantsApi
from openapi_client.api.association_units_api import AssociationUnitsApi as AssociationUnitsApi
from openapi_client.api.associations_api import AssociationsApi as AssociationsApi
from openapi_client.api.bank_accounts_api import BankAccountsApi as BankAccountsApi
from openapi_client.api.bills_api import BillsApi as BillsApi
from openapi_client.api.board_members_api import BoardMembersApi as BoardMembersApi
from openapi_client.api.budgets_api import BudgetsApi as BudgetsApi
from openapi_client.api.client_leads_api import ClientLeadsApi as ClientLeadsApi
from openapi_client.api.communications_api import CommunicationsApi as CommunicationsApi
from openapi_client.api.contact_requests_api import ContactRequestsApi as ContactRequestsApi
from openapi_client.api.files_api import FilesApi as FilesApi
from openapi_client.api.general_ledger_api import GeneralLedgerApi as GeneralLedgerApi
from openapi_client.api.lease_transactions_api import LeaseTransactionsApi as LeaseTransactionsApi
from openapi_client.api.leases_api import LeasesApi as LeasesApi
from openapi_client.api.listings_api import ListingsApi as ListingsApi
from openapi_client.api.ownership_account_transactions_api import OwnershipAccountTransactionsApi as OwnershipAccountTransactionsApi
from openapi_client.api.ownership_accounts_api import OwnershipAccountsApi as OwnershipAccountsApi
from openapi_client.api.property_groups_api import PropertyGroupsApi as PropertyGroupsApi
from openapi_client.api.rental_appliances_api import RentalAppliancesApi as RentalAppliancesApi
from openapi_client.api.rental_meter_readings_api import RentalMeterReadingsApi as RentalMeterReadingsApi
from openapi_client.api.rental_owner_requests_api import RentalOwnerRequestsApi as RentalOwnerRequestsApi
from openapi_client.api.rental_owners_api import RentalOwnersApi as RentalOwnersApi
from openapi_client.api.rental_properties_api import RentalPropertiesApi as RentalPropertiesApi
from openapi_client.api.rental_tenants_api import RentalTenantsApi as RentalTenantsApi
from openapi_client.api.rental_units_api import RentalUnitsApi as RentalUnitsApi
from openapi_client.api.resident_center_api import ResidentCenterApi as ResidentCenterApi
from openapi_client.api.resident_requests_api import ResidentRequestsApi as ResidentRequestsApi
from openapi_client.api.tasks_api import TasksApi as TasksApi
from openapi_client.api.to_do_requests_api import ToDoRequestsApi as ToDoRequestsApi
from openapi_client.api.vendors_api import VendorsApi as VendorsApi
from openapi_client.api.work_orders_api import WorkOrdersApi as WorkOrdersApi

# import ApiClient
from openapi_client.api_response import ApiResponse as ApiResponse
from openapi_client.api_client import ApiClient as ApiClient
from openapi_client.configuration import Configuration as Configuration
from openapi_client.exceptions import OpenApiException as OpenApiException
from openapi_client.exceptions import ApiTypeError as ApiTypeError
from openapi_client.exceptions import ApiValueError as ApiValueError
from openapi_client.exceptions import ApiKeyError as ApiKeyError
from openapi_client.exceptions import ApiAttributeError as ApiAttributeError
from openapi_client.exceptions import ApiException as ApiException

# import models into sdk package
from openapi_client.models.account_info_message import AccountInfoMessage as AccountInfoMessage
from openapi_client.models.accounting_entity_message import AccountingEntityMessage as AccountingEntityMessage
from openapi_client.models.accounting_entity_patch_message import AccountingEntityPatchMessage as AccountingEntityPatchMessage
from openapi_client.models.accounting_entity_save_message import AccountingEntitySaveMessage as AccountingEntitySaveMessage
from openapi_client.models.accounting_lock_period_message import AccountingLockPeriodMessage as AccountingLockPeriodMessage
from openapi_client.models.accounting_settings_message import AccountingSettingsMessage as AccountingSettingsMessage
from openapi_client.models.address_message import AddressMessage as AddressMessage
from openapi_client.models.all_tasks_message import AllTasksMessage as AllTasksMessage
from openapi_client.models.announcement_message import AnnouncementMessage as AnnouncementMessage
from openapi_client.models.announcement_post_message import AnnouncementPostMessage as AnnouncementPostMessage
from openapi_client.models.announcement_sender_message import AnnouncementSenderMessage as AnnouncementSenderMessage
from openapi_client.models.api_error import ApiError as ApiError
from openapi_client.models.api_error_response import ApiErrorResponse as ApiErrorResponse
from openapi_client.models.appliance_message import ApplianceMessage as ApplianceMessage
from openapi_client.models.applicant_application_message import ApplicantApplicationMessage as ApplicantApplicationMessage
from openapi_client.models.applicant_group_message import ApplicantGroupMessage as ApplicantGroupMessage
from openapi_client.models.applicant_group_post_message import ApplicantGroupPostMessage as ApplicantGroupPostMessage
from openapi_client.models.applicant_group_put_message import ApplicantGroupPutMessage as ApplicantGroupPutMessage
from openapi_client.models.applicant_message import ApplicantMessage as ApplicantMessage
from openapi_client.models.applicant_post_message import ApplicantPostMessage as ApplicantPostMessage
from openapi_client.models.applicant_put_message import ApplicantPutMessage as ApplicantPutMessage
from openapi_client.models.application_message import ApplicationMessage as ApplicationMessage
from openapi_client.models.application_put_message import ApplicationPutMessage as ApplicationPutMessage
from openapi_client.models.application_response_field_message import ApplicationResponseFieldMessage as ApplicationResponseFieldMessage
from openapi_client.models.application_response_message import ApplicationResponseMessage as ApplicationResponseMessage
from openapi_client.models.application_section_response_message import ApplicationSectionResponseMessage as ApplicationSectionResponseMessage
from openapi_client.models.applied_vendor_credit_message import AppliedVendorCreditMessage as AppliedVendorCreditMessage
from openapi_client.models.architectural_requests_post_message import ArchitecturalRequestsPostMessage as ArchitecturalRequestsPostMessage
from openapi_client.models.association_appliance_message import AssociationApplianceMessage as AssociationApplianceMessage
from openapi_client.models.association_appliance_post_message import AssociationAppliancePostMessage as AssociationAppliancePostMessage
from openapi_client.models.association_appliance_put_message import AssociationAppliancePutMessage as AssociationAppliancePutMessage
from openapi_client.models.association_appliance_service_history_message import AssociationApplianceServiceHistoryMessage as AssociationApplianceServiceHistoryMessage
from openapi_client.models.association_appliance_service_history_post_message import AssociationApplianceServiceHistoryPostMessage as AssociationApplianceServiceHistoryPostMessage
from openapi_client.models.association_architectural_request_file_message import AssociationArchitecturalRequestFileMessage as AssociationArchitecturalRequestFileMessage
from openapi_client.models.association_architectural_request_message import AssociationArchitecturalRequestMessage as AssociationArchitecturalRequestMessage
from openapi_client.models.association_board_member_message import AssociationBoardMemberMessage as AssociationBoardMemberMessage
from openapi_client.models.association_board_member_post_message import AssociationBoardMemberPostMessage as AssociationBoardMemberPostMessage
from openapi_client.models.association_board_member_put_message import AssociationBoardMemberPutMessage as AssociationBoardMemberPutMessage
from openapi_client.models.association_message import AssociationMessage as AssociationMessage
from openapi_client.models.association_owner_board_term_message import AssociationOwnerBoardTermMessage as AssociationOwnerBoardTermMessage
from openapi_client.models.association_owner_board_term_post_message import AssociationOwnerBoardTermPostMessage as AssociationOwnerBoardTermPostMessage
from openapi_client.models.association_owner_message import AssociationOwnerMessage as AssociationOwnerMessage
from openapi_client.models.association_owner_post_message import AssociationOwnerPostMessage as AssociationOwnerPostMessage
from openapi_client.models.association_owner_put_message import AssociationOwnerPutMessage as AssociationOwnerPutMessage
from openapi_client.models.association_owner_to_existing_ownership_account_post_message import AssociationOwnerToExistingOwnershipAccountPostMessage as AssociationOwnerToExistingOwnershipAccountPostMessage
from openapi_client.models.association_owner_unit_occupancy_put_message import AssociationOwnerUnitOccupancyPutMessage as AssociationOwnerUnitOccupancyPutMessage
from openapi_client.models.association_owner_unit_occupancy_status_message import AssociationOwnerUnitOccupancyStatusMessage as AssociationOwnerUnitOccupancyStatusMessage
from openapi_client.models.association_ownership_account_message import AssociationOwnershipAccountMessage as AssociationOwnershipAccountMessage
from openapi_client.models.association_ownership_account_post_message import AssociationOwnershipAccountPostMessage as AssociationOwnershipAccountPostMessage
from openapi_client.models.association_ownership_account_put_message import AssociationOwnershipAccountPutMessage as AssociationOwnershipAccountPutMessage
from openapi_client.models.association_post_message import AssociationPostMessage as AssociationPostMessage
from openapi_client.models.association_preferred_vendor_message import AssociationPreferredVendorMessage as AssociationPreferredVendorMessage
from openapi_client.models.association_preferred_vendor_put_message import AssociationPreferredVendorPutMessage as AssociationPreferredVendorPutMessage
from openapi_client.models.association_put_message import AssociationPutMessage as AssociationPutMessage
from openapi_client.models.association_tax_information_message import AssociationTaxInformationMessage as AssociationTaxInformationMessage
from openapi_client.models.association_tenant_message import AssociationTenantMessage as AssociationTenantMessage
from openapi_client.models.association_tenant_post_message import AssociationTenantPostMessage as AssociationTenantPostMessage
from openapi_client.models.association_tenant_put_message import AssociationTenantPutMessage as AssociationTenantPutMessage
from openapi_client.models.association_unit_message import AssociationUnitMessage as AssociationUnitMessage
from openapi_client.models.association_unit_put_message import AssociationUnitPutMessage as AssociationUnitPutMessage
from openapi_client.models.association_units_post_message import AssociationUnitsPostMessage as AssociationUnitsPostMessage
from openapi_client.models.bank_account_check_accounting_entity_save_message import BankAccountCheckAccountingEntitySaveMessage as BankAccountCheckAccountingEntitySaveMessage
from openapi_client.models.bank_account_check_file_message import BankAccountCheckFileMessage as BankAccountCheckFileMessage
from openapi_client.models.bank_account_check_line_message import BankAccountCheckLineMessage as BankAccountCheckLineMessage
from openapi_client.models.bank_account_check_line_save_message import BankAccountCheckLineSaveMessage as BankAccountCheckLineSaveMessage
from openapi_client.models.bank_account_check_message import BankAccountCheckMessage as BankAccountCheckMessage
from openapi_client.models.bank_account_check_payee_message import BankAccountCheckPayeeMessage as BankAccountCheckPayeeMessage
from openapi_client.models.bank_account_check_payee_save_message import BankAccountCheckPayeeSaveMessage as BankAccountCheckPayeeSaveMessage
from openapi_client.models.bank_account_check_post_message import BankAccountCheckPostMessage as BankAccountCheckPostMessage
from openapi_client.models.bank_account_check_put_message import BankAccountCheckPutMessage as BankAccountCheckPutMessage
from openapi_client.models.bank_account_deposit_line_message import BankAccountDepositLineMessage as BankAccountDepositLineMessage
from openapi_client.models.bank_account_deposit_line_save_message import BankAccountDepositLineSaveMessage as BankAccountDepositLineSaveMessage
from openapi_client.models.bank_account_deposit_message import BankAccountDepositMessage as BankAccountDepositMessage
from openapi_client.models.bank_account_deposit_post_message import BankAccountDepositPostMessage as BankAccountDepositPostMessage
from openapi_client.models.bank_account_deposit_put_message import BankAccountDepositPutMessage as BankAccountDepositPutMessage
from openapi_client.models.bank_account_message import BankAccountMessage as BankAccountMessage
from openapi_client.models.bank_account_post_message import BankAccountPostMessage as BankAccountPostMessage
from openapi_client.models.bank_account_put_message import BankAccountPutMessage as BankAccountPutMessage
from openapi_client.models.bank_account_quick_deposit_message import BankAccountQuickDepositMessage as BankAccountQuickDepositMessage
from openapi_client.models.bank_account_quick_deposit_save_message import BankAccountQuickDepositSaveMessage as BankAccountQuickDepositSaveMessage
from openapi_client.models.bank_account_reconciliation_balance_message import BankAccountReconciliationBalanceMessage as BankAccountReconciliationBalanceMessage
from openapi_client.models.bank_account_reconciliation_balance_put_message import BankAccountReconciliationBalancePutMessage as BankAccountReconciliationBalancePutMessage
from openapi_client.models.bank_account_reconciliation_message import BankAccountReconciliationMessage as BankAccountReconciliationMessage
from openapi_client.models.bank_account_reconciliation_transaction_message import BankAccountReconciliationTransactionMessage as BankAccountReconciliationTransactionMessage
from openapi_client.models.bank_account_transaction_message import BankAccountTransactionMessage as BankAccountTransactionMessage
from openapi_client.models.bank_account_transfer_accounting_entity_save_message import BankAccountTransferAccountingEntitySaveMessage as BankAccountTransferAccountingEntitySaveMessage
from openapi_client.models.bank_account_transfer_message import BankAccountTransferMessage as BankAccountTransferMessage
from openapi_client.models.bank_account_transfer_save_message import BankAccountTransferSaveMessage as BankAccountTransferSaveMessage
from openapi_client.models.bank_account_withdrawal_message import BankAccountWithdrawalMessage as BankAccountWithdrawalMessage
from openapi_client.models.bank_account_withdrawal_save_message import BankAccountWithdrawalSaveMessage as BankAccountWithdrawalSaveMessage
from openapi_client.models.bank_lockbox_data_association_message import BankLockboxDataAssociationMessage as BankLockboxDataAssociationMessage
from openapi_client.models.bank_lockbox_data_association_owner_message import BankLockboxDataAssociationOwnerMessage as BankLockboxDataAssociationOwnerMessage
from openapi_client.models.bank_lockbox_data_message import BankLockboxDataMessage as BankLockboxDataMessage
from openapi_client.models.bank_lockbox_data_ownership_account_message import BankLockboxDataOwnershipAccountMessage as BankLockboxDataOwnershipAccountMessage
from openapi_client.models.bank_pending_reconciliation_post_message import BankPendingReconciliationPostMessage as BankPendingReconciliationPostMessage
from openapi_client.models.bank_reconciliation_clear_transactions_post_message import BankReconciliationClearTransactionsPostMessage as BankReconciliationClearTransactionsPostMessage
from openapi_client.models.bank_reconciliation_cleared_balance_message import BankReconciliationClearedBalanceMessage as BankReconciliationClearedBalanceMessage
from openapi_client.models.bank_reconciliation_put_message import BankReconciliationPutMessage as BankReconciliationPutMessage
from openapi_client.models.bank_reconciliation_statement_balance_message import BankReconciliationStatementBalanceMessage as BankReconciliationStatementBalanceMessage
from openapi_client.models.bank_reconciliation_unclear_transactions_post_message import BankReconciliationUnclearTransactionsPostMessage as BankReconciliationUnclearTransactionsPostMessage
from openapi_client.models.bill_file_message import BillFileMessage as BillFileMessage
from openapi_client.models.bill_line_item_patch_message import BillLineItemPatchMessage as BillLineItemPatchMessage
from openapi_client.models.bill_line_message import BillLineMessage as BillLineMessage
from openapi_client.models.bill_line_post_message import BillLinePostMessage as BillLinePostMessage
from openapi_client.models.bill_line_put_message import BillLinePutMessage as BillLinePutMessage
from openapi_client.models.bill_markup_message import BillMarkupMessage as BillMarkupMessage
from openapi_client.models.bill_markup_patch_message import BillMarkupPatchMessage as BillMarkupPatchMessage
from openapi_client.models.bill_markup_save_message import BillMarkupSaveMessage as BillMarkupSaveMessage
from openapi_client.models.bill_message import BillMessage as BillMessage
from openapi_client.models.bill_patch_message import BillPatchMessage as BillPatchMessage
from openapi_client.models.bill_payment_accounting_entity_message import BillPaymentAccountingEntityMessage as BillPaymentAccountingEntityMessage
from openapi_client.models.bill_payment_line_message import BillPaymentLineMessage as BillPaymentLineMessage
from openapi_client.models.bill_payment_line_post_message import BillPaymentLinePostMessage as BillPaymentLinePostMessage
from openapi_client.models.bill_payment_message import BillPaymentMessage as BillPaymentMessage
from openapi_client.models.bill_payment_post_message import BillPaymentPostMessage as BillPaymentPostMessage
from openapi_client.models.bill_post_message import BillPostMessage as BillPostMessage
from openapi_client.models.bill_put_message import BillPutMessage as BillPutMessage
from openapi_client.models.budget_details_message import BudgetDetailsMessage as BudgetDetailsMessage
from openapi_client.models.budget_details_save_message import BudgetDetailsSaveMessage as BudgetDetailsSaveMessage
from openapi_client.models.budget_message import BudgetMessage as BudgetMessage
from openapi_client.models.budget_monthly_amounts_message import BudgetMonthlyAmountsMessage as BudgetMonthlyAmountsMessage
from openapi_client.models.budget_monthly_amounts_save_message import BudgetMonthlyAmountsSaveMessage as BudgetMonthlyAmountsSaveMessage
from openapi_client.models.budget_post_message import BudgetPostMessage as BudgetPostMessage
from openapi_client.models.budget_put_message import BudgetPutMessage as BudgetPutMessage
from openapi_client.models.cc_payments_message import CCPaymentsMessage as CCPaymentsMessage
from openapi_client.models.cc_payments_put_message import CCPaymentsPutMessage as CCPaymentsPutMessage
from openapi_client.models.charge_recurring_transaction_post_message import ChargeRecurringTransactionPostMessage as ChargeRecurringTransactionPostMessage
from openapi_client.models.charge_recurring_transaction_put_message import ChargeRecurringTransactionPutMessage as ChargeRecurringTransactionPutMessage
from openapi_client.models.check_printing_info_message import CheckPrintingInfoMessage as CheckPrintingInfoMessage
from openapi_client.models.check_printing_info_post_message import CheckPrintingInfoPostMessage as CheckPrintingInfoPostMessage
from openapi_client.models.check_printing_info_put_message import CheckPrintingInfoPutMessage as CheckPrintingInfoPutMessage
from openapi_client.models.client_lead_credit_request_message import ClientLeadCreditRequestMessage as ClientLeadCreditRequestMessage
from openapi_client.models.client_lead_message import ClientLeadMessage as ClientLeadMessage
from openapi_client.models.contact_detail_message import ContactDetailMessage as ContactDetailMessage
from openapi_client.models.contact_detail_phone_message import ContactDetailPhoneMessage as ContactDetailPhoneMessage
from openapi_client.models.contact_detail_save_message import ContactDetailSaveMessage as ContactDetailSaveMessage
from openapi_client.models.contact_detail_save_phone_message import ContactDetailSavePhoneMessage as ContactDetailSavePhoneMessage
from openapi_client.models.contact_info_message import ContactInfoMessage as ContactInfoMessage
from openapi_client.models.contact_request_task_message import ContactRequestTaskMessage as ContactRequestTaskMessage
from openapi_client.models.contact_request_task_post_message import ContactRequestTaskPostMessage as ContactRequestTaskPostMessage
from openapi_client.models.contact_request_task_put_message import ContactRequestTaskPutMessage as ContactRequestTaskPutMessage
from openapi_client.models.cosigner_message import CosignerMessage as CosignerMessage
from openapi_client.models.created_by_user_message import CreatedByUserMessage as CreatedByUserMessage
from openapi_client.models.credit_recurring_transaction_post_message import CreditRecurringTransactionPostMessage as CreditRecurringTransactionPostMessage
from openapi_client.models.deposit_detail_message import DepositDetailMessage as DepositDetailMessage
from openapi_client.models.eft_payments_message import EFTPaymentsMessage as EFTPaymentsMessage
from openapi_client.models.eft_payments_put_message import EFTPaymentsPutMessage as EFTPaymentsPutMessage
from openapi_client.models.e_pay_settings_message import EPaySettingsMessage as EPaySettingsMessage
from openapi_client.models.e_pay_settings_put_message import EPaySettingsPutMessage as EPaySettingsPutMessage
from openapi_client.models.electronic_payments_message import ElectronicPaymentsMessage as ElectronicPaymentsMessage
from openapi_client.models.email_message import EmailMessage as EmailMessage
from openapi_client.models.email_post_message import EmailPostMessage as EmailPostMessage
from openapi_client.models.email_recipient_message import EmailRecipientMessage as EmailRecipientMessage
from openapi_client.models.email_sender_message import EmailSenderMessage as EmailSenderMessage
from openapi_client.models.emergency_contact_message import EmergencyContactMessage as EmergencyContactMessage
from openapi_client.models.file_category_message import FileCategoryMessage as FileCategoryMessage
from openapi_client.models.file_category_post_message import FileCategoryPostMessage as FileCategoryPostMessage
from openapi_client.models.file_category_put_message import FileCategoryPutMessage as FileCategoryPutMessage
from openapi_client.models.file_download_message import FileDownloadMessage as FileDownloadMessage
from openapi_client.models.file_entity_message import FileEntityMessage as FileEntityMessage
from openapi_client.models.file_message import FileMessage as FileMessage
from openapi_client.models.file_name_post_message import FileNamePostMessage as FileNamePostMessage
from openapi_client.models.file_put_message import FilePutMessage as FilePutMessage
from openapi_client.models.file_sharing_account_message import FileSharingAccountMessage as FileSharingAccountMessage
from openapi_client.models.file_sharing_account_put_message import FileSharingAccountPutMessage as FileSharingAccountPutMessage
from openapi_client.models.file_sharing_association_message import FileSharingAssociationMessage as FileSharingAssociationMessage
from openapi_client.models.file_sharing_association_owner_message import FileSharingAssociationOwnerMessage as FileSharingAssociationOwnerMessage
from openapi_client.models.file_sharing_association_owner_put_message import FileSharingAssociationOwnerPutMessage as FileSharingAssociationOwnerPutMessage
from openapi_client.models.file_sharing_association_put_message import FileSharingAssociationPutMessage as FileSharingAssociationPutMessage
from openapi_client.models.file_sharing_association_unit_message import FileSharingAssociationUnitMessage as FileSharingAssociationUnitMessage
from openapi_client.models.file_sharing_association_unit_put_message import FileSharingAssociationUnitPutMessage as FileSharingAssociationUnitPutMessage
from openapi_client.models.file_sharing_committee_message import FileSharingCommitteeMessage as FileSharingCommitteeMessage
from openapi_client.models.file_sharing_committee_put_message import FileSharingCommitteePutMessage as FileSharingCommitteePutMessage
from openapi_client.models.file_sharing_lease_message import FileSharingLeaseMessage as FileSharingLeaseMessage
from openapi_client.models.file_sharing_lease_put_message import FileSharingLeasePutMessage as FileSharingLeasePutMessage
from openapi_client.models.file_sharing_message import FileSharingMessage as FileSharingMessage
from openapi_client.models.file_sharing_ownership_account_message import FileSharingOwnershipAccountMessage as FileSharingOwnershipAccountMessage
from openapi_client.models.file_sharing_ownership_account_put_message import FileSharingOwnershipAccountPutMessage as FileSharingOwnershipAccountPutMessage
from openapi_client.models.file_sharing_put_message import FileSharingPutMessage as FileSharingPutMessage
from openapi_client.models.file_sharing_rental_message import FileSharingRentalMessage as FileSharingRentalMessage
from openapi_client.models.file_sharing_rental_owner_message import FileSharingRentalOwnerMessage as FileSharingRentalOwnerMessage
from openapi_client.models.file_sharing_rental_owner_put_message import FileSharingRentalOwnerPutMessage as FileSharingRentalOwnerPutMessage
from openapi_client.models.file_sharing_rental_put_message import FileSharingRentalPutMessage as FileSharingRentalPutMessage
from openapi_client.models.file_sharing_rental_unit_mesage import FileSharingRentalUnitMesage as FileSharingRentalUnitMesage
from openapi_client.models.file_sharing_rental_unit_put_mesage import FileSharingRentalUnitPutMesage as FileSharingRentalUnitPutMesage
from openapi_client.models.file_sharing_tenant_message import FileSharingTenantMessage as FileSharingTenantMessage
from openapi_client.models.file_sharing_tenant_put_message import FileSharingTenantPutMessage as FileSharingTenantPutMessage
from openapi_client.models.file_sharing_vendor_message import FileSharingVendorMessage as FileSharingVendorMessage
from openapi_client.models.file_sharing_vendor_put_message import FileSharingVendorPutMessage as FileSharingVendorPutMessage
from openapi_client.models.file_upload_post_message import FileUploadPostMessage as FileUploadPostMessage
from openapi_client.models.file_upload_ticket_message import FileUploadTicketMessage as FileUploadTicketMessage
from openapi_client.models.gl_account_balance_item_message import GLAccountBalanceItemMessage as GLAccountBalanceItemMessage
from openapi_client.models.gl_account_balance_message import GLAccountBalanceMessage as GLAccountBalanceMessage
from openapi_client.models.gl_account_message import GLAccountMessage as GLAccountMessage
from openapi_client.models.gl_account_post_message import GLAccountPostMessage as GLAccountPostMessage
from openapi_client.models.gl_account_put_message import GLAccountPutMessage as GLAccountPutMessage
from openapi_client.models.gl_transaction_message_v1 import GLTransactionMessageV1 as GLTransactionMessageV1
from openapi_client.models.general_journal_entry_line_save_message import GeneralJournalEntryLineSaveMessage as GeneralJournalEntryLineSaveMessage
from openapi_client.models.general_journal_entry_post_message import GeneralJournalEntryPostMessage as GeneralJournalEntryPostMessage
from openapi_client.models.general_journal_entry_put_message import GeneralJournalEntryPutMessage as GeneralJournalEntryPutMessage
from openapi_client.models.general_ledger_entry_message import GeneralLedgerEntryMessage as GeneralLedgerEntryMessage
from openapi_client.models.general_ledger_journal_line_message import GeneralLedgerJournalLineMessage as GeneralLedgerJournalLineMessage
from openapi_client.models.general_ledger_journal_message import GeneralLedgerJournalMessage as GeneralLedgerJournalMessage
from openapi_client.models.general_ledger_message import GeneralLedgerMessage as GeneralLedgerMessage
from openapi_client.models.general_ledger_transaction_message import GeneralLedgerTransactionMessage as GeneralLedgerTransactionMessage
from openapi_client.models.image_reorder_request_put_message import ImageReorderRequestPutMessage as ImageReorderRequestPutMessage
from openapi_client.models.insured_tenant_message import InsuredTenantMessage as InsuredTenantMessage
from openapi_client.models.internal_transaction_status_message import InternalTransactionStatusMessage as InternalTransactionStatusMessage
from openapi_client.models.java_script_encoder import JavaScriptEncoder as JavaScriptEncoder
from openapi_client.models.journal_line_message import JournalLineMessage as JournalLineMessage
from openapi_client.models.journal_message import JournalMessage as JournalMessage
from openapi_client.models.json_patch_operation import JsonPatchOperation as JsonPatchOperation
from openapi_client.models.last_updated_by_user_message import LastUpdatedByUserMessage as LastUpdatedByUserMessage
from openapi_client.models.lease_account_detail_message import LeaseAccountDetailMessage as LeaseAccountDetailMessage
from openapi_client.models.lease_auto_allocated_payment_post_message import LeaseAutoAllocatedPaymentPostMessage as LeaseAutoAllocatedPaymentPostMessage
from openapi_client.models.lease_charge_line_message import LeaseChargeLineMessage as LeaseChargeLineMessage
from openapi_client.models.lease_charge_line_save_message import LeaseChargeLineSaveMessage as LeaseChargeLineSaveMessage
from openapi_client.models.lease_charge_message import LeaseChargeMessage as LeaseChargeMessage
from openapi_client.models.lease_charge_post_message import LeaseChargePostMessage as LeaseChargePostMessage
from openapi_client.models.lease_charge_put_message import LeaseChargePutMessage as LeaseChargePutMessage
from openapi_client.models.lease_charge_recurring_transaction_message import LeaseChargeRecurringTransactionMessage as LeaseChargeRecurringTransactionMessage
from openapi_client.models.lease_cosigner_post_message import LeaseCosignerPostMessage as LeaseCosignerPostMessage
from openapi_client.models.lease_ledger_credit_line_post_message import LeaseLedgerCreditLinePostMessage as LeaseLedgerCreditLinePostMessage
from openapi_client.models.lease_ledger_credit_post_message import LeaseLedgerCreditPostMessage as LeaseLedgerCreditPostMessage
from openapi_client.models.lease_ledger_deposit_withholding_line_post_message import LeaseLedgerDepositWithholdingLinePostMessage as LeaseLedgerDepositWithholdingLinePostMessage
from openapi_client.models.lease_ledger_deposit_withholding_line_put_message import LeaseLedgerDepositWithholdingLinePutMessage as LeaseLedgerDepositWithholdingLinePutMessage
from openapi_client.models.lease_ledger_deposit_withholding_post_message import LeaseLedgerDepositWithholdingPostMessage as LeaseLedgerDepositWithholdingPostMessage
from openapi_client.models.lease_ledger_deposit_withholding_put_message import LeaseLedgerDepositWithholdingPutMessage as LeaseLedgerDepositWithholdingPutMessage
from openapi_client.models.lease_ledger_payment_line_save_message import LeaseLedgerPaymentLineSaveMessage as LeaseLedgerPaymentLineSaveMessage
from openapi_client.models.lease_ledger_payment_post_message import LeaseLedgerPaymentPostMessage as LeaseLedgerPaymentPostMessage
from openapi_client.models.lease_ledger_payment_put_message import LeaseLedgerPaymentPutMessage as LeaseLedgerPaymentPutMessage
from openapi_client.models.lease_ledger_refund_line_message import LeaseLedgerRefundLineMessage as LeaseLedgerRefundLineMessage
from openapi_client.models.lease_ledger_refund_line_post_message import LeaseLedgerRefundLinePostMessage as LeaseLedgerRefundLinePostMessage
from openapi_client.models.lease_ledger_refund_message import LeaseLedgerRefundMessage as LeaseLedgerRefundMessage
from openapi_client.models.lease_ledger_refund_post_message import LeaseLedgerRefundPostMessage as LeaseLedgerRefundPostMessage
from openapi_client.models.lease_ledger_reverse_payment_nsf_charge_post_message import LeaseLedgerReversePaymentNSFChargePostMessage as LeaseLedgerReversePaymentNSFChargePostMessage
from openapi_client.models.lease_ledger_reverse_payment_other_bank_charge_post_message import LeaseLedgerReversePaymentOtherBankChargePostMessage as LeaseLedgerReversePaymentOtherBankChargePostMessage
from openapi_client.models.lease_ledger_reverse_payment_post_message import LeaseLedgerReversePaymentPostMessage as LeaseLedgerReversePaymentPostMessage
from openapi_client.models.lease_message import LeaseMessage as LeaseMessage
from openapi_client.models.lease_move_out_data_message import LeaseMoveOutDataMessage as LeaseMoveOutDataMessage
from openapi_client.models.lease_move_out_data_post_message import LeaseMoveOutDataPostMessage as LeaseMoveOutDataPostMessage
from openapi_client.models.lease_outstanding_balance_message import LeaseOutstandingBalanceMessage as LeaseOutstandingBalanceMessage
from openapi_client.models.lease_post_message import LeasePostMessage as LeasePostMessage
from openapi_client.models.lease_put_message import LeasePutMessage as LeasePutMessage
from openapi_client.models.lease_recurring_credit_message import LeaseRecurringCreditMessage as LeaseRecurringCreditMessage
from openapi_client.models.lease_recurring_payment_message import LeaseRecurringPaymentMessage as LeaseRecurringPaymentMessage
from openapi_client.models.lease_renewal_message import LeaseRenewalMessage as LeaseRenewalMessage
from openapi_client.models.lease_renewal_post_message import LeaseRenewalPostMessage as LeaseRenewalPostMessage
from openapi_client.models.lease_rent_charge_message import LeaseRentChargeMessage as LeaseRentChargeMessage
from openapi_client.models.lease_rent_charge_post_message import LeaseRentChargePostMessage as LeaseRentChargePostMessage
from openapi_client.models.lease_rent_message import LeaseRentMessage as LeaseRentMessage
from openapi_client.models.lease_rent_post_message import LeaseRentPostMessage as LeaseRentPostMessage
from openapi_client.models.lease_security_deposit_post_message import LeaseSecurityDepositPostMessage as LeaseSecurityDepositPostMessage
from openapi_client.models.lease_tenant_message import LeaseTenantMessage as LeaseTenantMessage
from openapi_client.models.lease_transaction_message import LeaseTransactionMessage as LeaseTransactionMessage
from openapi_client.models.listing_contact_message import ListingContactMessage as ListingContactMessage
from openapi_client.models.listing_contact_save_message import ListingContactSaveMessage as ListingContactSaveMessage
from openapi_client.models.listing_entity_file_post_message import ListingEntityFilePostMessage as ListingEntityFilePostMessage
from openapi_client.models.listing_file_message import ListingFileMessage as ListingFileMessage
from openapi_client.models.listing_message import ListingMessage as ListingMessage
from openapi_client.models.listing_property_message import ListingPropertyMessage as ListingPropertyMessage
from openapi_client.models.listing_put_message import ListingPutMessage as ListingPutMessage
from openapi_client.models.listing_unit_message import ListingUnitMessage as ListingUnitMessage
from openapi_client.models.lock_period_settings_global_message import LockPeriodSettingsGlobalMessage as LockPeriodSettingsGlobalMessage
from openapi_client.models.lock_period_settings_overrides_message import LockPeriodSettingsOverridesMessage as LockPeriodSettingsOverridesMessage
from openapi_client.models.logged_by_staff_user_message import LoggedByStaffUserMessage as LoggedByStaffUserMessage
from openapi_client.models.lookup_message import LookupMessage as LookupMessage
from openapi_client.models.mailing_template_message import MailingTemplateMessage as MailingTemplateMessage
from openapi_client.models.meter_reading_detail_message import MeterReadingDetailMessage as MeterReadingDetailMessage
from openapi_client.models.meter_reading_detail_put_message import MeterReadingDetailPutMessage as MeterReadingDetailPutMessage
from openapi_client.models.meter_reading_details_message import MeterReadingDetailsMessage as MeterReadingDetailsMessage
from openapi_client.models.meter_reading_details_put_message import MeterReadingDetailsPutMessage as MeterReadingDetailsPutMessage
from openapi_client.models.meter_reading_message import MeterReadingMessage as MeterReadingMessage
from openapi_client.models.multiple_bill_payments_post_message import MultipleBillPaymentsPostMessage as MultipleBillPaymentsPostMessage
from openapi_client.models.note_message import NoteMessage as NoteMessage
from openapi_client.models.note_post_message import NotePostMessage as NotePostMessage
from openapi_client.models.note_put_message import NotePutMessage as NotePutMessage
from openapi_client.models.offline_payments_message import OfflinePaymentsMessage as OfflinePaymentsMessage
from openapi_client.models.offline_payments_put_message import OfflinePaymentsPutMessage as OfflinePaymentsPutMessage
from openapi_client.models.outstanding_balances_line_message import OutstandingBalancesLineMessage as OutstandingBalancesLineMessage
from openapi_client.models.ownership_account_auto_allocated_payment_post_message import OwnershipAccountAutoAllocatedPaymentPostMessage as OwnershipAccountAutoAllocatedPaymentPostMessage
from openapi_client.models.ownership_account_charge_recurring_transaction_message import OwnershipAccountChargeRecurringTransactionMessage as OwnershipAccountChargeRecurringTransactionMessage
from openapi_client.models.ownership_account_credit_line_post_message import OwnershipAccountCreditLinePostMessage as OwnershipAccountCreditLinePostMessage
from openapi_client.models.ownership_account_credit_post_message import OwnershipAccountCreditPostMessage as OwnershipAccountCreditPostMessage
from openapi_client.models.ownership_account_deposit_withholding_line_post_message import OwnershipAccountDepositWithholdingLinePostMessage as OwnershipAccountDepositWithholdingLinePostMessage
from openapi_client.models.ownership_account_deposit_withholding_line_put_message import OwnershipAccountDepositWithholdingLinePutMessage as OwnershipAccountDepositWithholdingLinePutMessage
from openapi_client.models.ownership_account_deposit_withholding_post_message import OwnershipAccountDepositWithholdingPostMessage as OwnershipAccountDepositWithholdingPostMessage
from openapi_client.models.ownership_account_deposit_withholding_put_message import OwnershipAccountDepositWithholdingPutMessage as OwnershipAccountDepositWithholdingPutMessage
from openapi_client.models.ownership_account_ledger_charge_line_message import OwnershipAccountLedgerChargeLineMessage as OwnershipAccountLedgerChargeLineMessage
from openapi_client.models.ownership_account_ledger_charge_lines_put_message import OwnershipAccountLedgerChargeLinesPutMessage as OwnershipAccountLedgerChargeLinesPutMessage
from openapi_client.models.ownership_account_ledger_charge_lines_save_message import OwnershipAccountLedgerChargeLinesSaveMessage as OwnershipAccountLedgerChargeLinesSaveMessage
from openapi_client.models.ownership_account_ledger_charge_message import OwnershipAccountLedgerChargeMessage as OwnershipAccountLedgerChargeMessage
from openapi_client.models.ownership_account_ledger_charge_post_message import OwnershipAccountLedgerChargePostMessage as OwnershipAccountLedgerChargePostMessage
from openapi_client.models.ownership_account_ledger_charge_put_message import OwnershipAccountLedgerChargePutMessage as OwnershipAccountLedgerChargePutMessage
from openapi_client.models.ownership_account_ledger_payment_line_save_message import OwnershipAccountLedgerPaymentLineSaveMessage as OwnershipAccountLedgerPaymentLineSaveMessage
from openapi_client.models.ownership_account_ledger_payment_post_message import OwnershipAccountLedgerPaymentPostMessage as OwnershipAccountLedgerPaymentPostMessage
from openapi_client.models.ownership_account_ledger_payment_put_message import OwnershipAccountLedgerPaymentPutMessage as OwnershipAccountLedgerPaymentPutMessage
from openapi_client.models.ownership_account_outstanding_balance_message import OwnershipAccountOutstandingBalanceMessage as OwnershipAccountOutstandingBalanceMessage
from openapi_client.models.ownership_account_recurring_credit_message import OwnershipAccountRecurringCreditMessage as OwnershipAccountRecurringCreditMessage
from openapi_client.models.ownership_account_recurring_payment_message import OwnershipAccountRecurringPaymentMessage as OwnershipAccountRecurringPaymentMessage
from openapi_client.models.ownership_account_refund_line_message import OwnershipAccountRefundLineMessage as OwnershipAccountRefundLineMessage
from openapi_client.models.ownership_account_refund_lines_post_message import OwnershipAccountRefundLinesPostMessage as OwnershipAccountRefundLinesPostMessage
from openapi_client.models.ownership_account_refund_message import OwnershipAccountRefundMessage as OwnershipAccountRefundMessage
from openapi_client.models.ownership_account_refund_post_message import OwnershipAccountRefundPostMessage as OwnershipAccountRefundPostMessage
from openapi_client.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage as OwnershipAccountTransactionMessage
from openapi_client.models.paid_by_message import PaidByMessage as PaidByMessage
from openapi_client.models.partial_payment_settings_message import PartialPaymentSettingsMessage as PartialPaymentSettingsMessage
from openapi_client.models.partial_payment_settings_patch_message import PartialPaymentSettingsPatchMessage as PartialPaymentSettingsPatchMessage
from openapi_client.models.participant_message import ParticipantMessage as ParticipantMessage
from openapi_client.models.participant_resource_message import ParticipantResourceMessage as ParticipantResourceMessage
from openapi_client.models.payee_message import PayeeMessage as PayeeMessage
from openapi_client.models.payment_detail_message import PaymentDetailMessage as PaymentDetailMessage
from openapi_client.models.payment_recurring_transaction_post_message import PaymentRecurringTransactionPostMessage as PaymentRecurringTransactionPostMessage
from openapi_client.models.payment_transactions_message import PaymentTransactionsMessage as PaymentTransactionsMessage
from openapi_client.models.phone_log_message import PhoneLogMessage as PhoneLogMessage
from openapi_client.models.phone_log_participant_post_message import PhoneLogParticipantPostMessage as PhoneLogParticipantPostMessage
from openapi_client.models.phone_log_participant_unit_agreement_post_message import PhoneLogParticipantUnitAgreementPostMessage as PhoneLogParticipantUnitAgreementPostMessage
from openapi_client.models.phone_log_post_message import PhoneLogPostMessage as PhoneLogPostMessage
from openapi_client.models.phone_log_put_message import PhoneLogPutMessage as PhoneLogPutMessage
from openapi_client.models.phone_number_message import PhoneNumberMessage as PhoneNumberMessage
from openapi_client.models.phone_numbers_message import PhoneNumbersMessage as PhoneNumbersMessage
from openapi_client.models.property_group_message import PropertyGroupMessage as PropertyGroupMessage
from openapi_client.models.property_group_post_message import PropertyGroupPostMessage as PropertyGroupPostMessage
from openapi_client.models.property_group_put_message import PropertyGroupPutMessage as PropertyGroupPutMessage
from openapi_client.models.property_manager_message import PropertyManagerMessage as PropertyManagerMessage
from openapi_client.models.property_message import PropertyMessage as PropertyMessage
from openapi_client.models.recurring_transaction_line_message import RecurringTransactionLineMessage as RecurringTransactionLineMessage
from openapi_client.models.recurring_transaction_line_post_message import RecurringTransactionLinePostMessage as RecurringTransactionLinePostMessage
from openapi_client.models.recurring_transaction_message import RecurringTransactionMessage as RecurringTransactionMessage
from openapi_client.models.rent_schedule_charge_post_message import RentScheduleChargePostMessage as RentScheduleChargePostMessage
from openapi_client.models.rent_schedule_charge_put_message import RentScheduleChargePutMessage as RentScheduleChargePutMessage
from openapi_client.models.rent_schedule_post_message import RentSchedulePostMessage as RentSchedulePostMessage
from openapi_client.models.rent_schedule_put_message import RentSchedulePutMessage as RentSchedulePutMessage
from openapi_client.models.rental_appliance_message import RentalApplianceMessage as RentalApplianceMessage
from openapi_client.models.rental_appliance_post_message import RentalAppliancePostMessage as RentalAppliancePostMessage
from openapi_client.models.rental_appliance_put_message import RentalAppliancePutMessage as RentalAppliancePutMessage
from openapi_client.models.rental_appliance_service_history_message import RentalApplianceServiceHistoryMessage as RentalApplianceServiceHistoryMessage
from openapi_client.models.rental_appliance_service_history_post_message import RentalApplianceServiceHistoryPostMessage as RentalApplianceServiceHistoryPostMessage
from openapi_client.models.rental_features_message import RentalFeaturesMessage as RentalFeaturesMessage
from openapi_client.models.rental_features_put_message import RentalFeaturesPutMessage as RentalFeaturesPutMessage
from openapi_client.models.rental_image_message import RentalImageMessage as RentalImageMessage
from openapi_client.models.rental_image_put_message import RentalImagePutMessage as RentalImagePutMessage
from openapi_client.models.rental_message import RentalMessage as RentalMessage
from openapi_client.models.rental_owner_contribution_data_message import RentalOwnerContributionDataMessage as RentalOwnerContributionDataMessage
from openapi_client.models.rental_owner_contribution_data_put_message import RentalOwnerContributionDataPutMessage as RentalOwnerContributionDataPutMessage
from openapi_client.models.rental_owner_contribution_message import RentalOwnerContributionMessage as RentalOwnerContributionMessage
from openapi_client.models.rental_owner_contribution_put_message import RentalOwnerContributionPutMessage as RentalOwnerContributionPutMessage
from openapi_client.models.rental_owner_contribution_reminder_message import RentalOwnerContributionReminderMessage as RentalOwnerContributionReminderMessage
from openapi_client.models.rental_owner_contribution_reminder_put_message import RentalOwnerContributionReminderPutMessage as RentalOwnerContributionReminderPutMessage
from openapi_client.models.rental_owner_message import RentalOwnerMessage as RentalOwnerMessage
from openapi_client.models.rental_owner_post_message import RentalOwnerPostMessage as RentalOwnerPostMessage
from openapi_client.models.rental_owner_put_message import RentalOwnerPutMessage as RentalOwnerPutMessage
from openapi_client.models.rental_owner_request_task_message import RentalOwnerRequestTaskMessage as RentalOwnerRequestTaskMessage
from openapi_client.models.rental_owner_request_task_post_message import RentalOwnerRequestTaskPostMessage as RentalOwnerRequestTaskPostMessage
from openapi_client.models.rental_owner_request_task_put_message import RentalOwnerRequestTaskPutMessage as RentalOwnerRequestTaskPutMessage
from openapi_client.models.rental_owner_tax_information_message import RentalOwnerTaxInformationMessage as RentalOwnerTaxInformationMessage
from openapi_client.models.rental_preferred_vendor_message import RentalPreferredVendorMessage as RentalPreferredVendorMessage
from openapi_client.models.rental_preferred_vendor_put_message import RentalPreferredVendorPutMessage as RentalPreferredVendorPutMessage
from openapi_client.models.rental_property_post_message import RentalPropertyPostMessage as RentalPropertyPostMessage
from openapi_client.models.rental_property_put_message import RentalPropertyPutMessage as RentalPropertyPutMessage
from openapi_client.models.rental_property_unit_post_message import RentalPropertyUnitPostMessage as RentalPropertyUnitPostMessage
from openapi_client.models.rental_tenant_post_message import RentalTenantPostMessage as RentalTenantPostMessage
from openapi_client.models.rental_tenant_put_message import RentalTenantPutMessage as RentalTenantPutMessage
from openapi_client.models.rental_tenant_renewal_post_message import RentalTenantRenewalPostMessage as RentalTenantRenewalPostMessage
from openapi_client.models.rental_unit_features_message import RentalUnitFeaturesMessage as RentalUnitFeaturesMessage
from openapi_client.models.rental_unit_features_put_message import RentalUnitFeaturesPutMessage as RentalUnitFeaturesPutMessage
from openapi_client.models.rental_unit_image_message import RentalUnitImageMessage as RentalUnitImageMessage
from openapi_client.models.rental_unit_image_put_message import RentalUnitImagePutMessage as RentalUnitImagePutMessage
from openapi_client.models.rental_unit_message import RentalUnitMessage as RentalUnitMessage
from openapi_client.models.rental_unit_put_message import RentalUnitPutMessage as RentalUnitPutMessage
from openapi_client.models.rental_units_post_message import RentalUnitsPostMessage as RentalUnitsPostMessage
from openapi_client.models.renters_insurance_policy_message import RentersInsurancePolicyMessage as RentersInsurancePolicyMessage
from openapi_client.models.requested_by_user_entity_message import RequestedByUserEntityMessage as RequestedByUserEntityMessage
from openapi_client.models.resident_center_user_message import ResidentCenterUserMessage as ResidentCenterUserMessage
from openapi_client.models.resident_center_user_reference_message import ResidentCenterUserReferenceMessage as ResidentCenterUserReferenceMessage
from openapi_client.models.resident_request_task_message import ResidentRequestTaskMessage as ResidentRequestTaskMessage
from openapi_client.models.resident_request_task_post_message import ResidentRequestTaskPostMessage as ResidentRequestTaskPostMessage
from openapi_client.models.resident_request_task_put_message import ResidentRequestTaskPutMessage as ResidentRequestTaskPutMessage
from openapi_client.models.retail_cash_property_message import RetailCashPropertyMessage as RetailCashPropertyMessage
from openapi_client.models.retail_cash_unit_message import RetailCashUnitMessage as RetailCashUnitMessage
from openapi_client.models.retail_cash_user_data_message import RetailCashUserDataMessage as RetailCashUserDataMessage
from openapi_client.models.retail_cash_user_message import RetailCashUserMessage as RetailCashUserMessage
from openapi_client.models.retail_cash_user_put_message import RetailCashUserPutMessage as RetailCashUserPutMessage
from openapi_client.models.save_address_message import SaveAddressMessage as SaveAddressMessage
from openapi_client.models.save_emergency_contact_message import SaveEmergencyContactMessage as SaveEmergencyContactMessage
from openapi_client.models.task_category_message import TaskCategoryMessage as TaskCategoryMessage
from openapi_client.models.task_category_put_message import TaskCategoryPutMessage as TaskCategoryPutMessage
from openapi_client.models.task_category_response_message import TaskCategoryResponseMessage as TaskCategoryResponseMessage
from openapi_client.models.task_category_save_message import TaskCategorySaveMessage as TaskCategorySaveMessage
from openapi_client.models.task_history_file_message import TaskHistoryFileMessage as TaskHistoryFileMessage
from openapi_client.models.task_history_file_upload_post_message import TaskHistoryFileUploadPostMessage as TaskHistoryFileUploadPostMessage
from openapi_client.models.task_history_message import TaskHistoryMessage as TaskHistoryMessage
from openapi_client.models.task_history_put_message import TaskHistoryPutMessage as TaskHistoryPutMessage
from openapi_client.models.task_history_user_message import TaskHistoryUserMessage as TaskHistoryUserMessage
from openapi_client.models.task_sub_category_message import TaskSubCategoryMessage as TaskSubCategoryMessage
from openapi_client.models.tax_information_post_message import TaxInformationPostMessage as TaxInformationPostMessage
from openapi_client.models.tax_information_save_message import TaxInformationSaveMessage as TaxInformationSaveMessage
from openapi_client.models.tenant_message import TenantMessage as TenantMessage
from openapi_client.models.to_do_task_message import ToDoTaskMessage as ToDoTaskMessage
from openapi_client.models.to_do_task_post_message import ToDoTaskPostMessage as ToDoTaskPostMessage
from openapi_client.models.to_do_task_put_message import ToDoTaskPutMessage as ToDoTaskPutMessage
from openapi_client.models.undeposited_funds_message import UndepositedFundsMessage as UndepositedFundsMessage
from openapi_client.models.unit_agreement_message import UnitAgreementMessage as UnitAgreementMessage
from openapi_client.models.unit_entity_message import UnitEntityMessage as UnitEntityMessage
from openapi_client.models.user_message import UserMessage as UserMessage
from openapi_client.models.user_role_message import UserRoleMessage as UserRoleMessage
from openapi_client.models.vehicle_message import VehicleMessage as VehicleMessage
from openapi_client.models.vendor_category_message import VendorCategoryMessage as VendorCategoryMessage
from openapi_client.models.vendor_category_save_message import VendorCategorySaveMessage as VendorCategorySaveMessage
from openapi_client.models.vendor_credit_line_item_message import VendorCreditLineItemMessage as VendorCreditLineItemMessage
from openapi_client.models.vendor_credit_line_item_post_message import VendorCreditLineItemPostMessage as VendorCreditLineItemPostMessage
from openapi_client.models.vendor_credit_message import VendorCreditMessage as VendorCreditMessage
from openapi_client.models.vendor_credit_post_message import VendorCreditPostMessage as VendorCreditPostMessage
from openapi_client.models.vendor_insurance_message import VendorInsuranceMessage as VendorInsuranceMessage
from openapi_client.models.vendor_insurance_save_message import VendorInsuranceSaveMessage as VendorInsuranceSaveMessage
from openapi_client.models.vendor_message import VendorMessage as VendorMessage
from openapi_client.models.vendor_post_message import VendorPostMessage as VendorPostMessage
from openapi_client.models.vendor_put_message import VendorPutMessage as VendorPutMessage
from openapi_client.models.vendor_refund_line_message import VendorRefundLineMessage as VendorRefundLineMessage
from openapi_client.models.vendor_refund_line_post_message import VendorRefundLinePostMessage as VendorRefundLinePostMessage
from openapi_client.models.vendor_refund_message import VendorRefundMessage as VendorRefundMessage
from openapi_client.models.vendor_refund_post_message import VendorRefundPostMessage as VendorRefundPostMessage
from openapi_client.models.vendor_tax_information_message import VendorTaxInformationMessage as VendorTaxInformationMessage
from openapi_client.models.vendor_transaction_message import VendorTransactionMessage as VendorTransactionMessage
from openapi_client.models.video_link_request_post_message import VideoLinkRequestPostMessage as VideoLinkRequestPostMessage
from openapi_client.models.work_order_entry_contact_message import WorkOrderEntryContactMessage as WorkOrderEntryContactMessage
from openapi_client.models.work_order_entry_contact_resource_message import WorkOrderEntryContactResourceMessage as WorkOrderEntryContactResourceMessage
from openapi_client.models.work_order_line_item_message import WorkOrderLineItemMessage as WorkOrderLineItemMessage
from openapi_client.models.work_order_line_item_save_message import WorkOrderLineItemSaveMessage as WorkOrderLineItemSaveMessage
from openapi_client.models.work_order_message import WorkOrderMessage as WorkOrderMessage
from openapi_client.models.work_order_post_message import WorkOrderPostMessage as WorkOrderPostMessage
from openapi_client.models.work_order_put_message import WorkOrderPutMessage as WorkOrderPutMessage
from openapi_client.models.work_order_task_message import WorkOrderTaskMessage as WorkOrderTaskMessage
from openapi_client.models.work_order_task_post_message import WorkOrderTaskPostMessage as WorkOrderTaskPostMessage

