import logging
import os
from pathlib import Path

import pandas as pd
from config.config import params
from dotenv import load_dotenv
from feature_engine.encoding import OneHotEncoder
from feature_engine.imputation import CategoricalImputer
from ml_workflow.model_trainer import ModelTrainer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

load_dotenv()

N_SPLITS = int(os.getenv('N_SPLITS'))

current_directory = Path(__file__).parent

def split_dataset(csv_path: Path, random_state: int = 10)-> tuple:
    '''
    Returns X_train, X_test, y_train, y_test
    '''
    df = pd.read_csv(csv_path)
    X = df.drop('charges', axis=1)
    y = df.charges.values
    return train_test_split(X, y, test_size=.2, random_state=random_state)

def preprocess(X, y, params: dict)->pd.DataFrame:
    steps = [
        ('categorical imputer', CategoricalImputer(
            fill_value='Healthy', 
            variables=params['categorical_imputer_features'])
        ),
        ('ohe', OneHotEncoder(variables=params['ohe_features'], ignore_format=True))
    ]

    pipeline = Pipeline(steps)    
    return pipeline.fit_transform(X, y)
    
def train_model(params: dict):
    logging.info('splitting dataset...')
    X_train, X_test, y_train, y_test = split_dataset(current_directory/params['csv_name'])

    logging.info('preprocessing train dataset...')
    processed_full_train = preprocess(X_train, y_train, params)  
    
    modelTrainer = ModelTrainer(params)        
    modelTrainer.cross_validation_scores(processed_full_train, y_train, n_splits=N_SPLITS)
    modelTrainer.train(X_train, y_train)    
    modelTrainer.evaluate(X_test, y_test)    
    modelTrainer.persist_pipeline(current_directory/'pipeline.pkl')
    
if __name__ == '__main__':
    train_model(params)
