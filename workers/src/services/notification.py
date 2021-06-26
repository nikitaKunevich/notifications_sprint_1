import logging
from contextlib import contextmanager

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db import SessionLocal
from services.abstract import AbstractService
from workers.email.models import Notification

logger = logging.getLogger(__name__)


@contextmanager
def service_with_session(session: Session):
    """Возвращает подготовленный сервис."""
    service = NotificationService(session)
    yield service
    service.close()


class NotificationService(AbstractService):
    """Сервис по работе с моделью notification."""

    def create_notification(self, **kwargs) -> None:
        """Создает экземпляр notification."""
        notification = Notification(**kwargs)
        self._session.add(notification)
        try:
            self._session.commit()
        except IntegrityError as exc:
            logger.exception(exc)


def get_notification_service() -> NotificationService:
    """Возвращает подготовленный TemplateService."""
    with service_with_session(SessionLocal()) as service:
        return service
