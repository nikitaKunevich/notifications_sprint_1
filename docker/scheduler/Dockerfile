FROM python:3.9.1-slim

ENV PYTHONUNBUFFERED 1

ARG ROOT_APP=/app/

RUN mkdir $ROOT_APP

COPY scheduler/* $ROOT_APP

WORKDIR $ROOT_APP
RUN pip install pipenv && \
    pipenv install --system --ignore-pipfile

CMD python main.py