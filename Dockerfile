# Stage 1: Build
FROM python:3.11-buster as builder

RUN pip install poetry==1.6.1

WORKDIR /backend_app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true && poetry install --no-root --without dev

# Stage 2: Runtime
FROM python:3.11-slim-buster

WORKDIR /backend_app

COPY --from=builder /backend_app .

ENV PATH="/backend_app/.venv/bin:$PATH"

COPY backend_app/ .

EXPOSE 8080

ENTRYPOINT [ "bash", "start_server.sh" ]