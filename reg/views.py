from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Event, CustomUser
from .forms import LoginForm, SignupForm, EventForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# home page for user log in
def index(request):
    if request.user.is_authenticated:
        # redirect to dashboard upon successful login
        return HttpResponseRedirect('/dashboard')
    else:
        return render(request, "login.html") 

# function for user authentication   
def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect("/dashboard")
    else:
        return HttpResponseRedirect("/")

# function that signs users up
def createUser(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = CustomUser.objects.create_user(username=username, email=email, password=password)
    user.save()
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect("/dashboard")
    else:
        return HttpResponseRedirect("/")

# renders sign up page
def signup(request):
    return render(request, "signup.html")    

# log out page
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# event viewing page
def dashboard(request):
    if request.user.is_authenticated:
        event_list = Event.objects.order_by('-event_time')
        context = {'event_list': event_list}
        return render(request, 'dashboard.html', context)
    else:
        return HttpResponseRedirect("/login")

# renders event registration page
def registration(request):
    return render(request, 'registration.html')

# function handling event registration
def register(request):
    if request.user.is_authenticated:
        eventname = request.POST('eventname')
        #filter returns query set
        event = Event.objects.filter(event_name=eventname)[0]
        request.user.user_attending_events.add(event)
    else:
        return HttpResponseRedirect('/login')

# event creation page
def create_event(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EventForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.timestamp = timezone.now()
                model_instance.save()
                return redirect('/dashboard')
        else: 
            form = EventForm() 
            return render(request, "create-event.html", {'form': form})
    else:
        return HttpResponseRedirect("/login")


