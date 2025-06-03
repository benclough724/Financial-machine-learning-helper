from pathlib import Path
from pipeline.kaggle import download_and_unzip_kaggle
from pipeline.data_loader import load_data
from pipeline.preprocess import preprocess_data

BASE_DIR = Path(__file__).parent  # Directory where main.py is
DATA_DIR = BASE_DIR / "Datasets" # Dataset directory
CSV_FILE = DATA_DIR / "expense_data_1.csv"

# main pipeline for project
def main():
    # Download and unzip dataset if not already downloaded
    if not CSV_FILE.exists():
        print(f"{CSV_FILE} not found. Downloading dataset...")
        download_and_unzip_kaggle('tharunprabu/my-expenses-data', DATA_DIR)
    else:
        print(f"{CSV_FILE} found. Skipping download.")

    df = load_data(CSV_FILE) # load dataset
    df = preprocess_data(df) # preprocess dataset
    print(df.head())

if __name__ == "__main__":
    main()