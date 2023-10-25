include .env
export

start_server:
	cd backend_app && bash start_server.sh

fetch_dataset:
	cd backend_app && python fetch_kaggle_dataset.py

train: fetch_dataset
	export PYTHONPATH=.; cd backend_app && python train.py

start_ui:
	cd streamlit_ui && streamlit run app.py

start_services:
	docker-compose up --build

ruff:
	ruff check backend_app/ frontend_streamlit/