from notification.apps.email import consts


DATETIME_SCHEMA = {
    "type": "object",
    "title": "Отправка письма",
    "properties": {
        "datetime_key": {
            "title": "Ключ",
            "type": "string",
            "enum": ["start_date", "created_at"],
        },
        "period": {
            "title": "Период отправки письма",
            "type": "string",
            "enum": consts.PERIODS,
        },
        "interval": {
            "title": "Мера времени",
            "type": "string",
            "enum": ["minutes", "hours", "days", "weeks"],
        },
        "time": {"title": "Значение", "type": "integer"},
    },
}
