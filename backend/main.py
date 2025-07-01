from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI  
from pathlib import Path
from data_pipeline.kaggle import download_and_unzip_kaggle
from data_pipeline.data_loader import load_data
from data_pipeline.preprocess import preprocess_data
import traceback
from fastapi import HTTPException

app = FastAPI()



# Define dataset info
DATA_DIR = Path(__file__).parent / "Datasets"
KAGGLE_DATASETS = {
    "expense_data": {
        "kaggle_id": "tharunprabu/my-expenses-data",
        "path": DATA_DIR / "expense_data_1.csv"
    },
    "budget_data": {
        "kaggle_id": "ismetsemedov/personal-budget-transactions-dataset",
        "path": DATA_DIR / "budget_data.csv"
    }
}


# main pipeline for project

# Download and unzip dataset if not already downloaded
def download_dataset():
    try:
        for key, dataset in KAGGLE_DATASETS.items():
            # print(f"{key=} => {dataset=}")q
            if not dataset["path"].exists():
                print(f"{dataset["path"].name} not found. Downloading dataset...")
                download_and_unzip_kaggle(dataset["kaggle_id"], dataset["path"])               
            else:
                print(f"{dataset["path"].name} found. Skipping download.")
            preprocess_data = get_preprocessed_data(dataset['path'])
            print(f"Preprocessed sample for {key}:\n{preprocessed}\n")
    except Exception as e: 
        print(f"Error downloading {dataset['kaggle_id']}: {str(e)}")
        traceback.print_exc()

#@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
    
# Get raw data and create REST API
#@app.get('/data/raw')
def get_raw_data():
    # return {"Hello: ben"} 
    df = load_data(KAGGLE_DATASETS) # load datasets
    #simple_cols = []
    return df.head().to_dict("records")
    
# Get preprocessed data and create REST API
# 
#@app.get('/data/preprocessed')
def get_preprocessed_data():
    df = load_data(datase) # load dataset
    df = preprocess_data(df) # preprocess dataset
    return df.head().to_dict('records')

    
if __name__ == "__main__":
    get_user_data_choice()
