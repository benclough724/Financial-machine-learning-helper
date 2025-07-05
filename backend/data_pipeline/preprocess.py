import pandas as pd
import numpy as np
import logging
from config.datasets import KAGGLE_DATASETS
from config.paths import PROCESSED_DATA_DIR

def preprocess_all_datasets():
    """_summary_

    Returns:
        result: returns the result of the preprocessed datasets
    """
    results = {}
    for name, dataset in KAGGLE_DATASETS.items():
        try:
            print(f"Preprocessing: {name}")
            df = pd.read_csv(dataset["path"])
            preprocessed = preprocess_data(df)
            output_path = PROCESSED_DATA_DIR / f"{name}_preprocessed.csv"
            preprocessed.to_csv(output_path, index=False)
            results[name] = preprocessed
            print(1)
        except Exception as e:
            print(f"Error preprocessing {name}: {e}")
            results[name] = None
    return results

def preprocess_data(df):
    """
    Applies the preprocessing pipeline.
    
    Function performs the following steps:
        1. Removes empty columns.
        2. Fills missing values using the specified strategy.
        3. Encodes categorical variables using one-hot encoding.
        4. Normalizes numerical data using z-score normalization.
    """
    df = remove_empty_columns(df)
    df = fill_missing_values(df)
    df = encode_categoricals(df)
    df = normalize_data(df)
    # df = convert_currency(df)
    # Move later test to see if add 
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


