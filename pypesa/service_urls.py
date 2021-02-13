class Required(object):
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


class sandbox(Required):
    def __init__(self):
        """
        Service URL to be used during sandbox Development

        """
        self.session_id = (
            "https://openapi.m-pesa.com/sandbox/ipg/v2/vodacomTZN/getSession/"
        )
        self.single_stage_c2b = "https://openapi.m-pesa.com:443/sandbox/ipg/v2/vodacomTZN/c2bPayment/singleStage/"
        self.single_stage_b2c = (
            "https://openapi.m-pesa.com:443/sandbox/ipg/v2/vodacomTZN/b2cPayment/"
        )
        self.single_stage_b2b = (
            "https://openapi.m-pesa.com:443/sandbox/ipg/v2/vodacomTZN/b2bPayment/"
        )
        self.payment_reversal = (
            "https://openapi.m-pesa.com:433/sandbox/ipg/v2/vodacomTZN/reversal/"
        )
        self.transaction_status = "https://openapi.m-pesa.com:443/sandbox/ipg/v2/vodacomTZN/queryTransactionStatus/"

        self.direct_debit = "https://openapi.m-pesa.com:443/sandbox/ipg/v2/vodacomTZN/directDebitCreation/"

        self.direct_debit_payment = "https://openapi.m-pesa.com:443/sandbox/ipg/v2/vodacomTZN/directDebitPayment/"

    def __str__(self) -> str:
        return '<Using Sandbox Urls>'

    def __str__(self) -> str:
        return '<Using Sandbox Urls>'


class production(Required):
    def __init__(self):
        """

        Service URL to be used for Production Development

        """
        self.session_id = (
            "https://openapi.m-pesa.com/openapi/ipg/v2/vodacomTZN/getSession/"
        )
        self.single_stage_c2b = "https://openapi.m-pesa.com:443/openapi/ipg/v2/vodacomTZN/c2bPayment/singleStage/"
        self.single_stage_b2c = (
            "https://openapi.m-pesa.com:443//openapi/ipg/v2/vodacomTZN/b2cPayment/"
        )
        self.single_stage_b2b = (
            "https://openapi.m-pesa.com:443/openapi/ipg/v2/vodacomTZN/b2bPayment/"
        )
        self.payment_reversal = (
            "https://openapi.m-pesa.com:443/openapi/ipg/v2/vodacomTZN/reversal/"
        )
        self.transaction_status = "https://openapi.m-pesa.com:443/openapi/ipg/v2/vodacomTZN/queryTransactionStatus/"
        self.direct_debit = "https://openapi.m-pesa.com:443/openapi/ipg/v2/vodacomTZN/directDebitCreation/"
        self.direct_debit_payment = "https://openapi.m-pesa.com:443/openapi/ipg/v2/vodacomTZN/directDebitPayment/"

    def __str__(self) -> str:
        return '<Using Production Urls>'

    def __repr__(self) -> str:
        return '<Using Production Urls>'
