import kaggle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 


kaggle.api.authenticate()


# Download latest version
kaggle.api.dataset_download_files('tharunprabu/my-expenses-data', unzip=True)

print("Path to dataset files:", path)