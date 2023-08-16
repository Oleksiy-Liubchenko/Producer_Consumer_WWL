import random
from producer_consumer_app.models import Order, Employee

from celery import shared_task

#docker run -d -p 6379:6379 redis
# celery -A Producer_Consumer_WWL worker -l INFO

# if without redis docker command error:  ERROR/MainProcess] consumer: Cannot connect to redis://localhost:6379//: Error 10061 connecting to localhost:6379. Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение..
# Trying again in 2.00 seconds... (1/100)

# from producer_consumer_app.tasks import count_orders
# pip install eventlet
# celery -A Producer_Consumer_WWL worker -l info -P eventlet
# celery -A Producer_Consumer_WWL beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

# @shared_task
# def count_orders():
#     return Order.objects.count()

# TODO: make upd 5 min, not 5 sec

@shared_task
def order_creation() -> None:
    random_employee = random.choice(
        list(Employee.objects.all())
    )

    def generate_numeric_id(length=8):
        numeric_chars = '0123456789'
        unique_id = ''.join(random.choice(numeric_chars) for _ in range(length))
        return unique_id

    Order.objects.create(
        task_id=generate_numeric_id(),
        name="Task",
        description="Description",
        employee=random_employee
    )

    return Order.objects.count()
