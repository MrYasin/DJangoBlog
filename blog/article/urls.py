from django.contrib import admin
from django.urls import path

app_name = "article"

from article import views

urlpatterns = [
    path('create/', views.index, name = "index"),

]




