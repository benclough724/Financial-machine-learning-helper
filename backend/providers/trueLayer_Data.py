# trueLayer_data.py

import requests

class TrueLayerDataAPI:
    def __init__(self, access_token):
        self.access_token = access_token
        print(access_token)
        self.base_url = "https://api.truelayer-sandbox.com"

    #Gets account data from True Layer
    def get_accounts(self):
        url = f"{self.base_url}/data/v1/accounts"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(url, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")  # See what was returned

        response.raise_for_status()  # Will throw an error for 4xx/5xx
        return response.json()

    # Get transaction data 
    def get_transactions(self, account_id):
        url = f"{self.base_url}/data/v1/accounts/{account_id}/transactions"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    #Get balance
    def get_balance(self, account_id):
        url = f"{self.base_url}/data/v1/accounts/{account_id}/balance"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

   