import logging
import sys

import pika
from fastapi import FastAPI, HTTPException

from event_model import Event
from config import settings

app = FastAPI()

logger = logging.getLogger(__name__)
logger.setLevel(settings.log_level)


@app.on_event("startup")
def init_queue():
    global connection
    global channel

    credentials = pika.PlainCredentials(
        settings.rabbit_username, settings.rabbit_password
    )
    parameters = pika.ConnectionParameters(
        settings.rabbit_host, credentials=credentials
    )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=settings.rabbit_events_queue_name)

    logger.info("Connected to queue.")


@app.on_event("shutdown")
def shutdown_event():
    logger.info("Closing queue connection.")
    connection.close()


@app.post("v1/event", status_code=201)
def put_event_to_queue(event: Event):

    try:
        channel.basic_publish(exchange='',
                              routing_key=settings.rabbit_events_queue_name,
                              body=event.json())
    except Exception as e:
        logger.error("ERROR - queue publishing error: " + str(e))
        raise HTTPException(500, detail="500: Internal server error. Please try later.")

    return {"201": "Created"}
