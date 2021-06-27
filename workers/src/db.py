"""Модуль содержит вспомогательный функции для работы с базой данных."""
import logging

from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

logger = logging.getLogger(__name__)

engine = create_engine(settings.database_uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
