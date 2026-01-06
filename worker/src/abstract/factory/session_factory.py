from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine

def async_session_factory(engine: AsyncEngine):
  return async_sessionmaker(
    engine,
    expire_on_commit=False
  )
