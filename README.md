# Test-Task “Producer - Consumer”


Simple service with creation task need to be deleted with:

Django, Celery, PostgreSQL, Redis, Docker, pyTelegramBotAPI

## Task:
https://drive.google.com/file/d/1U5Qe1yvngefp1lfy1gqE6nhi3OOc0UbT/view?usp=sharing


## Installing:
```angular2html
git clone https://github.com/Oleksiy-Liubchenko/Producer_Consumer_WWL.git
cd Producer_Consumer_WWL
python -m venv venv
source venv/bin/activate #for iOS or Linux
venv/Scripts/activate #for Windows
pip install -r requirements.txt
fill ".env_sample" with your data and make file name just ".env" without "_sample"
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

user login - user1
user password - 12345678
```
do not forget about ".env_sample" file change name to ".env"  and fill your data
```
python manage.py migrate
python manage.py runserver
```


To make periodic Tasks make 2 terminal for your comfort:

First terminal command:
```
-celery -A Producer_Consumer_WWL worker -l info -P eventlet
```
Second terminal command:
```
-celery -A Producer_Consumer_WWL beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## Run with Docker:
```angular2html
docker-compose build
docker-compose up
```

## Get Telegram notifications:
- Create new bot by BotFather and get token as TELEGRAM_BOT_TOKEN
- Get your CHAT_ID with https://t.me/userinfobot in your TG