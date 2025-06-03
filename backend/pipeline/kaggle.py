import kaggle

def download_and_unzip_kaggle(dataset_name: str, download_path: Path):
    # Use kaggle CLI with --unzip or download only then unzip manually
    kaggle.api.authenticate()

    # Download kaggle dataset and unzip
    kaggle.api.dataset_download_files('tharunprabu/my-expenses-data', path='./Datasets' ,unzip=True)
    pass