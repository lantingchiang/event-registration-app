from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Event

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')

class LoginForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


    