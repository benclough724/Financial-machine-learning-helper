import requests
import os
from dotenv import load_dotenv

load_dotenv()

class BaseAPI: 
    
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key