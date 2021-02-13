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

### Table of Content 
1. [Authentication](#authentication-in-pypesa) 
2. [Customer to Bussiness(C2B) Single Payment](#customer-to-bussiness-(c2b)-in-pypesa) 
3. [Bussiness to Customer (B2C)](#bussiness-to-customer-(b2c)-in-pypesa)
4. [Bussiness to Bussiness (B2B)](#bussiness-to-bussiness-(b2b)-in-pypesa)
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

To authenticate your app using json, you need to have a json file named **keys.json** on your project directory and then fill put in it your public and api keys in json format shown below;

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


Customer to Bussiness (C2B) in Pypesa
-------------------------------------

```python
>> import pypesa 
>> mpesa = pypesa()
>> transaction_query = {"input_Amount": "10", 
                        "input_Country": "TZN", 
                        "input_Currency": "TZS", 
                        "input_CustomerMSISDN": "000000000001", 
                        "input_ServiceProviderCode": "000000", 
                        "input_ThirdPartyConversationID":'2edf7a0206d848f6b6fedea26accdc3a', 
                        "input_TransactionReference": 'T23434ZE5',
                        "input_PurchasedItemsDesc": "Python Book"
}
>> mpesa.customer_to_bussiness(transaction_query)
Request processed successfully   INS-0
<Response [201]>
```

Bussiness to Customer (B2C) in Pypesa
-------------------------------------
b2c docs here 


Bussiness to Bussiness (B2B) in PyPesa
--------------------------------------
b2b docs here 


Payment Reversal in Pypesa
--------------------------
payment reversal docs here 


Query Transaction status in Pypesa
----------------------------------
Query Transaction status docs here 


Direct debit creation and Payment
---------------------------------
direct debit create and payment docs here 


Deployment to Production 
------------------------
deployment to production docs here 


## production environmnent

The package run by default using sandbox environmnent, If you wanna use it to real production
environmnent you can specify it while creating an instance as shown below 

```python
>>>from pypesa import Mpesa
>>>mpesa = Mpesa(environmnent="production")
```

