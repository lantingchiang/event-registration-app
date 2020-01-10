from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_time = models.DateTimeField()
    event_description = models.TextField()

    class Meta:
        ordering = ['-event_time']

    def __str__(self):
        return self.event_name

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_comments = models.TextField()
    user_attending_events = models.ManyToManyField(Event)

    def __str__(self):
        return self.user_email