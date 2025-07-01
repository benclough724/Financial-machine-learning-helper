import pandas as pd
import numpy as np

def date_features(df, date_col='Date'):
    """Extracts useful time-based features from the date."""
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce') # Date column --> datetime object
    df['DayOfWeek'] = df[date_col].dt.dayofweek # extract the day of the week
    df['Day'] = df[date_col].dt.day # extract day 
    df['Month'] = df[date_col].dt.month # extract month
    df['Year'] = df[date_col].dt.year # extract year 
    df['IsWeekend'] = df[date_col].dt.dayofweek >= 5 # adds boolean if transaction happened on a weekend
    return df


def rolling_features(df, amount_col='Amount', date_col='Date'):
    """Adds rolling average/spending features based on amount."""
    df = df.sort_values(by=date_col)
    df['RollingMean_3'] = df[amount_col].rolling(window=3, min_periods=1).mean()
    df['RollingStd_3'] = df[amount_col].rolling(window=3, min_periods=1).std().fillna(0)
    df['CumulativeSum'] = df[amount_col].cumsum()
    return df

def add_transaction_type_flag(df, type_col='TransactionType'):
    """Converts 'Income' / 'Expense' to binary flag."""
    df['IsIncome'] = df[type_col].str.lower().map({'income': 1, 'expense': 0})
    return df

def clean_amount_column(df, amount_col='Amount'):
    """Removes symbols, commas, and converts amount to float."""
    df[amount_col] = df[amount_col].astype(str).str.replace('[^0-9.-]', '', regex=True)
    df[amount_col] = pd.to_numeric(df[amount_col], errors='coerce')
    return df

def engineer_features(df):
    """Runs the full feature engineering pipeline."""
    df = clean_amount_column(df, 'Amount')
    df = add_date_features(df, 'Date')
    df = add_transaction_type_flag(df, 'TransactionType')
    df = add_rolling_features(df, 'Amount', 'Date')

    # Drop rows with missing required values
    df = df.dropna(subset=['Amount', 'Date', 'IsIncome'])

    return df