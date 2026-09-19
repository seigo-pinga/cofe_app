from django.db import models
from django.utils import timezone

class Coffee(models.Model):
    date = models.DateTimeField(default=timezone.now)
    bean_amount = models.IntegerField()
    bean_grind = models.CharField(max_length=10)
    bean_rost = models.CharField(max_length=10)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    weather = models.CharField(max_length=10)
    atmospheric_pressure = models.IntegerField()