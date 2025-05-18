import pika

# Подключаемся к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Убеждаемся, что очередь 'hello' существует
channel.queue_declare(queue='test_queue', durable=True)

# Функция, которая срабатывает при получении сообщения
def callback(ch, method, properties, body):
    print(f" [x] Получено сообщение: {body.decode()}")

# Подписываемся на очередь 'hello'
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Ждём сообщений. Нажмите CTRL+C для выхода.')
channel.start_consuming()
