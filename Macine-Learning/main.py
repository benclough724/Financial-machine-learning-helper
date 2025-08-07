# from pathlib import Path
from data_pipeline.data_loader import DataLoader
from data_pipeline.preprocess import PreprocessData
# from data_pipeline.feature_engineering import engineer_features
from config.datasets import KAGGLE_DATASETS
import traceback

# main pipeline for project

def main():
    """
    Main function to execute the data loading and preprocessing pipeline.
    This function initializes the data loader, retrieves datasets from Kaggle,
    """
    # call the data loader to download and unzip the dataset
    loader = DataLoader(KAGGLE_DATASETS)
    df_dict = loader.get_data()  # Load data from Kaggle datasets
    
    preprocessed_dfs = {}
    #print(df_dict.keys())
    for name, df in df_dict.items():
        df = df_dict['pat']
        df_processed = PreprocessData.preprocess_data(df)
        preprocessed_dfs[name] = df_processed
        print(each_df.head())
        PreprocessData.preprocess_data(df)
        
    
    # df = engineer_features(df)
    
    # df = models.LinearRegressionModel(df)

    
if __name__ == "__main__":
    main()
    
