from django.urls import path, re_path
from django.contrib import admin
from main import views
from .views import (
    welcome,
    create_project,
    project_detail,
    project_list,
    project_update,
    project_delete,
    project_signin,
    project_signup,
    project_logout,
    user_profile
)

app_name = 'main'

urlpatterns = [
    path('', welcome, name='home'),
    path('list', project_list, name="list"),
    path('create', create_project, name='create'),
    path('profile', user_profile, name='profile'),
    path('signin', project_signin, name='signin'),
    path('signup', project_signup, name='signup'),
    path('logout', project_logout, name='logout'),
    re_path(r'^(?P<slug>[\w-]+)/detail/$', project_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', project_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', project_delete, name='delete'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/project/', views.ProjectList.as_view()),
]
