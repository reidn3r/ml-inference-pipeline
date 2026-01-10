import json
import time
from sqlalchemy.ext.asyncio import AsyncEngine
from aio_pika.abc import AbstractIncomingMessage
from src.database.repository import inference_repository
from src.inference.sentiment_analyser import SentimentAnalyser
from src.abstract.factory.session_factory import async_session_factory
import asyncio
from config.logger import logger

async def callback(
  engine: AsyncEngine,
  model: SentimentAnalyser,
  message: AbstractIncomingMessage
  ):

  payload = json.loads(message.body.decode())
  logger.info(f'message: {payload}')

  start = time.time()
  loop = asyncio.get_running_loop()
  label, score = await loop.run_in_executor(
    None,
    model.run,
    payload["content"],
    payload["id"],
  )

  end = time.time()

  async with async_session_factory(engine)() as session:
    await inference_repository.add(
      session=session,
      model_name=model.name,
      req_id=payload["id"],
      input_content=payload["content"],
      predict_label=label,
      score=score,
      inference_time=end - start
    )
