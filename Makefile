include .env
export

start_server:
	cd src && bash scripts/start_server.sh

fetch_dataset:
	cd src && python fetch_kaggle_dataset.py

train:
	export PYTHONPATH=.; cd src && python ml_workflow/train.py