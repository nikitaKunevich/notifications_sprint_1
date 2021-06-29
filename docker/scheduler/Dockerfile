FROM python:3.9.1-slim

ENV PYTHONUNBUFFERED 1

ARG ROOT_APP=/app

RUN mkdir $ROOT_APP

COPY scheduler/Pipfile $ROOT_APP/Pipfile
COPY scheduler/Pipfile.lock $ROOT_APP/Pipfile.lock

WORKDIR $ROOT_APP
RUN pip install pipenv && \
    pipenv install --system --ignore-pipfile

COPY scheduler/src $ROOT_APP/

CMD python main.py