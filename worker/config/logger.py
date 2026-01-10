import json
import logging
import sys
from typing import Optional
from datetime import datetime
from config.environment import environment

def setup_logger(
  name: str = "worker",
  level: Optional[str] = None,
  json_logs: bool = False
) -> logging.Logger:
  
  log_level = level or environment.get("LOG_LEVEL", "INFO")
  
  logger = logging.getLogger(name)
  logger.setLevel(getattr(logging, log_level.upper()))

  logger.handlers.clear()
  
  # Handler para stdout
  handler = logging.StreamHandler(sys.stdout)
  handler.setLevel(getattr(logging, log_level.upper()))
  
  if json_logs:
    formatter = JsonFormatter()
  else:
    formatter = logging.Formatter(
      fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S'
  )
  
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  
  return logger

class JsonFormatter(logging.Formatter):
  def format(self, record: logging.LogRecord) -> str:
    log_data = {
      "timestamp": datetime.utcnow().isoformat(),
      "level": record.levelname,
      "logger": record.name,
      "message": record.getMessage(),
      "module": record.module,
      "function": record.funcName,
      "line": record.lineno
    }

    if hasattr(record, 'extra'):
      log_data.update(record.extra)
        
    # Adiciona exception info se existir
    if record.exc_info:
      log_data["exception"] = self.formatException(record.exc_info)

    return json.dumps(log_data)

logger = setup_logger()