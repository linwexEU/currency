FROM python:3.11.7

RUN mkdir /currency 

WORKDIR /currency

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . . 

CMD ["gunicorn", "app.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]









