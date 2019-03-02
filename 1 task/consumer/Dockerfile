FROM python:3.7-alpine

WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY consumer.py .

CMD ["python", "consumer.py"]
