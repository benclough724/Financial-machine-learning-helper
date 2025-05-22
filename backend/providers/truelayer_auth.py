import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

Warning("1")

#class object that ensure token from true layer exists and is valid 
class TrueLayerAuth:
    Warning("2")
    
    # Contains True layer authentication and URL  
    def __init__(self):
        Warning("3")
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.token_url = "https://auth.truelayer-sandbox.com/connect/token"
        self.access_token = None
        self.token_expiry_time = 0  # Unix timestamp
        Warning("4")

    def get_access_token(self):
        # Only get new token if expired or not set
        if self.access_token is None or time.time() >= self.token_expiry_time:
            Warning("5")
            print("Fetching new access token...")
            payload = {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": "accounts"
            }
            headers = {
                "accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            print("Payload:", payload)

            response = requests.post(self.token_url, data=payload, headers=headers)

            if response.status_code == 200:
                data = response.json()
                self.access_token = data["access_token"]
                # Store expiry time in seconds from now
                self.token_expiry_time = time.time() + data["expires_in"]
                print(f"Access token retrieved. Expires in {data['expires_in']} seconds.")
            else:
                raise Exception(f"Failed to retrieve token: {response.status_code} - {response.text}")

        return self.access_token


     