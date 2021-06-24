from typing import Optional
import logging

from consumers.email import EmailConsumer

logger = logging.getLogger(__name__)


class Handler:
    def __init__(self):
        self._email_consumer: Optional[EmailConsumer] = None

    def on_startup(self):
        self._email_consumer = EmailConsumer()

    def start(self):
        logger.info("Запуск email потребителя")
        self._email_consumer.consume()


if __name__ == '__main__':
    handler = Handler()
    handler.on_startup()
    handler.start()
