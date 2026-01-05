from src.database.connection import database_connect
from src.amqp.connect import amqp_connect
from src.amqp.message_callback import message_callback_factory
from config.environment import environment
from src.database.models import *
from src.model.sentiment_analyser import SentimentAnalyser

def bootstrap():
  print("[MODEL]: Loading model...", flush=True)
  model = SentimentAnalyser()
  print("[MODEL]: Model loaded", flush=True)

  engine = database_connect(environment["DATABASE_URL"])
  amqp_connect(message_callback_factory(engine, model))
