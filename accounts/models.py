from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(null= True, blank=True, max_length=50)

    GENDER_CHOICES = (
        ("M", "male"),
        ("F", "female"),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField(null=True, blank=True)
    last_name = models.CharField(null=True, blank=True, max_length=50)

    phone = models.CharField(max_length=15, null=True, blank=True)

    def get_full_name(self) -> str:
        return super().get_full_name()