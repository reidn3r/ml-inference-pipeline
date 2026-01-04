from sqlalchemy.orm import Session
from src.database.models.input_entity import InputEntity

def add(
  session: Session,
  req_id: str,
  content: str,
  ) -> InputEntity:
  input_record = InputEntity(
    request_id=req_id,
    content=content
  )

  session.add(input_record)
  session.commit()

  return input_record