import pandas as pd
import logging
from pathlib import Path


def load_data(file_path: Path) -> pd.DataFrame:
    logging.info(f"Loading data from {file_path.resolve()}")
    
    if not file_path.exists():
        raise FileNotFoundError(f"File does not exist: {file_path.resolve()}")
    
    df = pd.read_csv(file_path)
    
    # Add preprocessing here if needed
    
    return df 
   