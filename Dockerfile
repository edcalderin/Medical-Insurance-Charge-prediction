FROM python:3.11-slim

RUN pip install poetry==1.6.1

WORKDIR /backend_app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --without dev

COPY backend_app/ .

ENTRYPOINT [ "bash", "start_server.sh" ]