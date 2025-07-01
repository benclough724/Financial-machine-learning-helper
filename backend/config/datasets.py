from pathlib import Path
from config.paths import DATA_DIR

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
