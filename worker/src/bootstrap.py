from src.database.connection import database_create_engine
from src.amqp.connect import amqp_connect
from config.environment import environment
from src.database.models import *
from src.inference.sentiment_analyser import SentimentAnalyser
from config.logger import logger

async def bootstrap():
  logger.info("Bootstrap started")
  logger.info("Loading model")
  model = SentimentAnalyser()
  logger.info("Model loaded")

  engine = database_create_engine(environment["DATABASE_URL"])
  await amqp_connect(engine, model)
