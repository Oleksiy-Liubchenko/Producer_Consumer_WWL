# Test-Task “Producer - Consumer”


Simple service with creation task need to be deleted with:

Django, Celery, PostgreSQL, Redis, Docker, pyTelegramBotAPI, bootstrap5, crispy_forms

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

fill ".env_copy" with your data and make file name just ".env" without "_copy"
-python manage.py makemigrations
-python manage.py migrate

or ask me for .env file with DB

python manage.py runserver

to login - http://127.0.0.1:8000/accounts/login/
user login - user1
user password - 12345678

to logout - http://127.0.0.1:8000/accounts/logout/
```
do not forget about ".env_copy" file change name to ".env"  and fill your data



To make periodic Tasks auto creation, make 2 terminal for your comfort:

First worker terminal command:
```
celery -A Producer_Consumer_WWL worker -l info -P eventlet
```
Second beat terminal command:
```
celery -A Producer_Consumer_WWL beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```


## Get Telegram notifications:
- Create new bot by BotFather and get token as TELEGRAM_BOT_TOKEN (in .env file)
- Get your CHAT_ID with https://t.me/userinfobot in your TG (in .env file)