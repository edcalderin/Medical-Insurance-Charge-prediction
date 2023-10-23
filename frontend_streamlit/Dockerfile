FROM python:3.11-slim

RUN pip install poetry==1.6.1

WORKDIR /frontend_streamlit

COPY pyproject.toml poetry.lock ./

#Since there are not dev dependences, just will run `poetry install`
RUN poetry config virtualenvs.create false && poetry install

COPY app.py .

ENTRYPOINT [ "streamlit", "run", "app.py" ]