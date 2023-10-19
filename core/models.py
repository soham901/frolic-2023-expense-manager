from django.db import models
from django.contrib.auth.models import User

class Expence(models.Model):
    title = models.CharField(max_length=255)
    amount = models.FloatField()
    date = models.DateField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Income(models.Model):
    title = models.CharField(max_length=255)
    amount = models.FloatField()
    date = models.DateField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title