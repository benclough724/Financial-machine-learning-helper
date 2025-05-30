import kaggle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
import matplotlib as plt


kaggle.api.authenticate()

# Download kaggle dataset and unzip
kaggle.api.dataset_download_files('tharunprabu/my-expenses-data', unzip=True)

df = pd.read_csv('./expense_data_1.csv')

print(df.columns)


plt.figure(figsize=(10,6))
plt.plot(df['Date'], df['Amount'])
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Amount Over Time')
plt.show()

#print("info:::", df.info())
#print("describe:::", df.describe())
#print("missing values", df.isnull().sum())  # Check for missing values
#print("Cols numbers:::", df.columns)