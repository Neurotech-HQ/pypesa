
class AuthenticationError(Exception):
    """
    Mpesa api Could'nt verify your keys 

    Please try entering again carefully

    >>mpesa = Mpesa(consumer_key = "xxxxxx",secret_key="xxxxx")


    """
    
    def __init__(self, error_message="Could not verify your authentication keys"):
        super().__init__(error_message)