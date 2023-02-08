from django.db import models
from accounts.models import *


class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    EXP_CHOICE = [(0, 0), (1,1), (2,2)]
    experience = models.SmallIntegerField(choices=EXP_CHOICE, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class Task(models.Model):
    pass    
