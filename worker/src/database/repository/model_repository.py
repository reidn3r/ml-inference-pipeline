from sqlalchemy.orm import Session
from src.database.models.model_entity import ModelEntity

def find_or_create(session: Session, model: str) -> ModelEntity:
  instance = (
    session.query(ModelEntity)
    .filter(ModelEntity.name == model)
    .one_or_none()
  )

  if instance:
    return instance

  instance = ModelEntity(name=model)
  session.add(instance)
  session.commit()
  session.refresh(instance)

  return instance
