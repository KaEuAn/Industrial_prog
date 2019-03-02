FROM python:3.7-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY producer.py .

CMD ["python", "producer.py"]
