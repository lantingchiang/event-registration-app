from django.db import models
from django.forms import ModelForm

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_description = models.TextField()

    def __str__(self):
        return self.event_name

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_comments = models.TextField()
    user_attending_events = models.ManyToManyField(Event)

    def __str__(self):
        return self.user_email

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

