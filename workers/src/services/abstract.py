from abc import ABC
from contextlib import contextmanager
from typing import Type

from sqlalchemy.orm import Session


class AbstractService(ABC):
    def __init__(self, session: Session) -> None:
        self._session = session

    def close(self) -> None:
        self._session.close()
