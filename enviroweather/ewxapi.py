
import requests
from os import path
import json
# create a config class that is a pydantic class

def host_exists(url):
    # strip path since path may be problematic
    base_url = path.dirname(url)



class EWXAPI():
    # class method: make from json config
    @classmethod
    def init_from_json_config(cls, ewx_api_config_json:str, ewx_env:str = 'production'):
        if json:
            try:
                ewx_api_config = json.loads(ewx_api_config_json)
            except json.decoder.JSONDecodeError: 
                raise ValueError("invalid JSON sent for configuration")
            
            return(cls.init(ewx_api_config,ewx_env))
        else:
            raise(ValueError("config str can't be empty"))

    @classmethod
    def init_from_config_file(cls, ewx_api_config_file:str, ewx_env:str = 'production' ):
        if not path.exists(ewx_api_config_file):
            raise ValueError(f"config file not found {ewx_api_config_file}")
        
        with open(ewx_api_config_file,"r") as f: 
            ewx_api_config  = json.load(f)
        
        return(cls.init(ewx_api_config,  ewx_env))

    # create attribs, default empty
    api_url = ""
    rm_api_url = ""
    anonymous_token = ""

    def __init__(self, ewx_api_config:dict[dict[str]],ewx_env:str = 'production'):
        self.ewx_env = ewx_env
        self.ewx_api_config = ewx_api_config
        self.set_urls(self.ewx_env)


    def set_urls(self, ewx_env:str):
        """used to set new URLs rather than creating new class"""
        self.ewx_env = ewx_env
        self.api_url = self.ewx_api_config[ewx_env]["api_url"]
        self.rm_api_url = self.ewx_api_config[ewx_env]["rm_api_url"] 
        # check them here and raise if not accessible


    def get_anonymous_token(self, reset_token:bool = False)->str:
        """using apis from config, contact the API to get an anonymous token
        Note that this method will be deprecated in 2027, and tokens are only available via log-in
        If a token already set in this object, don't get another one, unless rest
        Returns:
            str: string token to use for subsequent requests
        """

        # don't get a new one if you have one, saves on API traffic
        if self.anonymous_token and not reset_token:
            return self.anonymous_token
        
        token_url = f"{self.api_url}/db2/siteToken"
        token_response = requests.request(method='GET', url=token_url)
        token_response_data = token_response.json()
        if not(token_response_data["error"]):
            # if the data dict does not have a 'token' key, returns blank!
            # todo: check for token field in response data
            anonymous_token = token_response_data['data'].get('token')
        else:
            anonymous_token = ""
            Warning(f"error in response when acquiring token: {token_response.status}")

        # if the request failed, this will write an empty token to our saved one
        self.anonymous_token = anonymous_token
        return anonymous_token


    def login(self):
        Warning("login not implemented")
        return True
    