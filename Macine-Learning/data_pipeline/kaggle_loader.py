import kaggle
from pathlib import Path
import logging

class KaggleLoader:
    """
    This module provides functionality to download and unzip Kaggle datasets.
    It uses the Kaggle API to authenticate and download datasets specified by their Kaggle IDs.
    """
    def __init__(self, dataset_name: str, download_path: Path):
        self.dataset_name = dataset_name
        self.download_path = download_path
        logging.info(f"KaggleLoader initialized for dataset: {self.dataset_name} at {self.download_path.resolve()}")
    
    """Load provides a place in which """
    def get_kaggle_data(self, dataset_name: str, download_path: Path):
        try:
            logging.info(f"Downloading and unzipping Kaggle dataset: {self.dataset_name} to {self.download_path.resolve()}")
        
            self.download_path.mkdir(parents=True, exist_ok=True)  # Ensure folder exists
        
            # Download and unzip dataset
            kaggle.api.authenticate()
            kaggle.api.dataset_download_files(self.dataset_name, path=str(self.download_path), unzip=True)
        
            logging.info("Download and unzip complete.")
        except Exception as e:
            logging.error(f"Error downloading dataset {self.dataset_name}: {e}")
            raise e

                  
        