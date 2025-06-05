import kaggle
from pathlib import Path
import logging

def download_and_unzip_kaggle(dataset_name: str, download_path: Path):
    logging.info(f"Downloading and unzipping Kaggle dataset: {dataset_name} to {download_path.resolve()}")
    
    download_path.mkdir(parents=True, exist_ok=True)  # Ensure folder exists
    
    # Download and unzip dataset
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_name, path=str(download_path), unzip=True)
    
    logging.info("Download and unzip complete.")