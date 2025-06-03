from pathlib import Path
from pipeline.unzip_kaggle import download_and_unzip_kaggle
from pipeline.data_loader import load_data

DATA_DIR = Path(__file__).parent / "Datasets"
CSV_FILE = DATA_DIR / "expense_data_1.csv"

def main():
    # Example: if you want to automate Kaggle download + unzip
    # download_and_unzip_kaggle("username/dataset-name", DATA_DIR)

    # Load and preprocess dataset
    X, y = load_data(CSV_FILE)

    # Proceed with training your logistic regression
    # from models.logistic_regression import train_model
    # model = train_model(X, y)

if __name__ == "__main__":
    main()
