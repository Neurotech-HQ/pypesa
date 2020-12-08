import os 
import json
import base64
import socket
import requests
import service_urls
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as rsa_cipher
from .mpesa_exceptions import AuthenticationError

#tdWtOTaKSCVGDCoqKM4zqPgnM70IyVe6

class Mpesa:

    def __init__(self, auth_path = 'keys.json', environment='testing'):
        """
            Mpesa API client for Python 

        """
        self.auth_path = auth_path
        self.__encrypted_api_key = None
        self.__origin_ip = '127.0.0.1'
        self.urls = service_urls.production if environment == 'production' else service_urls.sandbox
        print(self.urls)
        if not self.authenticated:
            raise AuthenticationError
        print(self.get_session_id())

    @property
    def authenticated(self):
        """
    
        """
        if self.auth_path in os.listdir():
            auth_keys = self.__load_keys(self.auth_path)
            if auth_keys:
                self.__encrypted_api_key = self.__generate_encrypted_key(auth_keys)
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
    
    @staticmethod
    def __generate_encrypted_key(auth_keys:dict):
        """

        """
        try:
            public_key_string = base64.b64decode(auth_keys['public_key'])
            rsa_public_key = RSA.importKey(public_key_string)
            raw_cipher = rsa_cipher.new(rsa_public_key)
            encrypted_key = raw_cipher.encrypt(auth_keys['api_key'].encode())
            return base64.b64encode(encrypted_key)
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


    @property        
    def default_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.__encrypted_api_key.decode()), 
            'Origin' : self.origin_address
        }

    def get_session_id(self):
        try:
            response = requests.get(self.urls.session_id, headers=self.default_headers)
            response = response.json()
            session_id = response['output_SessionID']
            response_code = response['output_ResponseCode']
            description = response['output_ResponseDesc']
            print(description, ' ', response_code)
            return session_id
        except Exception as bug:
            print(bug)
            raise AuthenticationError

    def customer_to_bussiness(self):
        """

        """

        pass

    def bussiness_to_customer(self):
        """
        
        """
        pass

    def bussiness_to_bussiness(self):
        """

        """
        pass
    
    def payment_reversal(self):
        """

        """
        pass

    def query_transaction_status(self):
        """

        """
        pass

    def __del__(self):
        pass


