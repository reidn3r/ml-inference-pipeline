from src.database.models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
import uuid

class InputEntity(Base):
  __tablename__ = "input_table"

  id: Mapped[int] = mapped_column(
    primary_key=True,
    autoincrement=True
  )
  
  request_id: Mapped[uuid.UUID] = mapped_column(
    nullable=False,
    unique=True,
    default=uuid.uuid4
)
  
  content: Mapped[str] = mapped_column(
    String(),
    nullable=False
  )