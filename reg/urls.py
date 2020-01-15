from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-event', views.create_event, name='create-event'),
    path('signup', views.signup, name='signup')
]