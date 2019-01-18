from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)
import pika

@app.task
def add(x, y):
    # return x + y

    #########
    # !/usr/bin/env python

    credentials = pika.PlainCredentials('admin', 'admin')
    parameters = pika.ConnectionParameters('localhost',
                                           5672,
                                           '/',
                                           credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    connection.close()
    return " [x] Sent 'Hello World!'"
    ######


