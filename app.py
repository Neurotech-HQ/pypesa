from pypesa import Mpesa


pesa = Mpesa()


query_c2b = {
  "input_Amount": "10", 
  "input_Country": "TZN", 
  "input_Currency": "TZS", 
  "input_CustomerMSISDN": "000000000001", 
  "input_ServiceProviderCode": "000000", 
  "input_ThirdPartyConversationID": "asv02e5958774f7ba228d83d0d6891261", 
  "input_TransactionReference": 'T23434ZE5',
  "input_PurchasedItemsDesc": "Shoes"
}

something = pesa.customer_to_bussiness(query_c2b)
print(something.json())

query_b2c = {
    "input_Amount": "10", 
    "input_Country": "TZN", 
    "input_Currency": "TZS", 
    "input_CustomerMSISDN": "000000000001", 
    "input_ServiceProviderCode": "000000", 
    "input_ThirdPartyConversationID": "asv02e5958774f7ba228d83d0d689761", 
    "input_TransactionReference": "T12344C",
    "input_PaymentItemsDesc": "Salary payment"
}

b2c_result = pesa.bussiness_to_customer(query_b2c)
print(b2c_result.json())