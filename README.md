##API  
**Отправитель**: auth  
**Тип источника сообщения**: email  
**Тип события**: приветственное письмо  
```json5
{
  "service": "ugc",
  "source": "email",
  "event_type": "welcome_letter",
  "scheduled_datetime": "2021-06-24T09:32:20.990847",
  "payload": {
    "user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f"
  }
}
```

**Отправитель**: ugc  
**Тип источника сообщения**: email  
**Тип события**: подборка фильмов
```json5
{
  "service": "ugc",
  "source": "email",
  "event_type": "selection_movies",
  "scheduled_datetime": "2021-06-24T09:32:20.990847",
  "payload": {
    "user_ids": [
      "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f",
      "39f042c2-dfb0-47e2-916b-5c0e0c493ded",
      "4109d174-eeec-4df3-8e4a-53fd59e251cd"
    ],
    "movie_ids": [
        "9dac72a5-f52e-4b0d-9ce9-e03b4ba0dfc4",
        "0425d9b1-9b02-4fbe-ba52-36e2d59a3a0e",
        "aca7e4c5-c3c8-456f-b162-a3cb02ff9000"
    ]
  }
}
```

**Отправитель**: ugc  
**Тип источника сообщения**: email  
**Тип события**: Персональная рассылка фильмов
```json5
{
  "service": "ugc",
  "source": "email",
  "event_type": "personal_newsletter",
  "scheduled_datetime": "2021-06-24T09:32:20.990847",
  "payload": {
    "user_id": "39f042c2-dfb0-47e2-916b-5c0e0c493ded",
    "movie_ids": [
        "9dac72a5-f52e-4b0d-9ce9-e03b4ba0dfc4",
        "0425d9b1-9b02-4fbe-ba52-36e2d59a3a0e",
        "aca7e4c5-c3c8-456f-b162-a3cb02ff9000"
    ]
  }
}
```
