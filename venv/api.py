from dotenv import load_dotenv
import requests
import os
import pandas as pd

load_dotenv()


# Open banking project
API_URL = "https://apisandbox.openbankproject.com/obp/v4.0.0/banks"
response = requests.get(API_URL)
data = response.json() 


# Convert to Pandas DataFrame
df = pd.DataFrame(transactions)

# Convert date to datetime format
df["date"] = pd.to_datetime(df["date"])

print(df.head())  # Display first few rows



