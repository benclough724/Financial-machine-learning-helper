from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI  
from pathlib import Path
from data_pipeline.kaggle import download_and_unzip_kaggle
from data_pipeline.data_loader import load_data
from data_pipeline.preprocess import preprocess_data
import traceback
from fastapi import HTTPException

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Or specify your frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

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
def get_user_data_choice():
    for path in kaggle_datasets:
        if not Path.exists:
            print(f"{Path.name} not found. Downloading dataset...")
            download_and_unzip_kaggle(kaggle_datasets[__name__], path.parent)

            
    else:
        print(f"{Path.name} found. Skipping download.")

#@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
    
# Get raw data and create REST API
#@app.get('/data/raw')
def get_raw_data():
    # return {"Hell: ben"} 
    df = load_data(CSV_FILE) # load datasets
    #simple_cols = []
    return df.head().to_dict("records")
    
# Get preprocessed data and create REST API
# 
#@app.get('/data/preprocessed')
def get_preprocessed_data():
    df = load_data(CSV_FILE) # load dataset
    df = preprocess_data(df) # preprocess dataset
    return df.head().to_dict('records')

    
if __name__ == "__main__":
    get_user_data_choice()
