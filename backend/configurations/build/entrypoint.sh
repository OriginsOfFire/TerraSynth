while ! nc -z rabbitmq 5672; do sleep 3; done
uvicorn src.app:app --reload --host 0.0.0.0 --port 8001