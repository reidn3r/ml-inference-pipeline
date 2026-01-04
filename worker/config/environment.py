import os
from dotenv import load_dotenv

load_dotenv() 

environment = {
  "RABBITMQ_URL": os.getenv("AMQP_URL"),
  "DATABASE_URL": os.getenv("DATABASE_URL"),
}
