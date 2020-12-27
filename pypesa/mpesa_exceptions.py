key_format = {"api_key": "xxxxxxxxx", "public_key": "xxxxxxx"}


class AuthenticationError(Exception):
    """
    Mpesa api Could'nt verify your keys

    Please try entering again carefully

    """

    error_message = f"""
        Could not verify your authentication keys

        keys.json should be formatted as shown below 

            {key_format}
    """

    def __init__(self, error_message=error_message):
        super().__init__(error_message)


class LoadingKeyError(Exception):
    """

    Exception thrown while loading authentication keys

    """

    error_message = f"""

        Exception thrown while loading authentication keys from file 

        Please make sure you format correctly in json format as shown below 

            {key_format}
    """

    def __init__(self, error_message=error_message):
        super().__init__(error_message)


class MpesaConnectionError(Exception):
    """
    This is exception will be thrown where there is no or slow internet connection
    """

    error_message = f"""

    Transaction couldn\'t be processed due to connection timeout
    
    Please make sure you have a stable internet Connection 
    """

    def __init__(self, error_message=error_message):
        super().__init__(error_message)
