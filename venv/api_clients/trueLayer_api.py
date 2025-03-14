from dotenv import load_dotenv
import requests
import os
import pandas as pd
import json

load_dotenv()

#Retrieve OAuth 2.0 token
url = "https://auth.truelayer-sandbox.com/connect/token" #Move to init file for ASE principals
grant_type = "client_credentials" 
client_id = "sandbox-personalbankingautomation-12a075"
client_secret = "f62cf86a-b29d-490a-a25b-ea11a92cdd88"
scope = "accounts"

#Truelayer 


headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

# Open banking project
#API_URL = "https://apisandbox.openbankproject.com/obp/v4.0.0/banks"
#response = requests.get(API_URL)
#data = response.json() 


# Convert to Pandas DataFrame
#df = pd.DataFrame(transactions)

# Convert date to datetime format
#df["date"] = pd.to_datetime(df["date"])


#print(json.dumps(data, indent=4))
#print(df.head())  # Display first few rows


