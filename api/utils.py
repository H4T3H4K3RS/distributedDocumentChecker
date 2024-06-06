import json

import pika
from django.conf import settings


def send_task_created_message(task_id, file_url):
    credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ_HOST, port=settings.RABBITMQ_PORT, credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=True)

    message = json.dumps({"task_id": str(task_id), "file_url": file_url})
    channel.basic_publish(
        exchange='',
        routing_key=settings.RABBITMQ_QUEUE,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,
        )
    )

    connection.close()
