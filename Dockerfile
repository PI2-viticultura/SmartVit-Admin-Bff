FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./src /app

RUN pip install -r requirements.txt