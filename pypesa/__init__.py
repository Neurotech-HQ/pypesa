import os 
import json
import base64
import socket
import requests
from . import service_urls
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as rsa_cipher
from .mpesa_exceptions import AuthenticationError

class Mpesa:

    def __init__(self, auth_path = 'keys.json', environment='testing'):
        """
            Mpesa API client for Python 

        """
        self.auth_path = auth_path
        self.__encrypted_api_key = None
        self.__origin_ip = '*'
        self.urls = service_urls.production if environment == 'production' else service_urls.sandbox
        print(self.urls)
        if not self.authenticated:
            raise AuthenticationError


    @property
    def authenticated(self):
        """
    
        """
        if self.auth_path in os.listdir():
            self.auth_keys = self.__load_keys(self.auth_path)
            if self.auth_keys:
                self.__encrypted_api_key = self.__generate_encrypted_key()
                if self.__encrypted_api_key:
                    return True
            return False
        raise FileNotFoundError('{} is not found on your current directory\nPlease Create one as instructed'.format(self.auth_path))

 
    @staticmethod
    def __load_keys(keys_filename):
        try:
            with open(keys_filename, 'r') as auth:
                return json.load(auth)
        except Exception as bug:
            print(bug)
            return 
    
    def __generate_encrypted_key(self, session = False):
        """

        """
        try:
            pub_key = self.auth_keys['public_key']
            raw_key = self.auth_keys['api_key']
            if session:
                raw_key = self.get_session_id()
            public_key_string = base64.b64decode(pub_key)
            rsa_public_key = RSA.importKey(public_key_string)
            raw_cipher = rsa_cipher.new(rsa_public_key)
            encrypted_key = raw_cipher.encrypt(raw_key.encode())
            return base64.b64encode(encrypted_key).decode('utf-8')
        except Exception as bug:
            print(bug)
            return
    
    @property
    def origin_address(self):
        return self.__origin_ip

    @origin_address.setter
    def origin_address(self, ip_address):
        if isinstance(ip_address, str):
            try:
                if socket.inet_aton(ip_address):
                    self.__origin_ip = ip_address
                    return self.__origin_ip
            except OSError:
                raise ValueError('{} is invalid ip, please enter it again carefully')
        raise TypeError('Address must be string')

        
    def default_headers(self, auth_key=None):
        if not auth_key:
            auth_key = self.__generate_encrypted_key(session=True)
        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(auth_key),
            'Host': 'openapi.m-pesa.com',
            'Origin' : self.origin_address
        }

    def get_session_id(self):
        try:
            headers = self.default_headers(auth_key=self.__encrypted_api_key)
            response = requests.get(
                self.urls.session_id,
                headers=headers)
            response = response.json()
            session_id = response['output_SessionID']
            response_code = response['output_ResponseCode']
            description = response['output_ResponseDesc']
            print(description, ' ', response_code)
            if response_code == 'INS-989':
                print('Session creation failed!!')
                raise AuthenticationError
            return session_id
        except Exception as bug:
            print(bug)
            raise AuthenticationError

    
    @staticmethod
    def verify_query(transaction_query: dict, required_fields: set) -> bool:        
        query_keys = set(transaction_query.keys())
        missing_keys = required_fields.difference(query_keys)
        if missing_keys:
            raise KeyError('These keys {} are missing in your transaction query'.format(missing_keys))
        return True

    
    def customer_to_bussiness(self, transaction_query:dict):
        """

        """
        required_fields = {'input_Amount',
                           'input_Country',
                           'input_Currency',
                           'input_CustomerMSISDN',
                           'input_ServiceProviderCode',
                           'input_ThirdPartyConversationID',
                           'input_TransactionReference',
                           'input_PurchasedItemsDesc'
        }

        self.verify_query(transaction_query, required_fields)
        try:
            return requests.post(
                self.urls.single_stage_c2b,
                json = transaction_query,
                headers = self.default_headers(),
                verify = True
            )
        except requests.ConnectionError as bug:
            print(bug)
            print("Transaction could\'nt processed\nPlease check your network connection")
            return False      

    def bussiness_to_customer(self, transaction_query:dict):
        """
        
        """
        required_fields = {
            "input_Amount",
            "input_Country", 
            "input_Currency", 
            "input_CustomerMSISDN", 
            "input_ServiceProviderCode", 
            "input_ThirdPartyConversationID", 
            "input_TransactionReference",
            "input_PaymentItemsDesc"
        }

        self.verify_query(transaction_query, required_fields)
        try:
            return requests.post(
                self.urls.single_stage_b2c,
                json = transaction_query,
                headers = self.default_headers(),
                verify = True
            )
        except Exception as bug:
            print(bug)
            print('Failed to iniate Transaction\nPlease take a look at your internet connection')
            return False

    def bussiness_to_bussiness(self, transaction_query:dict):
        """

        """
        required_fields = {
            "input_Amount",
            "input_Country", 
            "input_Currency", 
            "input_PrimaryPartyCode", 
            "input_ReceiverPartyCode", 
            "input_ThirdPartyConversationID", 
            "input_TransactionReference",
            "input_PurchasedItemsDesc"
        }
    
        self.verify_query(transaction_query, required_fields)
        try:
            return requests.post(
                self.urls.single_stage_b2b,
                json=transaction_query,
                headers=self.default_headers(),
                verify=True
            )
        except Exception as bug:
            print(bug)
            print('Failed to initiate Transaction\nPlease take a loook at your internet connection')
            return False
    
    def payment_reversal(self, transaction_query:dict):
        """

        """
        required_fields = {
            "input_Country",
            "input_ReversalAmount", 
            "input_ServiceProviderCode", 
            "input_ThirdPartyConversationID", 
            "input_TransactionID"
        }

        self.verify_query(transaction_query, required_fields)
        try:
            return requests.post(
                self.urls.payment_reversal,
                json = transaction_query,
                headers = self.default_headers(),
                verify = True
            )
        except Exception as bug:
            print(bug)
            print('Payment Reversal Failed\nPlease make sure you have stable internet connection')
            return False

    def query_transaction_status(self, transaction_query:dict):
        """

        """
        required_fields = {
            "input_Country",
            "input_QueryReference",
            "input_ServiceProviderCode",
            "input_ThirdPartyConversationID", 
        }

        self.verify_query(transaction_query, required_fields)
        try:
            return requests.post(
                self.urls.transaction_status,
                json=transaction_query,
                headers=self.default_headers(),
                verify=True
            )
        except Exception as bug:
            print(bug)
            print('Exception thrown while querying transaction status\nPlease make sure you have a stable internet connection')
            return False