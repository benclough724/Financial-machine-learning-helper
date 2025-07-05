import kaggle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score 
import matplotlib.pyplot as plt

class LinearRegressionModel:
    def __init__(self, dataset_path: str):
        """
        Initializes the LinearRegressionModel with the dataset path.
        
        Parameters:
            dataset_path (str): Path to the dataset CSV file.
        """
        self.dataset_path = dataset_path
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    # def load_data(self):
    #     """
    #     Loads the dataset from the specified path and splits it into training and testing sets.
        
    #     Returns:
    #         pd.DataFrame: The loaded dataset.
    #     ""