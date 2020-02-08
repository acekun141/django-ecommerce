from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from uuid import uuid4


class Customer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customer_avatar', default=settings.BASE_AVATAR)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email


class Bill(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid4())
    products = models.CharField(max_length=100)
    prices = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return str(self.uuid)