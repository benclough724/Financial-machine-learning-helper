import pandas as pd
import logging
from pathlib import Path
from config.datasets import KAGGLE_DATASETS
from backend.data_pipeline.kaggle_loader import download_and_unzip_kaggle
import traceback

"""Loads"""
class DataLoader(Exception):
            

    def __init__(self, KAGGLE_DATASETS: dict, message: str = "Data Loader initialised"): # Initializes the DataLoader class 
        self.KAGGLE_DATASETS = KAGGLE_DATASETS
        self.message = message
        logging.error(message)
    
    def get_data(self) -> pd.DataFrame:
        try:
            for key, dataset in KAGGLE_DATASETS.items(): # Loops over each financial dataset in the KAGGLE_DATASETS dictionary
                file_path = dataset["path"] # Gets the path to the dataset from the dictionary
                if not file_path.exists(): # Checks if the file exists at the specified path
                    print(f"{dataset["path"].name} not found. Downloading dataset...")
                    download_and_unzip_kaggle(dataset["kaggle_id"], file_path) # Uses names from the dictionary to find and download datasets from Kaggle          
                else:
                    print(f"{file_path.name} found. Skipping download.") 

            #print(f"Preprocessed sample for {key}:\n{preprocessed}\n")
        except Exception as e: 
            print(f"Error downloading {dataset['kaggle_id']}: {str(e)}") # Log error to the console
            traceback.print_exc() # Display the full traceback for debugging
    
            if not dataset["path"].exists():
                raise FileNotFoundError(f"Dataset {key} not found at {dataset['path']}. Please download it first.")
      
        df = pd.read_csv(file_path)
        
        # Add preprocessing here if needed
        
        return df 


   