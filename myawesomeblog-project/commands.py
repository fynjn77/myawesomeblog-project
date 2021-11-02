# django-admin startproject myfirstproject #создаю проект в консоли
# cd myfirstproject #захожу в создавшуюся папку
# py manage.py runserver #запускаю сервер
# Ctrl+C #остановить сервер
# py manage.py startapp name_of_app
# py manage.py makemigrations #сделать миграцию мо дели
# py manage.py migrate #применить миграцию модели
# py manage.py createsuperuser #создаю админа


# pip install virtualenv
# virtualenv name_of_env
# name_of_env\Scripts\activate
# django-admin startproject myfirstproject #Создаю джанго проект
#на уровне name_of_env

# local
# git --version #Узнать текущую версию (если git стоит)
# git init #В папке проекта
# git status #Покажет, если что-то не отслеживается
# git add . #добавить все файлы, которые не отслеживаются
# git commit -m "commit message" #Сохраняю текующее состояние в git
#
#и комментарий к сохранению
# Для загрузки на github нужно на сайте создать репазиторий
# git remote add origin ссылка_на_репазиторий
# git branch -M main
# git push -u origin main # отправить на git


#PostgreSQL
# \! chcp 1251
# \du #
# \password postgres