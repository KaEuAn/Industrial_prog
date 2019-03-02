import os
import pika

print('starting...')

rmq_parameters = pika.URLParameters(os.getenv('RABBIT_URL'))
print(f'starting with parameters {rmq_parameters}')
connection = pika.BlockingConnection(rmq_parameters)
print(f'got connection: {connection}')
channel = connection.channel()
print(f'got channel: {channel}')
channel.queue_declare(queue='sendrecqueue')
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    message = int(body)
    print(message)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='sendrecqueue')

channel.start_consuming()
