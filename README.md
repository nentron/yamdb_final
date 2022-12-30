# YAMDB_FINAL 
[work's status](https://github.com/nentron/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
Yamdb_final - это проект созданный для публикации информации о произведение искуства, оставление ревью на них, комментарии на ривью. Он создан на REST API. В проекте реализованно 4 вида пользователя: админ, модератор, пользователь и анонимный пользователь.
Пользователи могут оставлять отзывы и оценки произведениям на основании которых формируется рейтинг.

## ТЕХНОЛОГИИ
- Python 3.7.9
- Django 2.2.16
- DRF 3.12.4
- Gunicore 20.1.0
- PostgreSQL
- Nginx

## Развертывание проекта из DockerHub:
- 1.Открыть в браузере https://github.com/nentron/yamdb_final/
- 2.Скопировать на локальный компьютер, директорию infra и перейдите в нее
- 3.Открыть файл docker-compose.yaml и поменять строчку в сервисе веб вместо build.. написать image: nentron/api_yamdb:v0.002
- 4.Создать .env и заполнить по образцу:
    ```
       DB_ENGINE=django.db.backends.postgresql
       DB_NAME=postgres
       POSTGRES_USER=postgres
       POSTGRES_PASSWORD=<придумайте пароль>
       DB_HOST=db
       DB_PORT=5432
       SECRET_KEY=<ключ в одинарных ковычках>
    ```
- 5.Запуск проекта командой ```docker-compose up -d```
- 6.Выполнить миграции командой ```docker-compose exec web python manage.py migrate```
- 7.Загрузить тест файл ```docker-compose exec web python manage.py loaddata fixtures.json```
    - При возникновении проблем на данном этапе, необходимо загрузить fixtures.json из директории api_yamdb проекта на локальный компьютер
    командой ```docker cp <директория расположения скаченного файла> <id web контенера>:app/``` и повторить пункт 7.
- 8.Создать суперпользователя ```docker-compose exec web python manage.py createsuperuser```
- 9.Собрать статику ```docker-compose exec web python manage.py collectstatic```
- 10.Через http://158.160.42.211/admin/ войдите в свою учетную запись 

## Примеры работы с api проекта:
 
Получение списка произведений

```
GET api/v1/titles/
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 2,
      "name": "Naked Pistol",
      "rating": null,
      "year": 1992,
      "description": "adfs",
      "genre": [
        {
          "name": "comedy",
          "slug": "comedy"
        }
      ],
      "category": {
        "name": "film",
        "slug": "film"
      }
    }
  ]
}
```

Получение списка отзывов на произведение

```
 GET api/v1/titles/{title_id}/reviews/
 {
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "text": "good film",
      "author": "dolgo",
      "score": 10,
      "pub_date": "2022-12-16T13:35:24.924993"
    }
  ]
}
```

Получение списка комментариев к отзывам

```
GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/

{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "text": "good film",
      "author": "dolgo",
      "pub_date": "2022-12-16T13:37:21.124444"
    }
  ]
}
```

Подробное описание api в формате ReDoc доступно [тут] 
Ссылка на развернутый проект: [yamdb_final]

[DRF]: <https://www.django-rest-framework.org/>
[тут]: <http://158.160.42.211/redoc/>
[yamdb_final]: <http://158.160.42.211/>
## Авторы проекта
- Nentron



