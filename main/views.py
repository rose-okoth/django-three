from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
from django.contrib.auth import authenticate, logout,login
# from .email import send_welcome_email
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def create_project(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Post Successfully Created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form":form,
    }
    return render(request,"new_project.html",context)

def project_detail(request,slug=None):
    instance = get_object_or_404(Project, slug=slug)
    share_string = quote_plus(instance.content)
    context = {
            "title":instance.title,
            "instance":instance,
            "share_string":share_string
        }

    return render(request,"project_detail.html",context)