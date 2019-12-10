from django.contrib import admin
from django.urls import path
from scrapperapp.views import home, bootcamp

urlpatterns = [
    path('home/', home),
    path('bootcamp/', bootcamp)
]
