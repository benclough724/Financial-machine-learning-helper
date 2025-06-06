from pathlib import Path
import os 
import matplotlib.pyplot as plt 
import pandas as pd


BASE_DIR = Path.cwd()  # Use os to get current working directory 


CSV_FILE = BASE_DIR / "Datasets" / "expense_data_1.csv" # path to database 
df = pd.read_csv(CSV_FILE) # place csv in data frame for EDA

plt.scatter(df['Amount'], df['Account.1'])
plt.xlabel("Amount")
plt.ylabel("Account")
plt.title("Scatter Plot of Amount vs Account")
plt.show()