import pandas as pd
import numpy as np
import logging
from config.datasets import KAGGLE_DATASETS


def preprocess_all_datasets():
    """_summary_

    Returns:
        result: returns the result of the preprocessed dataset
    """
    results = {}
    for name, dataset in KAGGLE_DATASETS.items():
        try:
            print(f"Preprocessing: {name}")
            df = pd.read_csv(dataset["path"])
            preprocessed = preprocess_data(df)
            output_path = PREPROCESSED_DATA_DIR / f"{name}_preprocessed.csv"
            preprocessed.to_csv(output_path, index=False)
            results[name] = preprocessed
        except Exception as e:
            print(f"Error preprocessing {name}: {e}")
            results[name] = None
    return results

def preprocess_data(df):
    """Applies the preprocessing pipeline."""
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
    """Removes columns with only NaN values."""
    logging.info("Removing empty columns...")
    return df.dropna(axis=1, how='all')

def fill_missing_values(df, strategy='mean'):
    "Fills in missing values using mean averaging."
    logging.info(f"Filling missing values using strategy: {strategy}")
    
    # Loops amount of columns in database. Replaces all missing values.
    # Uses mean 
    for col in df.columns:
        if df[col].isnull().any():
            if strategy == 'mean' and pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].mean())
            elif strategy == 'median' and pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna('missing')
    return df

def encode_categoricals(df, encoding='one-hot'):
    """Encodes categorical variables."""
    logging.info(f"Encoding categorical variables using {encoding} encoding.")
    if encoding == 'one-hot':
        df = pd.get_dummies(df, drop_first=True)
    return df

def normalize_data(df, columns=None, method='z-score'):
    """Normalizes specified columns or all numerical columns."""
    logging.info(f"Normalizing data using {method} method.")
    if columns is None:
        columns = df.select_dtypes(include=np.number).columns
    for col in columns:
        if method == 'z-score':
            df[col] = (df[col] - df[col].mean()) / df[col].std()
        elif method == 'min-max':
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df


