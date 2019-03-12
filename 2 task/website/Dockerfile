FROM python:3.7.2-alpine
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /
RUN pip install -r /requirements.txt
VOLUME /app
COPY * /app/
CMD ["/bin/sh", "/app/run.sh"]