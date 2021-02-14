## Welcome to PyPesa Official Documentation 

Hi welcome to Official PyPesa Documentation 

Pypesa is python wrapper on **Mpesa public API** for mobile Payment Integration made with care, this package is aimed to make integrating with Vodacom Mpesa Api as smooth as 
possible for newbie and Pro Devs.

Transaction query  ⮕  Pypesa  ⮕ Done  

### Opensource 

Pypesa is an opensource project under MIT public license, the complete source code can be found at [pypesa](https://kalebu.github.io/pypesa), I welcome contributors to the package whether its a code or documentation you're warmly welcome. 

You can Take a look at [contributing.md](https://github.com/Kalebu/pypesa/blob/main/Contributing.md) for more guide on howto.


## Getting started 

To get started with the pypesa package firstly install the package using python *pip* just as illustrated below;

```bash
pip install python-pesa
```

To make sure you install the latest version of Pypesa to keep yourself updated do this;
```bash
pip install --upgrade python-pesa
```

You can also install directly from github install directly from github just as shown below;

```bash
git clone https://github.com/Kalebu/pypesa
cd pypesa
pypesa-> python setup.py install 
```

## One More Step 

In order to able to integrate with Mpesa-Api you need an (api key) and (public key) from Vodacom, They offer two kinds of them one for Sandbox(Experimenting) and Production(Deployment).

If you already have them [Go to the next part](#what-pypesa-allows-you-to-do-?)

Sandbox auth keys doesn't require you directly notifying physically Vodacom, you can sign up to the portal and get your keys instantly and start using them to architect your payment gateway.

When you wanna move to the Production, you just need to replace the sandbox authentication keys with Production keys but codebase stays the same.

Here is an article on how to easily get your authentication keys 

[Getting started with Mpesa Developer portal](https://dev.to/alphaolomi/getting-started-with-mpesa-developer-portal-46a4) 


What Pypesa allows you to do ?
------------------------------

With Pypesa package you will be able to do the following kind of transaction 

- [x]  Customer to Bussiness (C2B) Single Payment 
- [x]  Bussiness to Customer (B2C)
- [x]  Bussiness to Bussiness (B2B) 
- [x]  Payment Reversal
- [x]  Query Transaction status 
- [x]  Direct debit creation and Payment


## Pypesa Usage 
Guide to usage of the Pypesa package 

Table of Content 
-----------------

1. [Authentication](#authentication-in-pypesa) 
2. [Customer to Bussiness(C2B) Single Payment](#customer-to-bussiness-in-pypesa) 
3. [Bussiness to Customer (B2C)](#bussiness-to-customer-in-pypesa)
4. [Bussiness to Bussiness (B2B)](#bussiness-to-bussiness-in-pypesa)
5. [Payment Reversal](#payment-reversal-in-pypesa)
6. [Query Transaction status](#query-transaction-status-in-pypesa) 
7. [Direct debit creation and Payment](#direct-debit-creation-and-payment) 
8. [Deployment to Production](#deployment-to-production)

Authentication in Pypesa
------------------------

Pypesa offers two distinct ways to authenticate your app

It all comes to you on which one you might find friendly and cool, personally I prefer putting them on separate file ([Using Json](#authentication-using-json)).

  - [Using Json](#authentication-using-json) 
  - [Including in your src code](#explicit-auth-within-source-code)

authentication using Json 
-------------------------

To authenticate your app using json, you need to have a json file named **keys.json** on your project directory and then add your public and api keys in json format shown below;

  ```python
    {
     'api_key': 'xxx', 
     'public_key': 'xxxxxxxxxxxxxx' 
    }
  ```

When you're done you can then get started with building your payment gateway with python, assumming your auth keys are valid.

```python
import pypesa
mpesa = pypesa()
```

If you named your authentication json in other name than **keys.json**,  you need to specify it while creating an instance for pypesa as shown below;

```python
import pypesa
mpesa = pypesa(auth_path = filename)
```

Note:
please Make sure you specify the correct path while while creating a pypesa instance 
otherwise Pypesa will raise **KeyError** 


Explicit auth within source code
--------------------------------
Apart from authenticating your python app using Json, you can also explicit specify the key in your code just as shown below;

```python
import pypesa 

mpesa = pypesa()

mpesa.api_key = "xxxxxxxxxxxxx"
mpesa.public_key ="xxxxxxxxxxxxx"
```

Note;

    Please Make sure you're keys are strings, pypesa will raise a TypeError() if you set it to other type than it.

⮕ [Back to the menu](#table-of-content)

Customer to Bussiness in Pypesa
-------------------------------------

The C2B API call is used as a standard customer-to-business transaction. Funds from the customer’s mobile money wallet will be deducted and be transferred to the mobile money wallet of the business. 

To authenticate and authorize this transaction, M-Pesa Payments Gateway will initiate a USSD Push message to the customer to gather and verify the mobile money PIN number. 

This number is not stored and is used only to authorize the transaction.

Use  *customer_to_bussiness()* method to process these kind of payments in Pypesa

As explained at the top, the journey to integrate is made smooth as possible, what you have to do is to prepare a *transaction_query{}* dictionary of the payment to be made and then do your transaction, just as illustrated in the example below;

```python
>> import pypesa 
>> mpesa = pypesa()
>> transaction_query = {
      "input_Amount": "10", 
      "input_Country": "TZN", 
      "input_Currency": "TZS", 
      "input_CustomerMSISDN": "000000000001", 
      "input_ServiceProviderCode": "000000", 
      "input_ThirdPartyConversationID":'2edf7a0206d848f6b6fedea26accdc3a', 
      "input_TransactionReference": 'T23434ZE5',
      "input_PurchasedItemsDesc": "Python Book"
  }
>> mpesa.customer_to_bussiness(transaction_query)

{'output_ResponseCode': 'INS-0', 'output_ResponseDesc': 'Request processed successfully', 'output_TransactionID': 'RvvsqB0rcP3Y', 'output_ConversationID': '1e029550d09745e7b2221bb4b2dc8ffc', 'output_ThirdPartyConversationID': '2edf7a0206d848f6b6fedea26accdc3a'}

```

Good news !! As we can see above, our payments was sucessfully processed by the sandbox. 

But you have to be carefully while writing your transaction_query by making sure all the neccessary keys are specified with their correct type.

### Pre-validation 

Pypesa do **pre-validation** before sending a request to vodacom openapi to ensure all the keys for particular transaction are present and it will raise **keyError** if any of the neccessary key is missing.  

For instance let's repeat doing the previous transaction but with a  a missing **input_PurchasedItemsDesc** field.

```python
>> import pypesa 
>> mpesa = pypesa()
>> transaction_query = {
      "input_Amount": "10", 
      "input_Country": "TZN", 
      "input_Currency": "TZS", 
      "input_CustomerMSISDN": "000000000001", 
      "input_ServiceProviderCode": "000000", 
      "input_ThirdPartyConversationID":'2edf7a0206d848f6b6fedea26accdc3a', 
      "input_TransactionReference": 'T23434ZE5',
  }
>> mpesa.customer_to_bussiness(transaction_query)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/kalebu/.local/lib/python3.8/site-packages/pypesa/__init__.py", line 77, in authorized_method
    return method(self, *args, **kwargs)
  File "/home/kalebu/.local/lib/python3.8/site-packages/pypesa/__init__.py", line 299, in customer_to_bussiness
    self.verify_query(transaction_query,
  File "/home/kalebu/.local/lib/python3.8/site-packages/pypesa/__init__.py", line 288, in verify_query
    raise KeyError(
KeyError: "These keys {'input_PurchasedItemsDesc'} are missing in your transaction query"

```

### Authentication Error 

Pypesa will does not verify your authentication instantly as you create a pypesa instance, instead it will verify them while submitting a request of particular transaction, so that means if you have put invalid api-key or public-key you will experience an **Authentication Error**

###  MpesaConnectionError

When you try to do a transaction without internet connection, pypesa will raise **MpesaConnectionError**, So make sure you have an active intenet connection when doing it so  

⮕ [Back to the menu](#table-of-content)

Bussiness to Customer in Pypesa
-------------------------------

The B2C API Call is used as a standard business-to-customer funds disbursement. Funds from the business account’s wallet will be deducted and paid to the mobile money wallet of the customer. Use cases for the B2C includes:
•	Salary payments 
•	Funds transfers from business
•	Charity pay-out

Use *bussiness_to_customer()* method to handle transaction from particular bussiness account to customers.

It's just samewise as how you would *customer_to_bussiness()* transaction, the only difference is the keys that needs to be specified while structuring a transaction_query.

Here is an example on how you would do that;

```python
>> import pypesa
>> mpesa = pypesa()
>> transaction_query = {
    'input_Amount': 250,
    'input_Country': 'TZN',
    'input_Currency': 'TZS',
    'input_CustomerMSISDN': '000000000001',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID':'f5e420e99594a9c496d8600',
    'input_TransactionReference': 'T12345C',
    'input_PaymentItemsDesc': 'Donation',
  }

>> mpesa.bussiness_to_customer(transaction_query)

{'output_ResponseCode': 'INS-0', 'output_ResponseDesc': 'Request processed successfully', 'output_TransactionID': 'sB3AXWzqXvfB', 'output_ConversationID': 'f971a34811784f939a61e9502ef1ffb2', 'output_ThirdPartyConversationID': 'f5e420e99594a9c496d8600'}

```
Done!! Just like we have already made our b2c transaction in a sandbox

*More description (Coming soon !!!)*

⮕ [Back to the menu](#table-of-content)

Bussiness to Bussiness in PyPesa
--------------------------------------

The B2B API Call is used for business-to-business transactions. Funds from the business’ mobile money wallet will be deducted and transferred to the mobile money wallet of the other business.

 Use cases for the B2C includes: 
    • Stock purchases 
    • Bill payment 
    • Ad-hoc payment

Use *bussiness_to_bussiness()* method while doing b2b transaction in Pypesa, 

Here is an example on how you would do that;

```python
>> import pypesa
>> mpesa = pypesa() 
>> transaction_query = {
      'input_Amount': 10,
      'input_Country': 'TZN',
      'input_Currency': 'TZS',
      'input_PrimaryPartyCode':'000000',
      'input_ReceiverPartyCode':'000001',
      'input_ServiceProviderCode': '000000',
      'input_ThirdPartyConversationID': '8a89835c71f15e99396',
      'input_TransactionReference': 'T1234C',
      'input_PurchasedItemsDesc': 'Shoes',
   }
>> mpesa.bussiness_to_bussiness(transaction_query) 

{'output_ResponseCode': 'INS-0', 'output_ResponseDesc': 'Request processed successfully', 'output_TransactionID': '4iUThBRRWXMG', 'output_ConversationID': 'f3ca96e7cb7f473a847247d8b887b922', 'output_ThirdPartyConversationID': '8a89835c71f15e99396'}

```

⮕ [Back to the menu](#table-of-content)

Payment Reversal in Pypesa
--------------------------
The Reversal API is used to reverse a successful transaction. Using the Transaction ID of a previously successful transaction,  the OpenAPI will withdraw the funds from the recipient party’s mobile money wallet and revert the funds to the mobile money wallet of the initiating party of the original transaction.

Use *payment_reversal()* method to reverse a transaction in pypesa, the most important thing to consider is the **output_TransactionID** of the previous transaction.

For instance if we take a look at json response of a previous b2b transaction we have done above illustrated below; 

```
{'output_ResponseCode': 'INS-0', 'output_ResponseDesc': 'Request processed successfully', 'output_TransactionID': '4iUThBRRWXMG', 'output_ConversationID': 'f3ca96e7cb7f473a847247d8b887b922', 'output_ThirdPartyConversationID': '8a89835c71f15e99396'}
```
 We can see the value of **output_TransactionID** to be **4iUThBRRWXMG**, Let's note that and use it reverse that transaction, If you had a different ID just do the same from json response of a transaction you would like to reverse;

 Our code to reverse it, would probably look like this;

```python
>> import pypesa
>> mpesa = pypesa()
>> transaction_query = {
      'input_ReversalAmount':10,
      'input_Country': 'TZN',
      'input_ServiceProviderCode': '000000',
      'input_ThirdPartyConversationID':'asvf7ba228d83d0d689761',
      'input_TransactionID':'4iUThBRRWXMG'
    }
>> mpesa.payment_reversal(transaction_query)

```

⮕ [Back to the menu](#table-of-content)


Query Transaction status in Pypesa
----------------------------------
The Query Transaction Status API call is used to query the status of the transaction that has been initiated.

Use *query_transaction_status()* to do this just as illustrated in the example below; 

Here also you can use your previous transaction ID as an input_QueryReference as to specify which transaction you wanna see it's status, 

```python
>> import pypesa
>> mpesa = pypesa()
>> transaction_query = {
      'input_QueryReference': '000000000000000000001',
      'input_ServiceProviderCode': '000000',
      'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
      'input_Country': 'TZN',
    }
>> mpesa.query_transaction_status(transaction_query)

```

⮕ [Back to the menu](#table-of-content)

Direct debit creation and Payment
---------------------------------
Direct Debits are payments in M-Pesa that are initiated by the Payee alone without any Payer interaction, but permission must first be granted by the Payer. The granted permission from the Payer to Payee is commonly termed a ‘Mandate’, and M-Pesa must hold details of this Mandate.

The Direct Debit API set allows an organisation to get the initial consent of their customers to create the Mandate that allows the organisation to debit customer's account at an agreed frequency and amount for services rendered. After the initial consent, the debit of the account will not involve any customer interaction. The Direct Debit feature makes use of the following API calls:
•	Create a Direct Debit mandate
•	Pay a mandate

The customer is able to view and cancel the Direct Debit mandate from G2 menu accessible via USSD menu or the Smartphone Application.

Use _create_direct_debit()_ method to create one in Pypesa as shown in the example below;

```python
>> import pypesa
>> mpesa = pypesa()
>> transaction_query = {
      "input_AgreedTC": "1",
      "input_Country": "TZN",
      "input_CustomerMSISDN": "000000000001",
      "input_EndRangeOfDays": "22",
      "input_ExpiryDate": "20211126",
      "input_FirstPaymentDate": "20160324",
      "input_Frequency": "06",
      "input_ServiceProviderCode": "000000",
      "input_StartRangeOfDays": "01",
      "input_ThirdPartyConversationID": "5334a912jbsj1j2kk1",
      "input_ThirdPartyReference": "3333",
    }
>> mpesa.create_direct_debit(transaction_query)

{'output_ResponseCode': 'INS-0', 'output_ResponseDesc': 'Request processed successfully', 'output_TransactionReference': '3333', 'output_ConversationID': '8eedbfb665284bdc9e5c548fa96e996a', 'output_ThirdPartyConversationID': '5334a912jbsj1j2kk1'}

```

⮕ [Back to the menu](#table-of-content)

Direct Debit Payment 
--------------------

Here an Pypesa example on how how you can do direct Debit Payment in Pypesa using the _direct debit payment()_;

```python
>> import pypesa
>> mpesa = pypesa()
>> transaction_query = {        
      "input_Amount": "10",
      "input_Country": "TZN",
      "input_Currency": "TZS",
      "input_CustomerMSISDN": "000000000001",
      "input_ServiceProviderCode": "000000",
      "input_ThirdPartyConversationID": "v2de053v4912jbasdj1j2kk",
      "input_ThirdPartyReference": "5db410b459bd433ca8e5"
    }
>> mpesa.direct_debit_payment(transaction_query)
{'output_ResponseCode': 'INS-0', 'output_ResponseDesc': 'Request processed successfully', 'output_TransactionID': 'js38ecMBpNoF', 'output_ConversationID': '263f515f8d464408b764b0f1bdbc0105', 'output_ThirdPartyConversationID': 'v2de053v4912jbasdj1j2kk'}

```
⮕ [Back to the menu](#table-of-content)

Deployment to Production 
------------------------

The package run by default using sandbox environmnent, If you wanna use it to real production environmnent you can specify it while creating an instance as shown below 

```python
>>>from pypesa import Mpesa
>>>mpesa = Mpesa(environmnent="production")
```

⮕ [Back to the menu](#table-of-content)


Related Projects 
  - [Pypesa](https://github.com/openpesa/pypesa) by [Openpesa](https://github.com/openpesa)
  - [Tigopesa-tanzania](https://github.com/dbrax/tigopesa-tanzania)
  - [Pesapal-laravel](https://github.com/dbrax/pesapal-laravel)
  - [Tigopesa Web Documentation](https://github.com/zechtz/tigoPesa)


References
  - [official Mpesa api Documentation](https://openapiportal.m-pesa.com/api-documentation)    
  - [Getting started with Mpesa Developer Portal](https://dev.to/alphaolomi/getting-started-with-mpesa-developer-portal-46a4)
  - [Pypesa](https://github.com/openpesa/pypesa) by [Openpesa](https://github.com/openpesa)



All the Credits to [kalebu](https://github.com/kalebu)