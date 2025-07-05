from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI  
from pathlib import Path
from data_pipeline.kaggle import download_and_unzip_kaggle
from data_pipeline.data_loader import load_data
from data_pipeline.preprocess import preprocess_data
from data_pipeline.feature_engineering import engineer_features
from config.datasets import KAGGLE_DATASETS
import traceback

# main pipeline for project

# Download and unzip dataset if not already downloaded
def download_dataset():
    try:
        for key, dataset in KAGGLE_DATASETS.items():
            # print(f"{key=} => {dataset=}")q
            if not dataset["path"].exists():
                print(f"{dataset["path"].name} not found. Downloading dataset...")
                download_and_unzip_kaggle(dataset["kaggle_id"], dataset["path"]) # Uses names from the dictionary to find and download datasets from Kaggle          
            else:
                print(f"{dataset["path"].name} found. Skipping download.")

            #print(f"Preprocessed sample for {key}:\n{preprocessed}\n")
    except Exception as e: 
        print(f"Error downloading {dataset['kaggle_id']}: {str(e)}")
        traceback.print_exc()

def read_root():
    return {"message": "Welcome to the API!"}
    

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
    for key, dataset in KAGGLE_DATASETS.items():
        download_dataset()
        #get_raw_data(dataset['path'])
        get_processed_data(dataset['path'])

    
if __name__ == "__main__":
    main()
    
