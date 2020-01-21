from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth', views.auth, name='authenticate'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-event', views.create_event, name='create-event'),
    path('createUser', views.createUser, name='createUser'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('registration', views.registration, name='registration')
]