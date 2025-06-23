import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files(name='tharunprabu/my-expenses-data', path='.', unzip=True)