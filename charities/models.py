from django.db import models
from accounts.models import *


class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    EXP_CHOICE = [(0, 0), (1,1), (2,2)]
    experience = models.SmallIntegerField(choices=EXP_CHOICE, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50, default="Unnamed-Charity")
    reg_number = models.CharField(max_length=10, default='-1')

class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return user.charity_set.all()

    def related_tasks_to_benefactor(self, user):
        return user.benefactor_set.all()

    def all_related_tasks_to_user(self, user):
        q1 = user.benefactor.all()
        q2 = user.charity_set.all()
        q3 = Task.objects.all(state="Pending")
        return q1.union(q2).union(q3)

class Task(models.Model):
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.PROTECT, default=None)

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

    title = models.CharField(max_length=60, default="Unknown-Title")

    objects = TaskManager()



