FROM python:3.7-alpine

WORKDIR /app
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN pip install --upgrade pip
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY consumer.py .

CMD ["python", "consumer.py"]
