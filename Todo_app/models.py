from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    datetime=models.DateTimeField(default=datetime.datetime.today)
    def __str__(self):
        return self.name