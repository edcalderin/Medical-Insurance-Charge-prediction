include .env
export

start_server:
	cd backend_app && uvicorn --host=0.0.0.0 --port=8080 api:app

fetch_dataset:
	cd backend_app && python fetch_kaggle_dataset.py

train: fetch_dataset
	cd backend_app && python train.py

start_ui:
	cd streamlit_ui && streamlit run app.py

start_services:
	docker-compose up --build

ruff:
	ruff check backend_app/ frontend_streamlit/