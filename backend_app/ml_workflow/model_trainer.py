import logging
import pickle
from pathlib import Path

import pandas as pd
from feature_engine.encoding import OneHotEncoder
from feature_engine.imputation import CategoricalImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline


class ModelTrainer:
    def __init__(self, params: dict) -> None:
        self.params = params
        self.__pipeline = None
    
    def cross_validation_scores(self, X: pd.DataFrame, y: list, n_splits: int = 20):
        logging.warning(f'cross validation using {n_splits} folds')
        
        scoring = make_scorer(lambda y1, y2: mean_squared_error(y1, y2, squared=False))
        cv = KFold(n_splits=n_splits, shuffle=True, random_state=42)

        try:
            scores = cross_val_score(LinearRegression(), X, y, cv=cv, verbose=3, scoring=scoring)
            logging.info(f'RMSE scores -- mean: {scores.mean():.3f} +- std: {scores.std():.3f}')
        except Exception as e:
            logging.error(f'Cross-validation failed: {e}')    
        
    def train(self, X: pd.DataFrame, y: list):
        logging.info('tranining model...')
        
        if not self.__pipeline:
            self.__pipeline = Pipeline(steps=[
                ('categorical imputer', CategoricalImputer(fill_value='Healthy', 
                                                           variables=self.params['categorical_imputer_features'])),
                ('ohe', OneHotEncoder(variables=self.params['ohe_features'], ignore_format=True)),
                ('lr', LinearRegression(n_jobs=-1))
            ])

        self.__pipeline.fit(X, y)
        
    def evaluate(self, X_test: pd.DataFrame, y_test: list)-> float:
        
        if not self.__pipeline:
            logging.error('cannot evaluate the pipeline since it has not been trained yet')
            return
        
        logging.info('evaluating...')
        y_pred = self.__pipeline.predict(X_test)
        rmse = mean_squared_error(y_pred, y_test, squared=False)

        logging.info(f'Test RMSE: {rmse:.3f}')
        
        return rmse
    
    def persist_pipeline(self, path: Path):
        if not self.__pipeline:
            logging.error('cannot persist the pipeline since it has not been trained yet')
            return
            
        with open(path, 'wb') as pkl_file:
            pickle.dump(self.__pipeline, pkl_file)
            
        if path.exists():
            logging.warning(f'The file "{path}" already exists and will be overwritten')
        else:
            logging.info(f'model saved successfully in "{path}"')
