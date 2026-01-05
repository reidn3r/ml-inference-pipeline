from sqlalchemy import Engine, create_engine

def database_connect(url: str) -> Engine:
  print("[DB]: Creating engine", flush=True)
  engine = create_engine(
    url=url,
    echo=True,
    pool_size=10
  )
  print("[DB]: PostgreSQL connected", flush=True)
  return engine