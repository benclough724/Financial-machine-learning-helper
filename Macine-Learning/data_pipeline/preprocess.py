import pandas as pd
import numpy as np
import logging
from config.datasets import KAGGLE_DATASETS
from config.paths import PROCESSED_DATA_DIR

class PreprocessData:
    """
    PreprocessData class applies a series of transformations to a DataFrame to prepare it for analysis.
    It includes methods to remove empty columns, fill missing values, encode categorical variables,
    and normalize numerical data.
    """
    
    def __init__(self, df):
        """
        Runs the full preprocessing pipeline.
        
        Parameters:
            df (pd.DataFrame): DataFrame containing the raw data.
        Returns:
            pd.DataFrame: DataFrame with preprocessed data.
        """
        self.df = df.copy()  # Prevents modifying the original df

        # df = convert_currency(df)
        # Move later test to see if add 
    
        self.df = self.preprocess_data(self.df)  # Applies the preprocessing pipeline
    
    def preprocess_data(self, df):
        """
        Applies the preprocessing pipeline.
            
        Function performs the following steps:
            1. Removes empty columns.
            2. Fills missing values using the specified strategy.
            3. Encodes categorical variables using one-hot encoding.
            4. Normalizes numerical data using z-score normalization.
        Parameters:"""
        print(df.head())
        df = PreprocessData.remove_empty_columns(df)
        df = PreprocessData.fill_missing_values(df)
        df = PreprocessData.encode_categoricals(df)
        df = PreprocessData.normalize_data(df)
        return df
        
   

    #Potentially add probably not though(currency conversion)
    # def convert_currency(row, from_currency='INR', to_currency='USD'):
    #     try:
    #         return c.convert(from_currency, to_currency, row['Amount'])
    #     except:
    #         return None

    def remove_empty_columns(df):
        """
        Removes columns with only NaN values.
        
        Parameters:
            df (pd.DataFrame): DataFrame to preprocess.
        Returns:
            pd.DataFrame: DataFrame with empty columns removed.
        """
        logging.info("Removing empty columns...")
        return df.dropna(axis=1, how='all') # Drops entire column if all values are NaN

    def fill_missing_values(df, strategy='mean'):
        """
        Fills in missing values using specified strategy.
        
        Parameters:
            df (pd.DataFrame): DataFrame to preprocess.
            strategy (str): Strategy to fill missing values. 
            Options:
                'mean': Fill with column mean.
                'median': Fill with column median.
                'missing': Fill with 'missing' string.
        Returns:
            pd.DataFrame: DataFrame with missing values filled.
        """
        logging.info(f"Filling missing values using strategy: {strategy}")
        
        # Checks if strategy is valid. If not, raises ValueError.
        if strategy not in ['mean', 'median', 'missing']: # if more strategies are added, add them here
            raise ValueError("Strategy must be 'mean', 'median', or 'missing'")
        
        # Loops amount of columns in database. Replaces all missing values.
        for col in df.columns:
            if df[col].isnull().any():
                if strategy == 'mean' and pd.api.types.is_numeric_dtype(df[col]): # If column is numeric, fill with mean
                    df[col] = df[col].fillna(df[col].mean()) # Applies mean to column
                elif strategy == 'median' and pd.api.types.is_numeric_dtype(df[col]): # if column is numeric, fill with median
                    df[col] = df[col].fillna(df[col].median()) 
                else:
                    df[col] = df[col].fillna('missing')
        return df

    def encode_categoricals(df, encoding='one-hot'):
        """Encodes categorical variables.
        
        Parameters:
            df (pd.DataFrame): DataFrame to preprocess.
        encoding (str): Encoding method. Options:
            'one-hot': One-hot encoding.
            'label': Label encoding (not implemented).
        """
        
        if encoding not in ['one-hot']: # if more encoding strategies are added, add them here
            raise ValueError("encoding must be 'one-hot'") # Currently only one-hot encoding is implemented
        
        logging.info(f"Encoding categorical variables using {encoding} encoding.")
        if encoding == 'one-hot':
            df = pd.get_dummies(df, drop_first=True)
        return df
    
    def normalize_data(df, columns=None, method='z-score'):
        """Normalizes specified columns or all numerical columns.
        
        Parameters:
            df (pd.DataFrame): DataFrame to preprocess.
            columns (list): List of columns to normalize. If None, all numerical columns are normalized.
            method (str): Normalization method. Options:
                'z-score': Z-score normalization.
                'min-max': Min-max normalization.
        Returns:
            pd.DataFrame: DataFrame with normalized columns.
        """

        if method not in ['z-score', 'min-max' ]: # if more encoding strategies are added, add them here
            raise ValueError("encoding must be 'one-hot' 'min-max'") # Currently only one-hot encoding is implemented
        
        logging.info(f"Normalizing data using {method} method.")
        # 
        if columns is None: # Checks if columns is None, if so, selects all numerical columns
            columns = df.select_dtypes(include=np.number).columns # Selects all numerical columns in the DataFrame
        for col in columns: 
            if method == 'z-score':
                df[col] = (df[col] - df[col].mean()) / df[col].std() # Applies z-score normalization to column
            elif method == 'min-max':
                df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min()) # Applies min-max normalization to column
        return df


    
        
        