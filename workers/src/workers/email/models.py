from datetime import datetime
from enum import Enum

from sqlalchemy import Column, String, Text, DateTime, ARRAY, JSON, Boolean, Integer, ForeignKey, Enum as saEnum
from sqlalchemy.orm import relationship

from db import Base


class DateMixin:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class TemplateCodes(Enum):
    welcome_letter = "welcome_letter"


class Template(DateMixin, Base):
    __tablename__ = "email_templates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    code = Column(saEnum(TemplateCodes))
    html = Column(Text, nullable=False)
    subject = Column(Text, nullable=False)


class TaskStatuses(Enum):
    in_process = 1
    done = 2
    cancelled = 3


class Task(DateMixin, Base):
    __tablename__ = "email_tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(String, nullable=False)
    status = Column(Integer)
    email = Column(String, nullable=False)

    template_id = Column(Integer, ForeignKey('email_templates.id'))
    template_data = Column(JSON)

    scheduled_datetime = Column(DateTime)
    execution_datetime = Column(DateTime)

    error = Column(Text, nullable=True)