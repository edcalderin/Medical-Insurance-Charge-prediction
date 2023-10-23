from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ml_workflow.model_predict import ModelPredict
from schemas.customer import Customer
from fetch_kaggle_dataset import FetchKaggleDataset

app = FastAPI()

current_directory = Path(__file__).parent
modelPredict = ModelPredict(current_directory/'pipeline.pkl')

fetch_dataset = FetchKaggleDataset()
fetch_dataset.get_dataset()

@app.get('/')
def root():
    return HTMLResponse(
        '''
        <html>
            <h1>Medical Insurance Charges Prediction</h1>
            <p>Go to <a href=/docs>docs</a> to explore the swagger documentation</p>
        </html>
        ''')

@app.post('/predict')
def predict(customer: Customer):
    prediction = modelPredict.predict(customer)
    return {'prediction': prediction}