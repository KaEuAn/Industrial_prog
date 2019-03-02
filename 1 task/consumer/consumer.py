import os
import pika
import psycopg2

print('starting...')

rmq_parameters = pika.URLParameters(os.getenv('RABBIT_URL'))
print(f'starting with parameters {rmq_parameters}')
connection = pika.BlockingConnection(rmq_parameters)
print(f'got connection: {connection}')
channel = connection.channel()
print(f'got channel: {channel}')
channel.queue_declare(queue='sendrecqueue')
print(' [*] Waiting for messages. To exit press CTRL+C')

db_conn = psycopg2.connect(os.getenv('DB_URL'))
cursor = db_conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages (number INT) ")
db_conn.commit()

def callback(ch, method, properties, body):
    message = int(body.decode())
    print(message, flush=True)
    cursor.execute("INSERT INTO messages VALUES (%s)", (message, ))
    db_conn.commit()
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='sendrecqueue')

channel.start_consuming()
cursor.close()