from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def user_login(request):
    return render(request, 'dashboard/login.html')


def user_register(request):
    return render(request, 'dashboard/register.html')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
