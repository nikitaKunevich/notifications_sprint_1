from typing import Optional

from consumers.email import EmailConsumer


class Handler:
    def __init__(self):
        self._email_consumer: Optional[EmailConsumer] = None

    def on_startup(self):
        self._email_consumer = EmailConsumer()

    def start(self):
        self._email_consumer.consume()


if __name__ == '__main__':
    handler = Handler()
    handler.on_startup()
    handler.start()
