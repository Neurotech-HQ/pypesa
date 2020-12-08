from pypesa import Mpesa


pesa = Mpesa()


query = {
  "input_Amount": "10", 
  "input_Country": "TZN", 
  "input_Currency": "TZS", 
  "input_CustomerMSISDN": "000000000001", 
  "input_ServiceProviderCode": "000000", 
  "input_ThirdPartyConversationID": "asv02e5958774f7ba228d83d0d6891261", 
  "input_TransactionReference": 'T23434ZE5',
  "input_PurchasedItemsDesc": "Shoes"
}


something = pesa.customer_to_bussiness(query)
print(something)