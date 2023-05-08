FROM python:3.10.2-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y netcat

COPY ./Pipfile ./Pipfile.lock /app/
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /app/

RUN chmod +x /app/build/entrypoint.sh

ENTRYPOINT ["sh", "/app/build/entrypoint.sh"]