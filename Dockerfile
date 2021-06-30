FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

EXPOSE 8000

WORKDIR /app

COPY ./ .

RUN pip3 install poetry==1.0.10

RUN poetry config virtualenvs.create false
RUN poetry install

# Copy startup script
COPY ./assets/entrypoint.sh /usr/sbin/entrypoint.sh
RUN chmod +x /usr/sbin/entrypoint.sh

ENTRYPOINT "/usr/sbin/entrypoint.sh"