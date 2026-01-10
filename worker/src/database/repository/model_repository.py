from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models.model_entity import ModelEntity

async def find_or_create(
  session: AsyncSession,
  model: str
) -> ModelEntity:
  record = select(ModelEntity).where(ModelEntity.name == model)
  result = await session.execute(record)
  instance = result.scalar_one_or_none()

  if instance:
    return instance

  instance = ModelEntity(name=model)
  session.add(instance)
  await session.commit()
  await session.refresh(instance)

  return instance
