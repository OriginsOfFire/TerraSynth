#!/bin/sh

until nc -z -v -w30 postgres 5432
do
  echo 'Waiting for database connection'
  sleep 5
done

alembic upgrade head
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000