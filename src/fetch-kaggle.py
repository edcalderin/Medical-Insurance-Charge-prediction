from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile, BadZipFile
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

logging.info('authenticating...')

api = KaggleApi()
api.authenticate()

def fetch_dataset():
    KAGGLE_DATASET: str = 'sridharstreaks/insurance-data-for-machine-learning'
    
    logging.info(f'downloading dataset "{KAGGLE_DATASET}" from Kaggle')
    
    try:
        api.dataset_download_files(KAGGLE_DATASET)
        
        zip_filename = Path(KAGGLE_DATASET).name
        zip_filename = f'{zip_filename}.zip'
    
        logging.info('unzipping...')
        with ZipFile(Path(zip_filename)) as file:
            file.extractall()
            csv_file = file.namelist()[0]

        os.remove(zip_filename)
        logging.info(f'dataset unzipped and saved as "{csv_file}"')
    
    except BadZipFile:
        logging.error('Not a zip file or a corrupted zip file')
    except Exception as e:
        logging.error(f'Unexpected error {e}')

if __name__ == '__main__':
    fetch_dataset()