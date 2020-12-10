import uuid 
import unittest
from pypesa import Mpesa 

class MpesaTest(unittest.TestCase):
    def setUp(self):
        self.mpesa = Mpesa()
        self.expected_output_keys = {
            'output_ResponseCode',
            'output_ResponseDesc',
            'output_TransactionID',
            'output_ConversationID',
            'output_ThirdPartyConversationID'
        }
        self.c2b_transaction_query = {
                "input_Amount": "10", 
                "input_Country": "TZN", 
                "input_Currency": "TZS", 
                "input_CustomerMSISDN": "000000000001", 
                "input_ServiceProviderCode": "000000", 
                "input_ThirdPartyConversationID":self.random_id, 
                "input_TransactionReference": 'T23434ZE5',
                "input_PurchasedItemsDesc": "Python Book"
        }

        self.b2c_transaction_query = {
                "input_Amount": "10", 
                "input_Country": "TZN", 
                "input_Currency": "TZS", 
                "input_CustomerMSISDN": "000000000001", 
                "input_ServiceProviderCode": "000000", 
                "input_ThirdPartyConversationID": self.random_id, 
                "input_TransactionReference": "T12344C",
                "input_PaymentItemsDesc": "Salary payment"
        }

        self.b2b_transaction_query = {
                "input_Amount": "10", 
                "input_Country": "TZN", 
                "input_Currency": "TZS", 
                "input_PrimaryPartyCode": "000000", 
                "input_ReceiverPartyCode": "000001", 
                "input_ThirdPartyConversationID": self.random_id, 
                "input_TransactionReference": "T12344C",
                "input_PurchasedItemsDesc": "Apartment"
        }

        self.payment_reversal_query = {
                "input_Country": "TZN", 
                "input_ReversalAmount": "25", 
                "input_ServiceProviderCode": "000000", 
                "input_ThirdPartyConversationID": self.random_id, 
                "input_TransactionID":  "0000000000001"
        }

        self.transaction_status_query = {
            "input_Country": "TZN",
            "input_QueryReference":"000000000000000000001" ,
            "input_ServiceProviderCode": "000000",
            "input_ThirdPartyConversationID": self.random_id
        }

    @property
    def random_id(self):
        unique_id = str(uuid.uuid4())
        unique_id = unique_id.replace('-', '')
        return unique_id

    def test_customer_to_bussiness(self):
        print('Testing customer_to_bussiness Feature')
        response = self.mpesa.customer_to_bussiness(self.c2b_transaction_query)
        response_keys = set(response.json().keys())
        self.assertEqual(response_keys, self.expected_output_keys)

    def test_bussiness_to_customer(self):
        print('Testing bussiness_to_customer Feature')
        response = self.mpesa.bussiness_to_customer(self.b2c_transaction_query)
        response_keys = set(response.json().keys())
        self.assertEqual(response_keys, self.expected_output_keys)
        print('Finished testing bussiness_to_customer Feature')

    def test_bussiness_to_bussiness(self):
        print('Testing bussiness_to_bussiness Feature')
        response = self.mpesa.bussiness_to_bussiness(self.b2b_transaction_query)
        response_keys = set(response.json().keys())
        self.assertEqual(response_keys, self.expected_output_keys)

    def test_payment_reversal(self):
        print('Testing payment Reversal Feature')
        response = self.mpesa.payment_reversal(self.payment_reversal_query)
        response_keys = set(response.json().keys())
        self.assertEqual(response_keys, self.expected_output_keys)
        print('Finished testing Payment reversal')

    def test_query_transaction_status(self):
        print('Testing query transaction status Feature')
        response = self.mpesa.query_transaction_status(self.transaction_status_query)
        response_keys = set(response.json().keys())
        self.assertEqual(response_keys, self.expected_output_keys)
        print('Finished Testing transaction status Feature')


if __name__ == "__main__":
    unittest.main()