from django.conf.urls import path
from django.contrib import admin
from .views import (
    welcome,
    create_project,
)

app_name = 'main'

urlpatterns = [
    path('', welcome),
    path('create', create_project, name='create')
]
