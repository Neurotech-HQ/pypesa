import requests
from .mpesa_exceptions import AuthenticationError

#tdWtOTaKSCVGDCoqKM4zqPgnM70IyVe6

class Mpesa:

    def __init__(self, consumer_key: str, secret_key: str):
        """
            Mpesa API client for Python 

        """
        
        self.__consumer_key = consumer_key
        self.__secret_key = secret_key

        if not self.__authenticated:
            raise AuthenticationError

    @property
    def __authenticated(self):
        """
    
        """
        return True

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
