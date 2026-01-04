from src.database.connection import database_connect
from src.amqp.connect import amqp_connect
from src.amqp.message_callback import message_callback_factory
from config.environment import environment
from src.database.models import *

def bootstrap():
  engine = database_connect(environment["DATABASE_URL"])
  amqp_connect(message_callback_factory(engine))
