## Проект «API для Yatube»
***
### Описание:

Бэкэнд-часть для API функционала проекта с использованием rest_framework и аутентификацией через JWT.
***
### Функционал:

* Создание и редактирование постов;
* Создание и редактирование комментариев к постам;
* Получение списка сообществ и информации он них;
* Получение списка подписок пользователя, а также возможность оформить подписку;
* Получение, обновление и проверка JWT-токена зарегистрированным пользователем. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:VorVorsky/api_final_yatube.git
```

```
cd api_final_yatube
```
***
Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```
***
Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
***
Перейдите в папку с manage.py проекта и запустите локальный сервер:

```
cd yatube_api/
```
```
python3 manage.py runserver
```
***
### Примеры запросов:

***GET*** /api/v1/posts/ -- для получения постов: 

Получить список всех постов. При указании параметров limit и offset выдача должна работать с пагинацией.

Параметры запроса:

| limit | offset |
|-------|--------|
| integer | integer |
| Количество публикаций на страницу | Номер страницы после которой начинать выдачу |

Ответ:
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
***POST*** /api/v1/posts/ -- для создания поста: 

Анонимные запросы запрещены.

Запрос:
```json
{
  "text": "string",   // required
  "image": "string",  // optional
  "group": 0          // optional
}
```
Ответ:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
***GET*** /api/v1/posts/***{id}*** -- для получения поста: 

Параметры запроса:

id -- int() and required (id публикации) 

Ответ:
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
***PUT*** /api/v1/posts/***{id}*** -- обновление поста: 

Обновить публикацию может только автор публикации. Анонимные запросы запрещены.

Запрос:
```json
{
  "text": "string",   // required
  "image": "string",  // optional
  "group": 0          // optional
}
```
Ответ:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
***PATCH*** /api/v1/posts/***{id}*** -- частичное обновление поста: 

Обновить публикацию может только автор публикации. Анонимные запросы запрещены.



Запрос:
```json
{
  "text": "string",   // required
  "image": "string",  // optional
  "group": 0          // optional
}
```
Ответ:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
***DELETE*** /api/v1/posts/***{id}*** -- удаление публикации:

Параметры запроса:

id -- int() and required (id публикации)

***GET*** /api/v1/posts/***{post_id}***/comments -- для получения всех комментариев к посту: 

Получить список всех постов. При указании параметров limit и offset выдача должна работать с пагинацией.

Параметры запроса:

post_id -- int() and required (id публикации)

Ответ:
```json
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
***POST*** /api/v1/posts/***{post_id}***/comments -- для добавление нового комментария к посту:

Анонимные запросы запрещены.

Параметры запроса:

post_id -- int() and required (id публикации)

Запрос:
```json
{
  "text": "string"   // required
}
```
Ответ:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
***GET*** /api/v1/posts/***{post_id}***/comments/***{id}*** -- для получения комментария к посту: 

Параметры запроса:

post_id -- int() and required (id публикации) 
id -- int() and required (id комментария)

Ответ:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
***PUT*** /api/v1/posts/***{post_id}***/comments/***{id}*** -- обновление комметария: 

Обновить комментарий может только автор комментария. Анонимные запросы запрещены.

Параметры запроса:

post_id -- int() and required (id публикации) 
id -- int() and required (id комментария)

Запрос:
```json
{
  "text": "string"   // required
}
```
Ответ:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
***PATCH*** /api/v1/posts/***{post_id}***/comments/***{id}*** -- частичное обновление комметария: 

Обновить комментарий может только автор комментария. Анонимные запросы запрещены

Параметры запроса:

post_id -- int() and required (id публикации) 
id -- int() and required (id комментария)

Запрос:
```json
{
  "text": "string"   // required
}
```
Ответ:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
***DELETE*** /api/v1/posts/***{post_id}***/comments/***{id}*** -- удаление комментария:

Удалить может только автор комментария. Анонимные запросы запрещены

Параметры запроса:

post_id -- int() and required (id публикации) 
id -- int() and required (id комментария)

***GET*** /api/v1/groups/ -- получение списка доступных сообществ: 

Ответ:
```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
***GET*** /api/v1/groups/***{id}*** -- получение информации о сообществе: 

Параметры запроса:

id -- int() and required (id сообщества)

Ответ:
```json
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```
***GET*** /api/v1/follow/ -- возвращает все подписки пользователя, сделавшего запрос:

Анонимные запросы запрещены.

Параметры запроса:

Возможен поиск по подпискам по параметру search

Ответ:
```json
[
  {
    "user": "string",
    "following": "string"
  }
]
```
***POST*** /api/v1/follow/ -- для подписки на автора: 

Анонимные запросы запрещены.

Запрос:
```json
{
"following": "string" // required (username на кого оформляется подписка)
}
```
Ответ:
```json
{
  "user": "string",
  "following": "string"
}
```
***
## JWT аутентификация
***POST*** /api/v1/jwt/create/ -- получение JWT-токена:

Запрос:
```json
{
  "username": "string", // required
  "password": "string"  // required
}
```
Ответ:
```json
{
  "refresh": "string",
  "access": "string"
}
```
***POST*** /api/v1/jwt/refresh/ -- обновление JWT-токена:

Запрос:
```json
{
  "refresh": "string" // required
}
```
Ответ:
```json
{
  "access": "string"
}
```
***POST*** /api/v1/jwt/verify/ -- проверить JWT-токена:

Запрос:
```json
{
  "token": "string" // required
}
```
Ответ:

***HTTP_200_OK***