from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, User, EventForm, SignupForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# home page for user log in
def index(request):
    

    return HttpResponse("This should be the home login page")

# user sign up page
def signup(request):
    form = SignupForm()    
    return render(request, 'signup.html', {'form': form})

# event viewing page
def dashboard(request):
    event_list = Event.objects.order_by('-event_time')
    context = {'event_list': event_list}
    return render(request, 'reg/dashboard.html', context)

# event creation page
def create_event(request):
    form = EventForm()    
    return render(request, 'create-event.html', {'form': form})


