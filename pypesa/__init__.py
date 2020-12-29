import os
import json
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
        environment: Optional[str] = "testing",
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
        """"""

        if self.auth_keys.get("public_key") and self.auth_keys.get("api_key"):
            self._encrypted_api_key = self.__generate_encrypted_key()
            return True

        elif os.path.isfile(self.auth_path):
            print("loading from file")
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
        """"""
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
        """"""
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
        return self.auth_path

    @path_to_auth.setter
    def path_to_auth(self, auth_path: Union[str, Path]) -> str:
        if isinstance(auth_path, str):
            self.auth_path = auth_path
            return self.auth_path
        raise TypeError(
            f"Path to auth file must of type Path or String not {type(auth_path)}"
        )

    @property
    def environment(self) -> Union[sandbox, production]:
        return self.urls

    @environment.setter
    def environment(self, enviro: str) -> Union[sandbox, production]:
        if isinstance(enviro, str):
            if enviro in ["testing", "production"]:
                if enviro == "testing":
                    self.urls = sandbox()
                else:
                    self.urls = production()
                print(self.urls)
                return self.urls
            return ValueError("Environment must be either testing or production")
        return TypeError(f"environment must be of type string not {type(enviro)}")

    @property
    def api_key(self) -> str:
        return self.auth_keys["api_key"]

    @api_key.setter
    def api_key(self, Api_key: str) -> str:
        if isinstance(Api_key, str):
            self.auth_keys["api_key"] = Api_key
            return self.auth_keys["api_key"]
        raise TypeError(f"API key must be a of type String not {type(Api_key)}")

    @property
    def public_key(self) -> str:
        return self.auth_keys["public_key"]

    @public_key.setter
    def public_key(self, pb_key: str) -> str:
        if isinstance(pb_key, str):
            self.auth_keys["public_key"] = pb_key
            return self.auth_keys["public_key"]
        raise TypeError(f"Public key must be a string not a {type(pb_key)}")

    @property
    def origin_address(self) -> str:
        return self._origin_ip

    @origin_address.setter
    def origin_address(self, ip_address: str) -> str:
        if isinstance(ip_address, str):
            self._origin_ip = ip_address
            return self._origin_ip
        raise TypeError(f"Address must be of type string not {type(ip_address)}")

    @authenticated
    def default_headers(self, auth_key: Optional[str] = "") -> dict:
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
            print(description, " ", response_code)
            if response_code == "INS-989":
                print("Session creation failed!!")
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
            raise KeyError(
                "These keys {} are missing in your transaction query".format(
                    missing_keys
                )
            )
        return True

    @authenticated
    def customer_to_bussiness(self, transaction_query: dict) -> dict:
        """"""
        required_fields = {
            "input_Amount",
            "input_Country",
            "input_Currency",
            "input_CustomerMSISDN",
            "input_ServiceProviderCode",
            "input_ThirdPartyConversationID",
            "input_TransactionReference",
            "input_PurchasedItemsDesc",
        }

        self.verify_query(transaction_query, required_fields)
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
        required_fields = {
            "input_Amount",
            "input_Country",
            "input_Currency",
            "input_CustomerMSISDN",
            "input_ServiceProviderCode",
            "input_ThirdPartyConversationID",
            "input_TransactionReference",
            "input_PaymentItemsDesc",
        }

        self.verify_query(transaction_query, required_fields)

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
        required_fields = {
            "input_Amount",
            "input_Country",
            "input_Currency",
            "input_PrimaryPartyCode",
            "input_ReceiverPartyCode",
            "input_ThirdPartyConversationID",
            "input_TransactionReference",
            "input_PurchasedItemsDesc",
        }

        self.verify_query(transaction_query, required_fields)

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
        required_fields = {
            "input_Country",
            "input_ReversalAmount",
            "input_ServiceProviderCode",
            "input_ThirdPartyConversationID",
            "input_TransactionID",
        }

        self.verify_query(transaction_query, required_fields)

        try:
            return requests.post(
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
                verify=True,
            ).json()

        except (requests.ConnectTimeout, requests.ConnectionError):
            raise MpesaConnectionError
