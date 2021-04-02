from django.urls import path, re_path
from django.contrib import admin
from .views import (
    welcome,
    create_project,
    project_detail,
)

app_name = 'main'

urlpatterns = [
    path('', welcome),
    path('create', create_project, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/detail/$', project_detail, name='detail'),
]
