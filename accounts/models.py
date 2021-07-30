from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField()
    phonenum = models.IntegerField()
    major = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    portfolio_isPrivate = models.BooleanField(default=False)
