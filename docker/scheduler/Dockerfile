FROM python:3.9.1-slim

ENV PYTHONUNBUFFERED 1

ARG ROOT_APP=/app/

RUN mkdir $ROOT_APP

WORKDIR $ROOT_APP

RUN pip install pipenv

COPY scheduler/Pipfile /app/Pipfile
COPY scheduler/Pipfile.lock /app/Pipfile.lock

RUN pipenv install --system --ignore-pipfile


COPY scheduler/src $ROOT_APP

CMD python main.py