from django.db import models
import datetime
from django.utils import timezone


class Fib_data(models.Model):
    number = models.IntegerField(null=True,blank=True)
    fib_list = models.TextField(null=True,blank=True)
    duretion = models.TextField(null=True,blank=True)
    date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return str(self.duretion)
