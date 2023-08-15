from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    probation = models.BooleanField(default=True)
    position = models.CharField(max_length=69)


class Order(models.Model):
    task_id = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
