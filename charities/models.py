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
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.PROTECT)

    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)

    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    GENDER_CHOICES = (
        ("M", "male"),
        ("F", "female"),
    )

    gender_limit = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)

    STATE_CHOICE = (
        ("P", "Pending"),
        ("W", "Waiting"),
        ("A", "Assigned"),
        ("D", "Done"),
    )

    state = models.CharField(choices=STATE_CHOICE, max_length=1, default="P")

    title = models.CharField(max_length=60)