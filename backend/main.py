from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI  
from pathlib import Path
from backend.data_pipeline.kaggle_loader import download_and_unzip_kaggle
from data_pipeline.data_loader import load_data
from data_pipeline.preprocess import preprocess_data
from data_pipeline.feature_engineering import engineer_features
from config.datasets import KAGGLE_DATASETS
import traceback

# main pipeline for project

# Download and unzip dataset if not already downloaded
def download_dataset():
   

def get_raw_data(dataset_path):
    # return {"Hello: ben"} 
    df = load_data() # load datasets
    #simple_cols = []
    return df.head().to_dict("records")
    

def get_processed_data(dataset_path):
    print("this")
    # df = load_data(dataset) # load dataset
    df = preprocess_data(dataset_path) # preprocess dataset
    df = engineer_features(dataset_path)
    return df.head().to_dict('records')


def main():
    
    load_data()
    get_raw_data(dataset['path'])
    get_processed_data(dataset['path'])

    
if __name__ == "__main__":
    main()
    
