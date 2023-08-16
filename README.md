"# Producer_Consumer_WWL" 

-celery -A Producer_Consumer_WWL worker -l info -P eventlet
-celery -A Producer_Consumer_WWL beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler