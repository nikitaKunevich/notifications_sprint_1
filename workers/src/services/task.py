from contextlib import contextmanager
from typing import Optional

from sqlalchemy.orm import Session

from db import SessionLocal
from services.abstract import AbstractService
from workers.email.models import Template, Task


@contextmanager
def service_with_session(session: Session):
    """Возвращает подготовленный сервис."""
    service = TaskService(session)
    yield service
    service.close()


class TaskService(AbstractService):
    def create_task(self, **kwargs):
        task = Task(**kwargs)
        self._session.add(task)
        self._session.commit()


def get_task_service() -> TaskService:
    """Возвращает подготовленный TemplateService."""
    with service_with_session(SessionLocal()) as service:
        return service
