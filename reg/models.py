from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField(default=datetime.date.today)
    event_time = models.TimeField()
    event_description = models.TextField()

    def __str__(self):
        return self.event_name

class CustomUser(AbstractUser):
    pass
    # use fields username, password and email
    user_attending_events = models.ManyToManyField(Event)

    def __str__(self):
        return self.user_email



