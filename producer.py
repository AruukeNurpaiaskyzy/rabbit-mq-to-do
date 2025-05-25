# import pika 

# # Подключаемся к RabbitMQ (localhost = твой компьютер)
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# # Создаём очередь с именем 'hello'
# channel.queue_declare(queue='hello')

# # Отправляем сообщение
# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body='Привет от Producer!')
# print(" [x] Отправлено: Привет от Producer!")

# connection.close() 
# from pika import ConnectionParameters, BlockingConnection
# connection_params = ConnectionParameters(
#     host = 'localhost',
#     port = 5672,
# )
# def main():
#     with BlockingConnection(connection_params) as conn:
#         with conn.channel() as ch:
#             ch.queue_declare(queue='messages')

#             ch.basic_publish(
#                 exchange="",
#                 routing_key='messages',
#                 body = 'Hello Rabbitmq.'
#             )
#             print('Message sent')

# if __name__ == "__main__":
#     main()
import pika
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='letterbox')

message = 'Hello this is my second message or third message'
channel.basic_publish (exchange = '', routing_key = 'letterbox', body = message)
print(f'sent message: {message}')
connection.close()

