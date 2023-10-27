from contextlib import asynccontextmanager
from pathlib import Path

from config.config import params
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ml_workflow.model_predict import ModelPredict
from schemas.customer import Customer

current_directory = Path(__file__).parent
resource = {}

@asynccontextmanager
async def startup_event(_: FastAPI):
    resource['model_predict'] = ModelPredict(current_directory/'pipeline.pkl')
    yield
    resource.clear()

app = FastAPI(title=params['title'], lifespan=startup_event)

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
    prediction = resource['model_predict'].predict(customer)
    return {'prediction': prediction}