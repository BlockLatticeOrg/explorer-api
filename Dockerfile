FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

EXPOSE 80
EXPOSE 8000

COPY ./ /app

RUN pip install poetry==1.0.10
RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY ./explorer_api /app/app