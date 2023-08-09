from django.shortcuts import redirect
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('home/joinroom/', views.joinRoom),
    path('home/joinroom/redirectroom/', views.redirect)
]
