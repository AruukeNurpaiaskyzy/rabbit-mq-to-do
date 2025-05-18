import pika

# Подключаемся к RabbitMQ (localhost = твой компьютер)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создаём очередь с именем 'hello'
channel.queue_declare(queue='hello')

# Отправляем сообщение
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Привет от Producer!')
print(" [x] Отправлено: Привет от Producer!")

connection.close() 
