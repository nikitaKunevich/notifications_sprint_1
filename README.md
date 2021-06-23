##Структура сообщений
###Массовая рассылка  
**Отправитель**: ugc  
**Тип сообщения**: email  
**Тип события**: новые фильмы на платформе

```json
{
  "event_id": "a53b6c5f-4ec8-450a-a16d-4c53a6bd2892",
  "service": "ugc",
  "source_type": "email",
  "event_type": "new_movies",
  "payload": {
    "user_ids": [
      "1ec4cd73-2fd5-4f25-af68-b6595d279af2",
      "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f"
    ]
  }
}
```
###Персонализированная рассылка
**Отправитель**: ugc  
**Тип сообщения**: email  
**Тип события**: статистика просмотренных фильмов
```json
{
  "event_id": "a53b6c5f-4ec8-450a-a16d-4c53a6bd2893",
  "service": "ugc",
  "source_type": "email",
  "event_type": "view_statistics",
  "payload": {
    "user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f",
    "movie_ids": [
      "25d7e6ab-f18a-4245-a8e1-76531c0fc98d",
      "b47bcfc0-9c74-4585-a866-4d4d4308902c",
      "484ea0d9-ff56-4ccc-b638-e09a9f3eaf00",
      "9277df37-3c6a-4b6f-a462-ac1f4cbf2917"
    ],
    "favourite_movie_ids": [
      "9277df37-3c6a-4b6f-a462-ac1f4cbf2917"
    ]
  }
}
```
