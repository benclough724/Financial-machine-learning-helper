import pandas as pd
import numpy as np

def date_features(df, date_col='Date'):
    """Extracts useful time-based features from the date."""
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df['DayOfWeek'] = df[date_col].dt.dayofweek
    df['Day'] = df[date_col].dt.day
    df['Month'] = df[date_col].dt.month
    df['Year'] = df[date_col].dt.year
    df['IsWeekend'] = df[date_col].dt.dayofweek >= 5
    return df