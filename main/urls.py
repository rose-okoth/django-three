from django.urls import path, re_path
from django.contrib import admin
from .views import (
    welcome,
    create_project,
    project_detail,
    project_list,
    project_update,
    project_delete
)

app_name = 'main'

urlpatterns = [
    path('', welcome, name='home'),
    path('list', project_list, name="list"),
    path('create', create_project, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/detail/$', project_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
]
