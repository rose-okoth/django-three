from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
# from .models import Post
# from .forms import PostForm, RegistrationForm
from django.contrib.auth import authenticate, logout,login
# from .email import send_welcome_email
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

# def create_project(request):
