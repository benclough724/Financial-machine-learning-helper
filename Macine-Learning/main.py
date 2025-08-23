# from pathlib import Path
from data_pipeline.data_loader import DataLoader
from data_pipeline.preprocess import PreprocessData
from data_pipeline.feature_engineering import FeatureEngineering
from config.datasets import KAGGLE_DATASETS
import traceback
import pandas as pd

# main pipeline for project

def main():
    """
    Main function to execute the data loading and preprocessing pipeline.
    This function initializes the data loader, retrieves datasets from Kaggle,
    """
    
    
    
    #print(df_dict)

    # preprocessed_dfs = {}
    # #print(df_dict.keys())
    for name, dataset_info in KAGGLE_DATASETS.items():
        # print("this is name: " + name)
        # print("this is DF: " + str(df))
        loader = DataLoader(KAGGLE_DATASETS) # call the data loader to download and unzip the dataset
        #df = df_dict['path']
        df = loader.get_data(dataset_info["kaggle_id"], dataset_info["path"])  # Load data from Kaggle datasets
        #print(df.head())
        #df_dict = loader.get_data()  # Load data from Kaggle datasets
        
        #df_processed = PreprocessData.preprocess_data(df)
        #preprocessed_dfs[name] = df_processed
        #print(each_df.head())
        print("Raw: ")
        print(df.all())
        df = PreprocessData.preprocess_data(df, df)
        print("preprocess: ")
        print(df.all())

    
        df = FeatureEngineering.feature_engineering_pipeline(df, df)
        print("feature engineering: ")
        print(df.all())

        #df = models.LinearRegressionModel(df)

    
if __name__ == "__main__":
    main()
    
