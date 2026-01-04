from pika.channel import Channel
from pika.spec import Basic, BasicProperties
from src.model.sentiment_analyser import SentimentAnalyser
from src.database.repository import inference_repository
from sqlalchemy import Engine
from sqlalchemy.orm import Session
import json
import time

def message_callback_factory(engine: Engine):
  def message_callback(
    channel: Channel,
    method_frame: Basic.Deliver,
    header_frame: BasicProperties,
    body: bytes,
  ) -> None:
    str_payload = body.decode()
    payload = json.loads(str_payload)

    model = SentimentAnalyser()

    start_time = time.time()
    label, score = model.run(payload["content"])
    end_time = time.time()

    with Session(engine) as session:
      model_name = model.name
      
      inference_repository.add(
        session=session,
        model_name=model_name,
        req_id=payload["id"],
        input_content=payload["content"],
        predict_label=label,
        score=score,
        inference_time=end_time-start_time
      )

    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

  return message_callback
