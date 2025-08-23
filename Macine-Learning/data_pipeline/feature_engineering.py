import pandas as pd
import numpy as np

"""
    FeatureEngineering class applies a series of transformations to a DataFrame to prepare it for analysis.
    It includes methods to clean the amount column, add date features, create rolling features,
    """
class FeatureEngineering:

    def feature_engineering_pipeline(self, df):
        """
        Applies the feature engineering pipeline.
        
        Function performs the following steps:
            1. Cleans the 'Amount' column by removing symbols and converting to float.
            2. Adds date features to the DataFrame.
            3. Adds rolling features based on 'Amount' and 'Date'.
            4. Converts 'Income' / 'Expense' to binary flag.
            5. Drops rows with missing required values.
        
        Parameters:
            df (pd.DataFrame): DataFrame containing the raw data.
        Returns:
            pd.DataFrame: DataFrame with engineered features.
        """
        # Apply feature engineering steps
        df = FeatureEngineering.clean_amount_column(df, 'Amount') # Clean the 'Amount' column by removing symbols and converting to float
        df = FeatureEngineering.date_features(df, 'Date') # Add date features to the DataFrame
        df = FeatureEngineering.rolling_features(df, 'Amount', 'Date') # Add rolling features based on
        df = FeatureEngineering.transaction_type_flag(df, 'TransactionType')

        # Drop rows with missing required values
        df = df.dropna(subset=['Amount', 'Date', 'IsIncome'])

        return df
    
    def date_features(self, df, date_col='Date'):    
        """
        Extracts useful time-based features from the date.
        
        Parameters:
            df (pd.DataFrame): DataFrame containing the date column.
            date_col (str): Name of the date column in the DataFrame.f
        Returns:
            pd.DataFrame: DataFrame with additional time-based features.
        Adds the following features:
            - DayOfWeek: Numeric representation of the day of the week (0=Monday, 6=Sunday).
            - Day: Day of the month.
            - Month: Month of the year.
            - Year: Year of the date.
            - IsWeekend: Boolean indicating if the date falls on a weekend (Saturday or Sunday).
        """
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce') # Date column --> datetime object
        df['DayOfWeek'] = df[date_col].dt.dayofweek # extract the day of the week
        df['Day'] = df[date_col].dt.day # extract day 
        df['Month'] = df[date_col].dt.month # extract month
        df['Year'] = df[date_col].dt.year # extract year 
        df['IsWeekend'] = df[date_col].dt.dayofweek >= 5 # adds boolean if transaction happened on a weekend
        return df


    def rolling_features(df, amount_col='Amount', date_col='Date'):
        """
        Adds rolling average/spending features based on amount.
        
        Parameters:
            df (pd.DataFrame): DataFrame containing the amount and date columns.
            amount_col (str): Name of the amount column in the DataFrame.
            date_col (str): Name of the date column in the DataFrame.
        """
        df = df.sort_values(by=date_col)
        df['RollingMean_3'] = df[amount_col].rolling(window=3, min_periods=1).mean()
        df['RollingStd_3'] = df[amount_col].rolling(window=3, min_periods=1).std().fillna(0)
        df['CumulativeSum'] = df[amount_col].cumsum()
        return df

    def transaction_type_flag(df, type_col='TransactionType'):
        """
        Converts 'Income' / 'Expense' to binary flag.
        
        Parameters:
            df (pd.DataFrame): DataFrame containing the transaction type column.
            type_col (str): Name of the transaction type column in the DataFrame.
        Returns:
            pd.DataFrame: DataFrame with an additional column 'IsIncome' where 'Income' is 1 and 'Expense' is 0."""
        df['IsIncome'] = df[type_col].str.lower().map({'income': 1, 'expense': 0})
        return df

    def clean_amount_column(df, amount_col='Amount'):
        """
        Removes symbols, commas, and converts amount to float.
        
        Parameters:
            df (pd.DataFrame): DataFrame containing the amount column.
            amount_col (str): Name of the amount column in the DataFrame.
        Returns:
            pd.DataFrame: DataFrame with the cleaned amount column.
        """
        df[amount_col] = df[amount_col].astype(str).str.replace('[^0-9.-]', '', regex=True)
        df[amount_col] = pd.to_numeric(df[amount_col], errors='coerce')
        return df

    
        