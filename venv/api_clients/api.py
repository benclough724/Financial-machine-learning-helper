from dotenv import load_dotenv
import requests
import os
import pandas as pd
import json

load_dotenv()


# Open banking project
API_URL = "https://apisandbox.openbankproject.com/obp/v4.0.0/banks"
response = requests.get(API_URL)
data = response.json() 

transactions = [
    {
        "transaction_id": t["id"],
        "account_id": t["this_account"]["id"],
        "bank_id": t["this_account"]["bank_id"],
        "amount": float(t["details"]["value"]["amount"]),
        "currency": t["details"]["value"]["currency"],
        "description": t["details"]["description"],
        "date": t["details"]["completed"]
    }
    for t in data.get("transactions", [])   
    # Ensure "transactions" key exists
]

# Convert to Pandas DataFrame
df = pd.DataFrame(transactions)

# Convert date to datetime format
#df["date"] = pd.to_datetime(df["date"])


print(json.dumps(data, indent=4))
print(df.head())  # Display first few rows


