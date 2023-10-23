# Medical Insurance Prediction
*Machine Learning Zoomcap Mid-term project*

## Problem description


## Directory layout
```
.
├── .github                          # CI/CD workflows
├── config/                          # Config files
├── images/                          # Assets
├── notebooks/                       # Notebooks used to explore data and select the best model
├── scripts/                         # Bash scripts
├── streaming/                       # Directory for handling streaming dataastAPI directoryF
|   ├── lambda_function.py           # Entrypoint for the application
|   ├── model.py                     # Functions and classes related to the model
├── streamlit/                       # User Interface built on Streamlit to interact with the model
├── .env.example                     # Template to set environment variables
├── .pre-commit-config.yaml          # Configuration file for pre-commit hooks
├── docker-compose.yaml              # Docker configuration for building the application
├── Dockerfile                       # Docker configuration for building the application
├── poetry.lock                      # Requirements for development and production
└── pyproject.toml                   # Project metadata and dependencies (PEP 518)
└── README.md
```

## Setup

1. Rename `.env.example` to `.env` and set your Kaggle credentials in this file.

## Notebooks

Run notebooks in `notebooks/` directory to conduct Exploratory Data Analysis and experiment with features selection using Feature-engine module ideally created for these purposes (See [References](#references) for further information). Diverse experiments were carry out using Linear Regression, RandomForest and XGBoost. The resultant features were persistent into a yaml file containing other global properties.

## Streamlit UI

![Alt text](./images/streamlit-ui.png)