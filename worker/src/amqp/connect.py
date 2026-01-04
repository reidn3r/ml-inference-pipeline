from config.environment import environment
import pika

def amqp_connect(callback) -> None :
  params = pika.URLParameters(environment["RABBITMQ_URL"])
  conn = pika.BlockingConnection(parameters=params)
  channel = conn.channel()

  channel.basic_consume(
    queue="inference.request",
    on_message_callback=callback)

  print("[AMQP]: RabbitMQ connected")
  channel.start_consuming()