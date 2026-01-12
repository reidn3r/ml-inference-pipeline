#!/bin/bash

set -e

echo "Subindo cluster Kubernetes"

# ===============================
# 1. DATABASE
# ===============================
echo "📦 [1/5] PostgreSQL"

kubectl create secret generic db-environment \
  --from-env-file=./database/.env \
  --dry-run=client -o yaml | kubectl apply -f -

kubectl apply -f ./database/db.statefulset.yml
kubectl apply -f ./database/service.yml

kubectl rollout status statefulset/pgsql

# ===============================
# 2. MIGRATION JOB
# ===============================
echo "🗄️ [2/5] Migration job"

kubectl delete job migration-job --ignore-not-found
kubectl apply -f ./database/migration.job.yml

kubectl wait --for=condition=complete job/migration-job --timeout=120s

# ===============================
# 3. RABBITMQ
# ===============================
echo "🐰 [3/5] RabbitMQ"

kubectl create secret generic rabbitmq-env \
  --from-env-file=./message-broker/.env \
  --dry-run=client -o yaml | kubectl apply -f -

kubectl apply -f ./message-broker/definitions.configmap.yml
kubectl apply -f ./message-broker/rabbitmqconf.configmap.yml

kubectl apply -f ./message-broker/mq.statefulset.yml
kubectl apply -f ./message-broker/service.yml

kubectl rollout status statefulset/rabbitmq

# ===============================
# 4. WORKER
# ===============================
echo "🧠 [4/5] Worker de inferência"

kubectl create secret generic worker-environment \
  --from-env-file=./worker/.env \
  --dry-run=client -o yaml | kubectl apply -f -

kubectl apply -f ./worker/deployment.yml

kubectl rollout status deployment/worker-deployment

# ===============================
# 5. API
# ===============================
echo "🌐 [5/5] API Web"

kubectl create secret generic api-environment \
  --from-env-file=./api/.env \
  --dry-run=client -o yaml | kubectl apply -f -

kubectl apply -f ./api/deployment.yml
kubectl apply -f ./api/service.yml

kubectl rollout status deployment/api-deployment

echo "✅ Cluster iniciado com sucesso!"
