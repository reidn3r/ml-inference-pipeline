from sqlalchemy.orm import Session
from src.database.models.inference_entity import InferenceEntity
from src.database.models.input_entity import InputEntity
import src.database.repository.input_repository as input_repository
import src.database.repository.model_repository as model_repository

def add(
  session: Session,
  model_name: str,
  req_id: str,
  input_content: str,
  predict_label: str,
  score: float,
  inference_time: float,
  ) -> InferenceEntity:
    
    model_entity = model_repository.find_or_create(session, model_name)
    input_entity: InputEntity = input_repository.add(session, req_id, input_content)

    inference_record = InferenceEntity(
      model_id=model_entity.id,
      input_id=input_entity.id,
      request_id=req_id,
      prediction_content=predict_label,
      prediction_score=score,
      inference_time_ms=inference_time
    )

    session.add(inference_record)
    session.commit()

    return inference_record

def list():
  pass
