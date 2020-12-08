
class sandbox:
    def __init__(self):
            
        """

        """    
        self.session_id = 'https://openapi.m-pesa.com/sandbox/ipg/v2/vodacomTZN/getSession/'

class production:
    def __init__(self):
        """

        """
        self.session_id = 'https://openapi.m-pesa.com/openapi/ipg/v2/vodacomTZN/getSession/'


if __name__ != '__main__':
    sandbox = sandbox()
    production = production()
