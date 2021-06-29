FROM python:3.9.1-slim

ENV PYTHONUNBUFFERED 1

ARG UID=2000
ARG GID=2000
ARG USER=django
ARG GROUP=application
ARG ROOT_APP=/app/

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    apt-get clean

RUN groupadd -g $GID $GROUP && \
    useradd -u $UID -g $GID -m $USER && \
    mkdir $ROOT_APP

COPY workers/* $ROOT_APP

WORKDIR $ROOT_APP
RUN pip install pipenv && \
    pipenv install --system --ignore-pipfile && \
    chown -R $USER:$GROUP $ROOT_APP && \
    chmod +x entrypoint.sh

USER $USER
ENTRYPOINT ["./entrypoint.sh"]