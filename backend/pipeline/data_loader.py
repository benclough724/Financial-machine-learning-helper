import pandas as pd
import logging

def load_data(file_path):
    logging.info(f"Loading data from {file_path}")
    df = pd.read_csv(file_path)
    # Add preprocessing steps or call preprocess.py functions here
   