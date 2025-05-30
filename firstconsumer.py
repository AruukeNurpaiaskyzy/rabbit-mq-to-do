import pika
import time
import random
def on_message_received(ch, method, properties, body):
    processing_time=random.randit(1,6)
    print(f"received:{body},will take {processing_time} to process")
    time.sleep(processing_time)
    ch.basic_ack(delvery_tag = method.delivery_tag)
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue = 'letterbox')
channel.basic_consume(queue='letterbox', auto_ack=True,
                      on_message_callback = on_message_received)
print('Starting Consuming')
channel.start_consuming()