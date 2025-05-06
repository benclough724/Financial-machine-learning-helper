# main.py

from trueLayer_auth import TrueLayerAuth
from trueLayer_data import TrueLayerDataAPI

if __name__ == "__main__":
    auth = TrueLayerAuth()
    token = auth.get_access_token()

    data_api = TrueLayerDataAPI(token)
    
    print("\nFetching accounts...")
    accounts = data_api.get_accounts()
    print(accounts)

    if accounts.get("results"):
        first_account_id = accounts["results"][0]["account_id"]

        print("\nFetching balance...")
        balance = data_api.get_balance(first_account_id)
        print(balance)

        print("\nFetching transactions...")
        transactions = data_api.get_transactions(first_account_id)
        print(transactions)
    else:
        print("No accounts available.")
