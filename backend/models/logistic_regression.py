import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
import kagglehub

# Download latest version
path = kagglehub.dataset_download("tharunprabu/my-expenses-data")

print("Path to dataset files:", path)