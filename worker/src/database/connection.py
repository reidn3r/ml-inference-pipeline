from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

def database_create_engine(url: str) -> AsyncEngine:
  print("[DB]: Creating engine", flush=True)
  engine = create_async_engine(
    url=url,
    echo=True,
    pool_size=10
  )
  print("[DB]: PostgreSQL connected", flush=True)
  return engine