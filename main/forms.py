from django import forms
from .models import Project,Profile,Review
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


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("design_rating", "usability_rating", "content_rating")