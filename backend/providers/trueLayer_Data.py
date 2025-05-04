import requests
from truelayer_auth import TrueLayerAuth 

#Get the auth token from truelayer
auth = TrueLayerAuth()
access_token = auth.get_access_token()

class TrueLayerData:
   