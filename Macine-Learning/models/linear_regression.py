import kaggle
import pandas as pd
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))  # Adjust path to include the parent directory
from data_pipeline.preprocess import PreprocessData
from data_pipeline.feature_engineering import FeatureEngineering
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score 
import matplotlib.pyplot as plt
 # Global variable for dataset path(change to modular structure later)

print("2")

class LinearRegressionModel:
    def __init__(self, dataset_path: str):
        """
        Initializes the LinearRegressionModel with the dataset path.
        
        Parameters:
            dataset_path (str): Path to the dataset CSV file.
        """
        dataset_path = "./data/unprocessed/expense_data_1.csv"  # Dataset path hard coded for now 
        
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        print("1")

    def load_data(self):
        """
        Loads the dataset from the specified path and splits it into training and testing sets.
        
        Returns:
            pd.DataFrame: The loaded dataset.
        """
        try:
            df = pd.read_csv(self.dataset_path)  # Load the dataset
            print(f"Dataset loaded successfully from {self.dataset_path}")
            print("After load_data:", type(df))
        except FileNotFoundError:
            print(f"Dataset not found at {self.dataset_path}. Please check the path.")
            
        return df
        
        # Split the dataset into features and target variable
        X = df.drop(columns=['target'])
        
    def train_test_split(self, test_size=0.2, random_state=42):
        """
        Splits the dataset into training and testing sets.
        
        Parameters:
            test_size (float): Proportion of the dataset to include in the test split.
            random_state (int): Controls the shuffling applied to the data before applying the split.
        
        Returns:
            tuple: X_train, X_test, y_train, y_test
        """
        
        X = self.X
        y = self.y
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        print("Data split into training and testing sets.")
        
    def linear_reg_pipeline(self):
        """
        Runs the linear regression pipeline.
        
        This method loads the data, splits it into training and testing sets,
        trains a linear regression model, evaluates it, and plots the results.
        """
        df = self.load_data() # First load the data into the project
        df = PreprocessData.preprocess_data(df) # Preprocess the data using the PreprocessData class
        df = FeatureEngineering.engineer_features(df) # Engineer features using the FeatureEngineering class
        print("Data loaded and preprocessed successfully.")
        print(df.head())