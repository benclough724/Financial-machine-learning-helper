from dotenv import load_dotenv
import requests
import os
import pandas as pd
import json

load_dotenv()

accessToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjE0NTk4OUIwNTdDOUMzMzg0MDc4MDBBOEJBNkNCOUZFQjMzRTk1MTBSUzI1NiIsIng1dCI6IkZGbUpzRmZKd3poQWVBQ291bXk1X3JNLWxSQSIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJodHRwczovL2F1dGgudHJ1ZWxheWVyLXNhbmRib3guY29tIiwibmJmIjoxNzQzMjY4NjM5LCJpYXQiOjE3NDMyNjg2MzksImV4cCI6MTc0MzI3MjIzOSwiYXVkIjoiZGF0YV9hcGkiLCJzY29wZSI6WyJhY2NvdW50cyJdLCJjbGllbnRfaWQiOiJzYW5kYm94LXBlcnNvbmFsYmFua2luZ2F1dG9tYXRpb24tMTJhMDc1IiwianRpIjoiNDMzMTFGMEQ1QTU2QkQ4OEQ2MkFCMzExNzJCMDdDMEEifQ.TH8c0GN8pPvGOmdG8h-QmlgLXcJhe0KbsQb9Un9023STI0NRaHX1SmMwBSAUdfmb4WmpBbYMndvfCHDUPiSsbDHsHYU5zjHUSEoqfnkhM1MxSjXH8bjkPkrcXUfTmzA-qQytTqVRW0bMMdEtMeOnAIYneOm7dP3ZCyx0zeEFYxYXJvEZC2JAJSfjs57g0FuF2ooO2ZL7yhC99GcWA3MO3YEBynl3P_AyHPZ2cDeauatJuqNqqCHRDoA0L4-pqWp41er3cPyDjy-_zk4kosuXhrZinJtzTJ4q1JmR_KVX4m480PSRCv52_2DxNZge_omFe06q7hufHVYmrJaGjuvaiw"
#Retrieve OAuth 2.0 token
tokenUrl = "https://auth.truelayer-sandbox.com/connect/token" #Move to init file for ASE principals
acctUrl = "https://api.truelayer-sandbox.com/data/v2/accounts" #True Layer account data endpoint 

#Token request
tokenBody  = {
    "grant_type": "client_credentials",
    "client_id": "sandbox-personalbankingautomation-12a075",
    "client_secret": "e71d46b5-b430-4831-907b-5e50a4f7c2ef",
    "scope": "accounts",
    "accept": "application/json"
    }


#response = requests.post(tokenUrl, data = tokenBody )
print(response.text)

'''acctBody = {
    "Authorization": "Bearer "
}'''

#Data API request
 #Fill with bearer token from the OAuth 2.0 token
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {accessToken}",
    
    }







#print(response.text)


