import pandas as pd
from pathlib import Path
from feature_engine.encoding import OneHotEncoder
from feature_engine.imputation import CategoricalImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from config.config import params
import logging
from model_trainer import ModelTrainer

current_directory = Path(__file__).parent
source_directory = current_directory.parent

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
            variables=params['CATEGORICAL_IMPUTER_FEATURES'])
        ),
        ('ohe', OneHotEncoder(variables=params['OHE_FEATURES'], ignore_format=True))
    ]

    pipeline = Pipeline(steps)    
    return pipeline.fit_transform(X, y)
    
def main(params: dict):
    logging.info('splitting dataset...')
    X_train, X_test, y_train, y_test = split_dataset(source_directory/params['CSV_NAME'])

    logging.info('preprocessing train dataset...')
    processed_full_train = preprocess(X_train, y_train, params)  
    
    modelTrainer = ModelTrainer(params)        
    modelTrainer.cross_validation_scores(processed_full_train, y_train)
    modelTrainer.train(X_train, y_train)    
    modelTrainer.evaluate(X_test, y_test)    
    modelTrainer.persist_pipeline(source_directory/'pipeline.pkl')
    
if __name__ == '__main__':
    main(params)
