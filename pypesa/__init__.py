"""
Python Package to Easy the Integration with Vodacom Public API
"""

import os
import json
import sys
import base64
import socket
import requests
from pathlib import Path
from .service_urls import sandbox, production
from typing import Optional, Union
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as rsa_cipher
from .mpesa_exceptions import AuthenticationError, LoadingKeyError, MpesaConnectionError


class Mpesa(object):

    __slots__ = [
        "auth_path",
        "auth_keys",
        "_encrypted_api_key",
        "_origin_ip",
        "urls",
    ]

    def __init__(
        self,
        auth_path: Optional[str] = "keys.json",
        environment: Optional[str] = "sandbox",
    ):
        """
        Mpesa API client for Python

        """
        self.auth_path = auth_path
        self.auth_keys = dict()
        self._encrypted_api_key = None
        self._origin_ip = "*"
        self.urls = production() if environment == "production" else sandbox()
        print(self.urls)

    @property
    def authenticate(self) -> bool:
        """
            Property to check If the user is has has included auth keys
            either manually or through auth json file(keys.json)

            >> import pypesa
            >> mpesa = pypesa()
            >> mpesa.authenticate

            Return True if the environment has auth keys
                   False if auth are not included
        """

        if self.auth_keys.get("public_key") and self.auth_keys.get("api_key"):
            self._encrypted_api_key = self.__generate_encrypted_key()
            return True

        elif os.path.isfile(self.auth_path):
            # print("loading from file")
            self.auth_keys = self.load_keys(self.auth_path)
            if self.auth_keys:
                self._encrypted_api_key = self.__generate_encrypted_key()
                return True
            return False

        else:
            return False

    def authenticated(method):
        def authorized_method(self, *args, **kwargs):
            if self.authenticate:
                return method(self, *args, **kwargs)
            else:
                raise AuthenticationError

        return authorized_method

    @staticmethod
    def load_keys(keys_filename: Union[str, Path]) -> dict:
        """
            Pypesa internal method to load the auth file 

                >> import pypesa
                >> mpesa = pypesa()
                >> pypesa.load_keys()

            Return keys Dict if auth file is present 

            Raise FileNotFoundError if auth file is absent
        """
        try:

            with open(keys_filename, "r") as auth:
                return json.load(auth)

        except FileNotFoundError:
            raise FileNotFoundError(
                f"{keys_filename} is not found on the current directory"
            )

        except Exception as bug:
            print(bug)
            raise LoadingKeyError

    def __generate_encrypted_key(self, session: Optional[bool] = False) -> str:
        """

            Method use to Encrypt the api key and public key 
            so as to get a secure RSA Encrypted key
        """
        try:
            pub_key = self.auth_keys.get("public_key")
            raw_key = self.auth_keys.get("api_key")

            if session:
                raw_key = self.get_session_id()

            public_key_string = base64.b64decode(pub_key)
            rsa_public_key = RSA.importKey(public_key_string)
            raw_cipher = rsa_cipher.new(rsa_public_key)
            encrypted_key = raw_cipher.encrypt(raw_key.encode())
            return base64.b64encode(encrypted_key).decode("utf-8")

        except Exception as bug:
            print(bug)
            """raise AuthenticationError(
                "Exceptions thrown while generating encrypted key\nPlease make sure you have the right public key"
            )"""

    @property
    def path_to_auth(self) -> str:
        """
            Return Path to Authentication file
        """
        return self.auth_path

    @path_to_auth.setter
    def path_to_auth(self, auth_path: Union[str, Path]) -> str:
        """
            Setting new path to the authentication file
        """
        if isinstance(auth_path, str):
            self.auth_path = auth_path
            return self.auth_path
        raise TypeError(
            f"Path to auth file must of type Path or String not {type(auth_path)}"
        )

    @property
    def environment(self) -> Union[sandbox, production]:
        """
            Return the Environment the Pypesa is running 

            whether its Sandbox | Production 
        """
        return self.urls

    @environment.setter
    def environment(self, enviro: str) -> Union[sandbox, production]:
        """
            Set new pypesa environment 

            Eg. changing env to production; 

            >> import pypesa
            >> mpesa = pypesa()
            >> mpesa.environment = "production"
            <Using Production Urls>
        """
        if isinstance(enviro, str):
            if enviro in ["sandbox", "production"]:
                if enviro == "sandbox":
                    self.urls = sandbox()
                else:
                    self.urls = production()
                print(self.urls)
                return self.urls
            raise ValueError(
                "Environment must be either sandbox or production")
        raise TypeError(
            f"environment must be of type string not {type(enviro)}")

    @property
    def api_key(self) -> str:
        '''
            Return current api key
        '''
        return self.auth_keys.get("api_key")

    @api_key.setter
    def api_key(self, Api_key: str) -> str:
        '''
            Use this propery to explicit set a api_key

            >> import pypesa
            >> wallet = pypesa()
            >> wallet.api_key = " Your api key" #here

        '''
        if isinstance(Api_key, str):
            self.auth_keys["api_key"] = Api_key
            return self.auth_keys["api_key"]
        raise TypeError(
            f"API key must be a of type String not {type(Api_key)}")

    @property
    def public_key(self) -> str:
        """
            Return the current Public key
        """
        return self.auth_keys.get("public_key")

    @public_key.setter
    def public_key(self, pb_key: str) -> str:
        """
            Set a new public key 
        """
        if isinstance(pb_key, str):
            self.auth_keys["public_key"] = pb_key
            return self.auth_keys["public_key"]
        raise TypeError(f"Public key must be a string not a {type(pb_key)}")

    @property
    def origin_address(self) -> str:
        """
            Return the current origin address
        """
        return self._origin_ip

    @origin_address.setter
    def origin_address(self, ip_address: str) -> str:
        """
            Set a new origin address 
        """
        if isinstance(ip_address, str):
            self._origin_ip = ip_address
            return self._origin_ip
        raise TypeError(
            f"Address must be of type string not {type(ip_address)}")

    @authenticated
    def default_headers(self, auth_key: Optional[str] = "") -> dict:
        """
            Generate Default header to be used during a Request

        """
        if not auth_key:
            auth_key = self.__generate_encrypted_key(session=True)
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(auth_key),
            "Host": "openapi.m-pesa.com",
            "Origin": self.origin_address,
        }

    @authenticated
    def get_session_id(self) -> str:
        try:
            headers = self.default_headers(auth_key=self._encrypted_api_key)
            response = requests.get(self.urls.session_id, headers=headers)
            response = response.json()
            session_id = response["output_SessionID"]
            response_code = response["output_ResponseCode"]
            description = response["output_ResponseDesc"]
            # print(description, " ", response_code)
            if response_code == "INS-989":
                # print("Session creation failed!!")
                raise AuthenticationError
            return session_id
        except Exception as bug:
            print(bug)
            raise AuthenticationError

    @staticmethod
    def verify_query(transaction_query: dict, required_fields: set) -> bool:
        """
        Raise KeyError if transaction query has a missing key

        """
        query_keys = set(transaction_query.keys())
        missing_keys = required_fields.difference(query_keys)
        if missing_keys:
            raise KeyError(
                "These keys {} are missing in your transaction query".format(
                    missing_keys
                )
            )
        return True

    @authenticated
    def customer_to_bussiness(self, transaction_query: dict) -> dict:
        """"""

        self.verify_query(transaction_query,
                          self.urls.re_customer_to_bussiness)

        try:
            return requests.post(
                self.urls.single_stage_c2b,
                json=transaction_query,
                headers=self.default_headers(),
                verify=True,
            ).json()

        except (requests.ConnectTimeout, requests.ConnectionError):
            raise MpesaConnectionError

    @authenticated
    def bussiness_to_customer(self, transaction_query: dict) -> dict:
        """"""

        self.verify_query(transaction_query,
                          self.urls.re_bussiness_to_customer)

        try:

            return requests.post(
                self.urls.single_stage_b2c,
                json=transaction_query,
                headers=self.default_headers(),
                verify=True,
            ).json()

        except (requests.ConnectTimeout, requests.ConnectionError):
            raise MpesaConnectionError

    @authenticated
    def bussiness_to_bussiness(self, transaction_query: dict) -> dict:
        """"""

        self.verify_query(transaction_query,
                          self.urls.re_bussiness_to_bussiness)

        try:
            return requests.post(
                self.urls.single_stage_b2b,
                json=transaction_query,
                headers=self.default_headers(),
                verify=True,
            ).json()

        except (requests.ConnectTimeout, requests.ConnectionError):
            raise MpesaConnectionError

    @authenticated
    def payment_reversal(self, transaction_query: dict) -> dict:
        """"""

        self.verify_query(transaction_query, self.urls.re_payment_reversal)

        try:
            return requests.put(
                self.urls.payment_reversal,
                json=transaction_query,
                headers=self.default_headers(),
                verify=True,
            ).json()

        except (requests.ConnectTimeout, requests.ConnectionError):
            raise MpesaConnectionError

    @authenticated
    def query_transaction_status(self, transaction_query: dict) -> dict:
        """"""

        self.verify_query(transaction_query, self.urls.re_transaction_status)

        try:
            return requests.get(
                self.urls.transaction_status,
                json=transaction_query,
                headers=self.default_headers(),
                verify=True,
            ).json()

        except (requests.ConnectTimeout, requests.ConnectionError):
            raise MpesaConnectionError

    @authenticated
    def create_direct_debit(self, transaction_query: dict) -> dict:
        """"""

        self.verify_query(transaction_query, self.urls.re_create_direct_debit)

        try:
            return requests.post(
                self.urls.direct_debit,
                json=transaction_query,
                headers=self.default_headers(),
                verify=True,
            ).json()

        except (requests.ConnectTimeout, requests.ConnectionError):
            raise MpesaConnectionError

    @authenticated
    def direct_debit_payment(self, transaction_query: dict) -> dict:
        """"""
        self.verify_query(transaction_query, self.urls.re_direct_debit_payment)

        try:
            return requests.post(
                self.urls.direct_debit_payment,
                json=transaction_query,
                headers=self.default_headers(),
                verify=True,
            ).json()
        except (requests.ConnectTimeout, requests.ConnectionError):
            raise MpesaConnectionError


sys.modules[__name__] = Mpesa
