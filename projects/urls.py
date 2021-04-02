from django.contrib import admin
from django.urls import path
from main.views import welcome


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
