import json
import logging
from datetime import datetime
from typing import Callable, Optional

import pika
from pika import channel as pika_channel  # noqa: F401

from config import settings
from consumers.base import ReconnectingConsumer
from services.task import get_task_service
from workers.email import models
from workers.email.handlers import handlers
from workers.email.logger import EmailEventAdapter
from workers.email.models import TaskStatuses

logger = logging.getLogger(__name__)


def get_template_data(handler: Callable[[dict], dict], event_data: dict) -> dict:
    return handler(event_data)


class EmailConsumer(ReconnectingConsumer):
    def __init__(self):
        parameters = {
            "EXCHANGE": settings.rabbit_email_exchange,
            "EXCHANGE_TYPE": settings.rabbit_email_exchange_type,
            "QUEUES": settings.rabbit_email_queues,
            "ROUTING_KEY": settings.rabbit_email_routing_key,
            "USERNAME": settings.rabbit_username,
            "PASSWORD": settings.rabbit_password,
            "HOST": settings.rabbit_host,
        }
        super().__init__(parameters)

    def decode_data(self, body: bytes, delivery_tag: int) -> Optional[dict]:
        try:
            return json.loads(body)
        except json.decoder.JSONDecodeError as e:
            logger.exception(e)
            self._consumer.acknowledge_message(delivery_tag)
            return

    def on_message(
        self,
        _unused_channel: pika_channel.Channel,
        basic_deliver: pika.spec.Basic.Deliver,
        _properties: pika.spec.BasicProperties,
        body: bytes,
    ):
        event_data = self.decode_data(body, basic_deliver.delivery_tag)

        if event_data is None:
            return

        # {"service": "ugc", "event_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f", "event_type": "welcome_letter",
        #  "payload": {"user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f"}}

        adapter = EmailEventAdapter(
            logger, event_data
        )

        try:
            handler = handlers[event_data["event_type"]]
        except KeyError:
            adapter.info("Handler not found for this product.")
        else:
            try:
                adapter.info("Email handler found")
                adapter.debug(f"Email handler called with {event_data}")

                template_data = handler(event_data)

                scheduled_datetime = datetime.fromisoformat(event_data['scheduled_datetime'])

                task_service = get_task_service()

                task_service.create_task(
                    event_id=event_data["event_id"],
                    email=template_data['context']["email"],
                    scheduled_datetime=scheduled_datetime,
                    template_id=template_data['template_id'],
                    status=TaskStatuses.in_process.value,
                    template_data=template_data['context']
                )

                adapter.info("Task successfully created")

            except Exception as e:
                adapter.exception(e)
                pass

        self._consumer.acknowledge_message(basic_deliver.delivery_tag)


email_consumer = EmailConsumer()