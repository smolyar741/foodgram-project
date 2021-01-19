<<<<<<< HEAD
=======
![foodgram_workflow Action Status](https://github.com/smolyar741/foodgram-project/workflows/foodgram_workflow/badge.svg)

## "Продуктовый помощник Foodgram"

[https://foodgram-book.ga/](https://foodgram-book.ga/ "Продуктовый помощник")

Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.


#### Функциональность проекта

* Проект доступен по IP или доменному имени.
* Все сервисы и страницы доступны для пользователей в соответствии с их правами.
* Рецепты на всех страницах сортируются по дате публикации (новые — выше).
* Работает фильтрация по тегам, в том числе на странице избранного и на странице рецептов одного автора).
* Работает пагинатор (в том числе при фильтрации по тегам).
* Обрабатывается ошибка 404.

#### Инфраструктура

* Проект работает с СУБД PostgreSQL.
* Проект запущен на сервере в Яндекс.Облаке в трёх контейнерах: nginx, PostgreSQL и Django+Gunicorn.
* Контейнер с проектом обновляется на Docker Hub.
* В nginx настроена раздача статики, остальные запросы переадресуются в Gunicorn.
* Данные сохраняются в volumes.


## Готовясь к запуску

Эти инструкции позволят вам запустить копию проекта на вашем локальном компьютере в целях разработки и тестирования.
Образ postgres [DockerHub](https://hub.docker.com/_/postgres).
Образ nginx [DockerHub](https://hub.docker.com/_/nginx).

## Требования

Перед запуском работы проверьте наличие 
[Python](https://www.python.org/downloads/),
[Django](https://www.djangoproject.com/), 
[Docker](https://www.docker.com/).

## Установка

*Клонируйте репозиторий на локальный компьютер. 
Выполните сборку контейнера.*
```
$ docker-compose build
```

*Запуск docker-compose.*
```
$ docker-compose up
```
При создании контейнера миграции выполнятся автоматически.

## Использование контейнера.

*Создание суперпользователя и инициализация данных.*

```sh
$ docker-compose exec web  python manage.py collectstatic
$ docker exec -it <CONTAINER ID> python manage.py makemigrations
$ docker exec -it <CONTAINER ID> python manage.py migrate
$ docker exec -it <CONTAINER ID> python manage.py createsuperuser
$ docker exec -it <CONTAINER ID> python manage.py loaddata fixtures.json
```
## Выключение контейнера.
```
docker-compose down
```
## Удаление контейнеров.
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
>>>>>>> cc2f3236586dfc558d7e4d822fca06c284882310
