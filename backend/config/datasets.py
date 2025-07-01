from pathlib import Path
from config.paths import RAW_DATA_DIR

KAGGLE_DATASETS = {
    "expense_data": {
        "kaggle_id": "tharunprabu/my-expenses-data",
        "path": RAW_DATA_DIR / "expense_data_1.csv"
    },
    "budget_data": {
        "kaggle_id": "ismetsemedov/personal-budget-transactions-dataset",
        "path": RAW_DATA_DIR / "budget_data.csv"
    }
}
