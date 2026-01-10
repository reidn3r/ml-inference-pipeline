from src.database.models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, REAL, Numeric, ForeignKey
from datetime import datetime
import uuid

class InferenceEntity(Base):
  __tablename__ = "inference_table"
  
  id: Mapped[int] = mapped_column(
    primary_key=True,
    autoincrement=True
  )
  
  input_id: Mapped[int] = mapped_column(
    ForeignKey("input_table.id"),
    nullable=False,
  )
  
  request_id: Mapped[uuid.UUID] = mapped_column(
    ForeignKey("input_table.request_id"),
    unique=True
  )
  
  prediction_content: Mapped[str] = mapped_column(
    String,
    nullable=False
  )
  
  prediction_score: Mapped[float] = mapped_column(
    Numeric(5, 4),
    nullable=False
  )
  
  inference_time_ms: Mapped[float] = mapped_column(
    REAL,
    nullable=False
  )

  model_id: Mapped[uuid.UUID] = mapped_column(
    ForeignKey("model_table.id"),
    nullable=False
  )


  created_at: Mapped[datetime] = mapped_column(
    nullable=False,
    default=datetime.now  
  )

  inference_model = relationship(
    "ModelEntity",
    back_populates="inferences"
  )

  def __repr__(self):
    return (
      f"InferenceEntity("
      f"id={self.id}, "
      f"model_id={self.model_id}, "
      f"input_id={self.input_id}, "
      f"request_id='{self.request_id}', "
      f"prediction_content='{self.prediction_content}', "
      f"prediction_score={self.prediction_score}, "
      f"inference_time_ms={self.inference_time_ms}"
      f")"
    )
