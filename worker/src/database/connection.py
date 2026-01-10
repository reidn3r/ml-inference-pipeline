from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from config.logger import logger

def database_create_engine(url: str) -> AsyncEngine:
  logger.info("DB Creating engine")
  engine = create_async_engine(
    url=url,
    echo=True,
    pool_size=10
  )
  logger.info("PostgreSQL connected")
  return engine