#!/bin/env bash
# Using /run/redis.sock
redis-server /etc/redis/redis.conf

# Wait for Redis to start via socket
while [ ! -e /run/redis.sock ] || ! nc -zU /run/redis.sock; do
  echo "Waiting for Redis to start..."
  sleep 1
done

python app.py
