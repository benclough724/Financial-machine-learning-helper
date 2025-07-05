import pandas as pd
import logging
from pathlib import Path
from config.datasets import KAGGLE_DATASETS
from data_pipeline.kaggle_loader import KaggleLoader
import traceback
from typing import List


class DataLoader(Exception):
      
    # add comments to the this function
    def __init__(self, KAGGLE_DATASETS: dict, message: str = "Data Loader initialised"): # Initializes the DataLoader class 
        self.KAGGLE_DATASETS = KAGGLE_DATASETS
        self.message = message
        logging.error(message)
    
    def get_data(self) -> List[pd.DataFrame]:
        """
        Loads data for financial datasets from Kaggle.
        Itterates through the KAGGLE_DATASETS dictionary, checks if the dataset file exists,
        and if not, downloads and unzips the dataset using the Kaggle API.
        If the file exists, it skips the download and proceeds to load the data into a DataFrame.
        Returns:
            pd.DataFrame: DataFrame containing the loaded dataset.
        """    
        try:
            for key, dataset in KAGGLE_DATASETS.items(): # Loops over each financial dataset in the KAGGLE_DATASETS dictionary
                dfList = {}
                file_path = dataset["path"] # Gets the path to the dataset from the dictionary
                if not file_path.exists(): # Checks if the file exists at the specified path
                    print(f"{dataset["path"].name} not found. Downloading dataset...")
                    KaggleLoader.get_kaggle_data(dataset["kaggle_id"], file_path) # Uses names from the dictionary to find and download datasets from Kaggle       
                     
                    
                else:
                    print(f"{file_path.name} found. Skipping download.") 
                    
                # Load the datasets into a list of DataFrames
                dfList[file_path] = pd.read_csv(file_path) # Reads the downloaded CSV file into a DataFrame
                print(dfList[file_path].head())
        except Exception as e: 
            print(f"Error downloading {dataset['kaggle_id']}: {str(e)}") # Log error to the console
            traceback.print_exc() # Display the full traceback for debugging

            # If the dataset file is not found after attempting to download, raise an error
            if not dataset["path"].exists():
                raise FileNotFoundError(f"Dataset {key} not found at {dataset['path']}. Please download it first.")
      
        
        
        # Add preprocessing here if needed
        
        return 


   