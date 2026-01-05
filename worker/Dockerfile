FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
  build-essential \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# pytorch cpu
RUN pip install --no-cache-dir \
  --extra-index-url https://download.pytorch.org/whl/cpu \
  -r requirements.txt

FROM python:3.11-slim AS prod

WORKDIR /app

# Copia apenas os pacotes Python instalados
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia o código da aplicação
COPY . .

EXPOSE 3031

CMD ["python3", "-u", "main.py"]