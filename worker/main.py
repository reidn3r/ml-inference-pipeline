import asyncio
from src.bootstrap import bootstrap

def main():
  asyncio.run(bootstrap())

if __name__ == "__main__":
  main()