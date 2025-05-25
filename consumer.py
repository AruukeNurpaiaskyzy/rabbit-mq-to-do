# import pika

# # Подключаемся к RabbitMQ
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# # Убеждаемся, что очередь 'hello' существует
# channel.queue_declare(queue='test_queue', durable=True)

# # Функция, которая срабатывает при получении сообщения
# def callback(ch, method, properties, body):
#     print(f" [x] Получено сообщение: {body.decode()}")

# # Подписываемся на очередь 'hello'
# channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# print(' [*] Ждём сообщений. Нажмите CTRL+C для выхода.')
# channel.start_consuming()

# from pika import ConnectionParameters, BlockingConnection
# connection_params = ConnectionParameters(
#     host = 'localhost',
#     port = 5672,
# )
# def process_message(*args):
#     for arg in args:
#         print(arg, "\n\n")
# def main():
#     with BlockingConnection(connection_params) as conn:
#         with conn.channel() as ch:
#             ch.queue_declare(queue='messages')
#             ch.basic_consume(
#                 queue='messages',
#                 on_message_callback = process_message,
#             )
#             print("жду сообщений")
#             ch.start_consuming()

# if __name__ == "__main__":
#     main()

import pika
def on_message_received(ch, method, properties, body):
    print(f"message received {body}")
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue = 'letterbox')
channel.basic_consume(queue='letterbox', auto_ack=True,
                      on_message_callback = on_message_received)
print('Starting Consuming')
channel.start_consuming()



