from src.inference.sentiment_analyser import SentimentAnalyser
from src.inference.infer_callback import callback
from config.environment import environment
from sqlalchemy.ext.asyncio import AsyncEngine
from config.logger import logger
from aio_pika import Channel
import aio_pika

async def amqp_connect(
    engine: AsyncEngine,
    model: SentimentAnalyser
  ) -> None :
  conn = await aio_pika.connect_robust(environment["RABBITMQ_URL"])
  channel: Channel = await conn.channel()

  queue = await channel.get_queue("inference.request")
  logger.info("RabbitMQ connected")

  async with queue.iterator() as iterator:
    async for msg in iterator:
      async with msg.process():
        await callback(engine, model, msg)
