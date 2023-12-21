Интернет-магазин на Django ***Web_shop**. 

#### Доступ к проекту:
https://store-prod.ru/


**Описание**
Проект реализует интерфейс и функциональные возможности Интернет-магазина.

В **Web_shop** реализованы следующие возможности:
    - регистрация пользователя, в том числе через GitHub
    - подтверждение учетной записи через электронную почту
    - редактирование личной страницы пользователя
    - сортировка товаров по категориям
    - добавлене товаров в корзину и удаление из нее
    - оплата товаров через Stripe
    - отслеживание статуса покупки
    - хранение истории покупок


#### Стек технологий:
- Python 3.9
- Django 
- Celery -отложенные задачи
- Redis - кеширование
- Stripe - оплата

#### Запуск приложения.

Создание локального окружения

`python3.9 -m venv venv`

`source ../venv/bin/activate`


Установите зависимости из requirements.txt:

`pip install -r requirements.txt`

Выполните все необходимые миграции:

`python manage.py makemigrations`

`python manage.py migrate`

Заполняем базу данных:

`python manage.py loaddata products/fixtures/categories.json`

`python manage.py loaddata products/fixtures/goods.json`

Для доступа к панели администратора создайте администратора:

`python manage.py createsuperuser`

Запуск [Redis Server](https://redis.io/docs/getting-started/installation/):

`redis-server`

Запуск Celery

`celery -A store worker --loglevel=INFO`

Запустите приложение:

`python manage.py runserver`