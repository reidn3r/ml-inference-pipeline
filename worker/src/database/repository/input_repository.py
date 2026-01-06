from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models.input_entity import InputEntity

async def add(
  session: AsyncSession,
  req_id: str,
  content: str,
  ) -> InputEntity:
  input_record = InputEntity(
    request_id=req_id,
    content=content
  )

  session.add(input_record)
  await session.commit()

  return input_record
