import kaggle
from pathlib import Path
import logging

"""
This module provides functionality to download and unzip Kaggle datasets.
It uses the Kaggle API to authenticate and download datasets specified by their Kaggle IDs.
"""
class KaggleLoader:
    def __init__(self, dataset_name: str, download_path: Path):
        self.dataset_name = dataset_name
        self.download_path = download_path
        logging.info(f"KaggleLoader initialized for dataset: {self.dataset_name} at {self.download_path.resolve()}")
    
    """Load provides a place in which """
    def load(self):
               
        try:
            download_and_unzip_kaggle(self.dataset_name, self.download_path)
            logging.info(f"Downloading and unzipping Kaggle dataset: {dataset_name} to {download_path.resolve()}")
        
            download_path.mkdir(parents=True, exist_ok=True)  # Ensure folder exists
            
            # Download and unzip dataset
            kaggle.api.authenticate()
            kaggle.api.dataset_download_files(dataset_name, path=str(download_path), unzip=True)
            
            logging.info("Download and unzip complete.")
        except Exception as e:
            logging.error(f"Error downloading dataset {self.dataset_name}: {e}")
            raise e

    def download_and_unzip_kaggle(dataset_name: str, download_path: Path):
                  
        