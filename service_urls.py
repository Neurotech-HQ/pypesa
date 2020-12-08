
class sandbox:
    def __init__(self):
            
        """

        """    
        self.session_id = 'https://openapi.m-pesa.com/sandbox/ipg/v2/vodacomTZN/getSession/'
        self.single_stage_c2b = 'https://openapi.m-pesa.com:443/sandbox/ipg/v2/vodacomTZN/c2bPayment/singleStage/'
        self.single_stage_b2c = 'https://openapi.m-pesa.com:443/sandbox/ipg/v2/vodacomTZN/b2cPayment/'
        
class production:
    def __init__(self):
        """

        """
        self.session_id = 'https://openapi.m-pesa.com/openapi/ipg/v2/vodacomTZN/getSession/'
        self.single_stage_c2b = 'https://openapi.m-pesa.com/openapi/ipg/v2/vodacomTZN/c2bPayment/singleStage/'
        self.single_stage_b2c = 'https://openapi.m-pesa.com:443//openapi/ipg/v2/vodacomTZN/b2cPayment/'


if __name__ != '__main__':
    sandbox = sandbox()
    production = production()
