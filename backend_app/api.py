from pathlib import Path

from config.config import params
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fetch_kaggle_dataset import FetchKaggleDataset
from ml_workflow.model_predict import ModelPredict
from schemas.customer import Customer

app = FastAPI(title=params['title'])

current_directory = Path(__file__).parent
modelPredict = ModelPredict(current_directory/'pipeline.pkl')

fetch_dataset = FetchKaggleDataset()
fetch_dataset.get_dataset()

@app.get('/', name='Welcome endpoint', description='Generates a HTML output')
def root():
    return HTMLResponse(
        '''
        <html>
            <h1>Medical Insurance Charges Prediction</h1>
            <p>Go to <a href=/docs>docs</a> to explore the swagger documentation</p>
        </html>
        ''')

@app.post('/predict', name='Prediction endpoint', description='Endpoint to make a prediction')
def predict(customer: Customer):
    prediction = modelPredict.predict(customer)
    return {'prediction': prediction}