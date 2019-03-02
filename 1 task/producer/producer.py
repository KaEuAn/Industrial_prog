import pika
import random
import os
from time import sleep

rmq_parameters = pika.URLParameters(os.getenv('RABBIT_URL'))
print(f'starting with parameters {rmq_parameters}')
connection = pika.BlockingConnection(rmq_parameters)
print(f'got connection: {connection}')
channel = connection.channel()
print(f'got channel: {channel}')
channel.queue_declare(queue='sendrecqueue')
print(4)

for i in range(100):
    sleep(random.randint(1,10)/100)
    message = random.randint(1,1000)
    channel.basic_publish(exchange='', routing_key='sendrecqueue', body = str(message).encode())

connection.close()