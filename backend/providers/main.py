import os 
import request

class main: 
    # import all environment variables
    def __init__(self):
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        redirect_URI = os.getenv("redirect_URI")
    
    def trueLayer_Auth():
        
