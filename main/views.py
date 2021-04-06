from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from .models import Project,Profile
from .forms import ProjectForm, RegistrationForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import authenticate, logout,login
from .email import send_welcome_email
import datetime
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def create_project(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user.profile
        instance.save()
        messages.success(request, "Post Successfully Created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form":form,
    }
    return render(request,"new_project.html",context)

def project_detail(request,slug=None):
    instance = get_object_or_404(Project, slug=slug)
    share_string = quote_plus(instance.description)
    context = {
            "title":instance.title,
            "instance":instance,
            "share_string":share_string
        }

    return render(request,"project_detail.html",context)

def project_list(request):
    today = timezone.now().date()
    queryset_list = Project.objects.active().order_by("-timestamp")
    queryset = Project.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) 
            ).distinct()

    context = {
            "title":"Projects",
            "object_list":queryset
        }
    return render(request,"project_list.html", context)

def project_update(request, slug=None):

    '''Updating projects function'''

    instance = get_object_or_404(Project, slug=slug)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Project Updated!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "title":instance.title,
            "instance":instance,
            "form":form,
        }
    return render(request,"new_project.html",context) 

def project_delete(request, slug=None):

    '''Deleting projects function'''

    instance = get_object_or_404(Project, slug=slug)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("main:home")

def project_signup(request):

    '''User signup function'''

    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)

        if form.is_valid():
            user = form.save()

            raw_password = form.cleaned_data.get('password1')

            print(request.POST)

            user = authenticate(username=user.username, password=raw_password)
            name = request.POST["username"]
            email = request.POST["email"]
            send_welcome_email(name,email)
            # signin(request, user)

            return redirect("main:home")

    else:
        form = RegistrationForm()

    return render(request, "signup.html", {"form": form})


def project_signin(request):

    '''User signin function'''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    #   check credentials  
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:

                login(request, user)
                return redirect('main:home')
            else:
                # login(request, user)
                return render(request, 'login.html', {"error": "Your account id is not active"})

        else:
            return render(request, 'login.html', {"error": "Invalid username or password"})

    return render(request, 'login.html')

def project_logout(request):

    '''User logout function'''

    logout(request)
    return redirect('main:signin')

def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('main:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    profile = request.user.profile.project.all

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile
    }

    return render(request, 'profile.html', context)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)