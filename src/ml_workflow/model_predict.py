from pathlib import Path
from sklearn.pipeline import Pipeline
import pickle
import pandas as pd
from schemas.customer import Customer

class ModelPredict:
    def __init__(self, pipeline_path: Path) -> None:
        if not pipeline_path.exists():
            raise FileNotFoundError(f'Pipeline file not found: {pipeline_path}')    
        self.__pipeline = self.load_pipeline(pipeline_path)
        
    def load_pipeline(self, path: Path)-> Pipeline:
        with open(path, 'rb') as pkl_file:
            return pickle.load(pkl_file)
        
    def predict(self, customer: Customer)-> float:
        df_customer = pd.DataFrame(customer.model_dump(), index=[0])
        prediction = self.__pipeline.predict(df_customer)[0]
        return round(prediction, 3)