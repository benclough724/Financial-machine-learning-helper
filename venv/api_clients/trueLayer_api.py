from dotenv import load_dotenv
import requests
import os
import pandas as pd
import json

load_dotenv()

#Retrieve OAuth 2.0 token
url = "https://auth.truelayer-sandbox.com/connect/token" #Move to init file for ASE principals

#Token request
#grant_type = "client_credentials" 
body = {
    "client_id": "sandbox-personalbankingautomation-12a075",
    "client_secret": "e71d46b5-b430-4831-907b-5e50a4f7c2ef",
    "scope": "accounts",
    "accept": "application/json"
    }



#Data API request
 #Fill with bearer token from the OAuth 2.0 token
"""headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjE0NTk4OUIwNTdDOUMzMzg0MDc4MDBBOEJBNkNCOUZFQjMzRTk1MTBSUzI1NiIsIng1dCI6IkZGbUpzRmZKd3poQWVBQ291bXk1X3JNLWxSQSIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJodHRwczovL2F1dGgudHJ1ZWxheWVyLXNhbmRib3guY29tIiwibmJmIjoxNzQyMDYzNDc2LCJpYXQiOjE3NDIwNjM0NzYsImV4cCI6MTc0MjA2NzA3NiwiYXVkIjoiZGF0YV9hcGkiLCJzY29wZSI6WyJhY2NvdW50cyJdLCJjbGllbnRfaWQiOiJzYW5kYm94LXBlcnNvbmFsYmFua2luZ2F1dG9tYXRpb24tMTJhMDc1IiwianRpIjoiNkNENTNENTE2MTgxMjc2RDM5OTkxMkMzNkVCN0ExMEIifQ.i-lQ1MpPcgEhjH8tJ8qi9I65QYhhKinPnMYy7YVin5In26ozog2XQSP3Iuv5wbAVfH3l29LUnmCdxSR5FAXnuMuyG9dm4mV2AW19sumXyJLBTUz0fT3zXSucBjblGjh4PTaXZLs-NthW6PZVcQMlrry1TB-B6oGUXz55ftYBN-HpttedQnko3DKd4rRbyGV6ojyc9nFRdqtgjlHc6e8BVRRqw-Q3O7sTlEOtRJ5lXS1BzurrV6ZTWBr6rPqKwljfqL0eopJUpRRQXx-NUiZXa1qKeB9yAY0jYnTuk4IWL76GtTdF5HoQEahZBc8KzP9aY7Mmp6VIjMo51nUsI9L4TA",
    
    } """



response = requests.get(url, body=body)

print(response.text)
return response

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


