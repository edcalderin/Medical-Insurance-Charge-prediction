include .env
export

fetch_dataset:
	cd backend_app && python fetch_kaggle_dataset.py

train: fetch_dataset
	cd backend_app && python train.py

start_server: train
	cd backend_app && bash start_server.sh

start_ui:
	cd streamlit_ui && streamlit run app.py

## Build or up services
build_services:
	docker-compose up --build

up_services:
	docker-compose up

## Linter
ruff:
	ruff check backend_app/ frontend_streamlit/