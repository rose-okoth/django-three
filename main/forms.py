from django import forms
from .models import Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "image",
            "link",
            "publish",   
        ]

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')