import pandas as pd 
from forex_python.converter import CurrencyRates


c = CurrencyRates()

df = pd.read_csv('./expense_data_1.csv')

inr_to_gbp = c.get_rate('INR', 'GBP')


df['Amount'] = df['Amount'] * inr_to_gbp
df['Account.1'] = df['Account.1'] * inr_to_gbp


print(df.head())
