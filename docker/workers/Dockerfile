FROM python:3.9.1-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y postgresql-client

ARG UID=2000
ARG GID=2000
ARG USER=django
ARG GROUP=application
ARG ROOT_APP=/app/

RUN groupadd -g $GID $GROUP
RUN useradd -u $UID -g $GID -m $USER

RUN mkdir $ROOT_APP

WORKDIR $ROOT_APP

COPY workers/Pipfile /app/Pipfile
COPY workers/Pipfile.lock /app/Pipfile.lock

RUN pip install pipenv
RUN pipenv install --system --ignore-pipfile

COPY workers/src $ROOT_APP
COPY workers/entrypoint.sh $ROOT_APP/entrypoint.sh

RUN chown -R $USER:$GROUP $ROOT_APP
USER $USER

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]