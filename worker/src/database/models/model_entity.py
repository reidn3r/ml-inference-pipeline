from src.database.models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from datetime import datetime
import uuid


class ModelEntity(Base):
  __tablename__ = "model_table"

  id: Mapped[uuid.UUID] = mapped_column(
    primary_key=True, 
    default=uuid.uuid4
  )
  
  name: Mapped[str] = mapped_column(
    String,
    nullable=False
  )
  
  created_at: Mapped[datetime] = mapped_column(
    nullable=False,
    default=datetime.now 
  )

  inferences = relationship(
    "InferenceEntity",
    back_populates="inference_model"
  )