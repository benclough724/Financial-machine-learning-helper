# from pathlib import Path
from data_pipeline.data_loader import DataLoader
from data_pipeline.preprocess import PreprocessData
# from data_pipeline.feature_engineering import engineer_features
from config.datasets import KAGGLE_DATASETS
import traceback

# main pipeline for project

# Download and unzip dataset if not already downloaded   

# def get_raw_data(dataset_path):
#     # return {"Hello: ben"} 
#     df = load_data() # load datasets
#     #simple_cols = []
#     return df.head().to_dict("records")
    

# def get_processed_data(dataset_path):
#     print("this")
#     # df = load_data(dataset) # load dataset
#     df = preprocess_data(dataset_path) # preprocess dataset
#     df = engineer_features(dataset_path)
#     return df.head().to_dict('records')


def main():
    
    # call the data loader to download and unzip the dataset
    dfList{} = DataLoader(KAGGLE_DATASETS).get_data()  # Load data from Kaggle datasets
    
    df = PreprocessData.preprocess_data(df)
    
    # df = engineer_features(df)
    
    # df = models.LinearRegressionModel(df)

    
if __name__ == "__main__":
    main()
    
