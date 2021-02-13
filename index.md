## Welcome to PyPesa Official Documentation 

Hi guys welcome to PyPesa Package [Pypesa Documentation](https://kalebu.github.io/pypesa) 

# pypesa

Python wrapper on **Mpesa public API** for mobile Payment Integration made with care, this package is aimed to make integrating with Vodacom Mpesa Api as smooth as 
possible for newbie and Pro Devs.

(Transaction query) -> Pypesa -> Done  

Pypesa is an opensource project under MIT public license, the complete source code can be found at [pypesa](https://kalebu.github.io/pypesa), I welcome contributors to the package whether its a code or documentation you're warmly welcome. 

You can Take a look at [contributing.md](https://github.com/Kalebu/pypesa/blob/main/Contributing.md) for more guide on howto.


## Getting started 

To get started with the pypesa package firstly install the package using python *pip* just as illustrated below;

```bash
pip install pypesa
```
You can also install directly from github
install directly from github or use pip to install it.

```bash
$~ git clone https://github.com/Kalebu/pypesa
$~ cd pypesa
$ pypesa ~ python setup.py install 
```

## One More Step 

In order to able to integrate with Mpesa-Api you need an (api key) and (public key) from Vodacom, They offer two kinds of them one for Sandbox(Experimenting) and Production(Deployment).

Sandbox auth keys doesn't require you directly notifying physically Vodacom, you can sign up to the portal and get your keys instantly and start using them to architect your payment gateway.

When you wanna move to the Production, you just need to replace the sandbox authentication keys with Production keys but codebase stays the same.

Here is an article on how to easily get your authentication keys 
-> [Getting started with Mpesa Developer portal](https://dev.to/alphaolomi/getting-started-with-mpesa-developer-portal-46a4) 


## What Pypesa allows you to do ?

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
    2. Customer to Bussiness(C2B) Single Payment 
    3. Bussiness to Customer (B2C)
    4. Bussiness to Bussiness (B2B) 
    5. Payment Reversal
    6. Query Transaction status 
    7. Direct debit creation and Payment 


Authentication in Pypesa
------------------------

1. You need to have a json file named **keys.json** on your project directly 
  and then fill put in it your public and api keys in json format shown below 

  ```python

    {
     'api_key': 'xxx', 
     'public_key': 'xxxxxxxxxxxxxx' 
    }
  ```

2. Once done you're ready to go, just make sure you have active internet connection

### Example of Usage (Customer to Bussiness Transaction)

```python
>>>from pypesa import Mpesa
>>>mpesa = Mpesa()
>>>transaction_query = {"input_Amount": "10", 
                        "input_Country": "TZN", 
                        "input_Currency": "TZS", 
                        "input_CustomerMSISDN": "000000000001", 
                        "input_ServiceProviderCode": "000000", 
                        "input_ThirdPartyConversationID":'2edf7a0206d848f6b6fedea26accdc3a', 
                        "input_TransactionReference": 'T23434ZE5',
                        "input_PurchasedItemsDesc": "Python Book"
}
>>>mpesa.customer_to_bussiness(transaction_query)
Request processed successfully   INS-0
<Response [201]>
```

### Naming the authentication json
If you named your authentication json in other name than **keys** you might to 
specify it while creating an instance for mpesa just as shown below;

```python
>>>from pypesa import Mpesa
>>>mpesa = Mpesa(auth_path = filename)
``` 

## production environmnent

The package run by default using sandbox environmnent, If you wanna use it to real production
environmnent you can specify it while creating an instance as shown below 

```python
>>>from pypesa import Mpesa
>>>mpesa = Mpesa(environmnent="production")
```

## Contributing 

Wanna contribute ? then please [contributing.md](https://github.com/Kalebu/pypesa/blob/main/Contributing.md) to see how 


## Give it a star 

If you found this repository useful, give it a star 

You can also keep in touch with on [Twitter](https://twitter.com/j_kalebu).


## Bug bounty?

If you encounter **issue** with the usage of the package, feel free raise an **issue** so as 
we can fix it as soon as possible(ASAP) or just reach me directly through [email](isaackeinstein@gmail.com)

