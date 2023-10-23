from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile, BadZipFile
import os
import logging
from pathlib import Path
from config.config import params

logging.info('authenticating...')

current_directory = Path(__file__).parent

class FetchKaggleDataset:
    
    def __init__(self) -> None:
        self.api = self.__auth()
        self.params = params

    def __auth(self):
        api = KaggleApi()
        api.authenticate()
        return api
    
    def __exists_dataset(self):
        CSV_FILE = Path(current_directory/self.params['CSV_NAME'])        
        return CSV_FILE.exists()
            
    def __fetch_from_kaggle(self):    
        try:
            KAGGLE_DATASET: str = self.params["KAGGLE_DATASET"]
            
            logging.info(f'downloading dataset "{KAGGLE_DATASET}" from Kaggle')
            
            self.api.dataset_download_files(KAGGLE_DATASET)
            
            zip_filename = Path(KAGGLE_DATASET).name
            zip_filename = f'{zip_filename}.zip'
        
            logging.info('unzipping...')
            
            with ZipFile(current_directory/zip_filename) as file:
                file.extractall()
                csv_file = file.namelist()[0]

            os.remove(zip_filename)
            logging.info(f'dataset unzipped and saved in "{current_directory/csv_file}"')
        
        except BadZipFile:
            logging.error('Not a zip file or a corrupted zip file')
        except Exception as e:
            logging.error(f'Unexpected error {e}')

    def get_dataset(self):
        if self.__exists_dataset():
            logging.info(f'dataset with name "{current_directory/params["CSV_NAME"]}" already exists')
            return
        
        self.__fetch_from_kaggle()
        
if __name__ == "__main__":
    fetcher = FetchKaggleDataset()
    fetcher.get_dataset()