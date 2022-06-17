class Required:
    """A class holding dictionaries of required fields
    for variety of transaction supported by pypesa.
    """
    re_customer_to_bussiness = {
        "input_Amount",
        "input_Country",
        "input_Currency",
        "input_CustomerMSISDN",
        "input_ServiceProviderCode",
        "input_ThirdPartyConversationID",
        "input_TransactionReference",
        "input_PurchasedItemsDesc",
    }

    re_bussiness_to_customer = {
        "input_Amount",
        "input_Country",
        "input_Currency",
        "input_CustomerMSISDN",
        "input_ServiceProviderCode",
        "input_ThirdPartyConversationID",
        "input_TransactionReference",
        "input_PaymentItemsDesc",
    }

    re_bussiness_to_bussiness = {
        "input_Amount",
        "input_Country",
        "input_Currency",
        "input_PrimaryPartyCode",
        "input_ReceiverPartyCode",
        "input_ThirdPartyConversationID",
        "input_TransactionReference",
        "input_PurchasedItemsDesc",
    }

    re_payment_reversal = {
        "input_Country",
        "input_ReversalAmount",
        "input_ServiceProviderCode",
        "input_ThirdPartyConversationID",
        "input_TransactionID",
    }

    re_transaction_status = {
        "input_Country",
        "input_QueryReference",
        "input_ServiceProviderCode",
        "input_ThirdPartyConversationID",
    }

    re_create_direct_debit = {
        "input_AgreedTC",
        "input_Country",
        "input_CustomerMSISDN",
        "input_EndRangeOfDays",
        "input_ExpiryDate",
        "input_FirstPaymentDate",
        "input_Frequency",
        "input_ServiceProviderCode",
        "input_StartRangeOfDays",
        "input_ThirdPartyConversationID",
        "input_ThirdPartyReference",
    }

    re_direct_debit_payment = {
        "input_Amount",
        "input_Country",
        "input_Currency",
        "input_CustomerMSISDN",
        "input_ServiceProviderCode",
        "input_ThirdPartyConversationID",
        "input_ThirdPartyReference",
    }


class Sandbox(Required):
    """Service URL to be used during sandbox Development.
    """

    def __init__(self) -> None:
        self.base_url = "https://openapi.m-pesa.com:443/sandbox/ipg/v2/vodacomTZN"

        self.session_id = f"{self.base_url}/getSession/"
        self.single_stage_c2b = f"{self.base_url}/c2bPayment/singleStage/"
        self.single_stage_b2c = f"{self.base_url}/b2cPayment/"
        self.single_stage_b2b = f"{self.base_url}/b2bPayment/"
    
        self.payment_reversal = f"{self.base_url}/reversal/"
        self.transaction_status = f"{self.base_url}/queryTransactionStatus/"

        self.direct_debit = f"{self.base_url}/directDebitCreation/"
        self.direct_debit_payment = f"{self.base_url}/directDebitPayment/"

    def __str__(self) -> str:
        return '<Using Sandbox Urls>'

    def __repr__(self) -> str:
        return '<Using Sandbox Urls>'


class Production(Required):
    """Service URL to be used for Production Development
    """

    def __init__(self) -> None:
        self.base_url = "https://openapi.m-pesa.com:443/openapi/ipg/v2/vodacomTZN"
        
        self.session_id = f"{self.base_url}/getSession/"
        self.single_stage_c2b = f"{self.base_url}/c2bPayment/singleStage/"
        self.single_stage_b2c = f"{self.base_url}/b2cPayment/"
        self.single_stage_b2b = f"{self.base_url}/b2bPayment/"

        self.payment_reversal = f"{self.base_url}/reversal/"
        self.transaction_status = f"{self.base_url}/queryTransactionStatus/"

        self.direct_debit = f"{self.base_url}/directDebitCreation/"
        self.direct_debit_payment = f"{self.base_url}/directDebitPayment/"

    def __str__(self) -> str:
        return '<Using Production Urls>'

    def __repr__(self) -> str:
        return '<Using Production Urls>'
