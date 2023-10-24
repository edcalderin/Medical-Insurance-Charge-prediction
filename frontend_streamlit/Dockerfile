# Stage 1: Build
FROM python:3.11-buster as builder

RUN pip install poetry==1.6.1

WORKDIR /frontend_streamlit

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true && poetry install --no-root

# Stage 2: Runtime
FROM python:3.11-slim-buster

WORKDIR /frontend_streamlit

COPY --from=builder /frontend_streamlit .

ENV PATH="/frontend_streamlit/.venv/bin:$PATH"

COPY app.py .

ENTRYPOINT ["streamlit", "run", "app.py"]