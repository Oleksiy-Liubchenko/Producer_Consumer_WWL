import random

from celery import shared_task

from producer_consumer_app.models import Order, Employee


@shared_task
def order_creation() -> None:
    random_employee = random.choice(
        list(Employee.objects.all())
    )

    def generate_numeric_id(length=8):
        numeric_chars = "0123456789"
        unique_id = "".join(
            random.choice(numeric_chars) for _ in range(length)
        )
        return unique_id

    Order.objects.create(
        task_id=generate_numeric_id(),
        name="Task",
        description="Description",
        employee=random_employee,
    )

    return Order.objects.count()
