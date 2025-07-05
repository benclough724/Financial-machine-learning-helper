from pathlib import Path
from config.paths import RAW_DATA_DIR

'''
- This file contains the configuration for datasets used in the project.
- It includes the Kaggle dataset IDs and their corresponding local paths.
- To add a new dataset, simply append it to the KAGGLE_DATASETS dictionary
- with the appropriate keys: 'kaggle_id' and 'path'.'''
KAGGLE_DATASETS = {
    "expense_data": {
        "kaggle_id": "tharunprabu/my-expenses-data",
        "path": RAW_DATA_DIR / "expense_data_1.csv"
    },
}
