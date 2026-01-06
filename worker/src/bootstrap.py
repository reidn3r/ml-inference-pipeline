# from src.amqp.message_callback import message_callback_factory
from src.database.connection import database_create_engine
from src.amqp.connect import amqp_connect
from config.environment import environment
from src.database.models import *
from src.inference.sentiment_analyser import SentimentAnalyser

async def bootstrap():
  print("[MODEL]: Loading model...", flush=True)
  model = SentimentAnalyser()
  print("[MODEL]: Model loaded", flush=True)

  engine = database_create_engine(environment["DATABASE_URL"])
  await amqp_connect(engine, model)
