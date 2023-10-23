include .env
export

start_server:
	cd backend_app && bash start_server.sh

fetch_dataset:
	cd backend_app && python fetch_kaggle_dataset.py

train:
	export PYTHONPATH=.; cd backend_app && python ml_workflow/train.py

start_ui:
	cd streamlit_ui && streamlit run app.py

docker_compose:
	docker-compose up --build