
class AuthenticationError(Exception):
    """
    Mpesa api Could'nt verify your keys 

    Please try entering again carefully

    """

    error_message = """

    Could not verify your authentication keys
    
    keys.json should be formatted as shown below 
    
    {
        'api_key' : 'xxxxxxxxx
        'public_key' : 'xxxxxxx', 
    }

    """
    
    def __init__(self, error_message=error_message):
        super().__init__(error_message)

