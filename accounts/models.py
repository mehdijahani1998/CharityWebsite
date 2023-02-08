from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    adress = models.TextField()
    age = models.PositiveSmallIntegerField()
    
    description = models.TextField()

    date_joined = models.DateTimeField(auto_now_add=True)

    GENDER_CHOICES = (
        ("M", "male"),
        ("F", "female"),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    phone = models.CharField(max_length=15)

