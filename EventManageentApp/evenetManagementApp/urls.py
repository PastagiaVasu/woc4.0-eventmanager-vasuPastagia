from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('event_registratition/', views.eventReg, name="event_registratition"),
    path('event_registratition/insert/', views.eventInsert, name="eventInsert"),
    path('event/', views.event, name="event"),
    path('participant/', views.participant, name="participant"),
    path('participant_registratition/', views.participantReg, name="participant_registratition"),
    path('participant_registratition/insert', views.participantInsert, name="participantInsert"),
]
