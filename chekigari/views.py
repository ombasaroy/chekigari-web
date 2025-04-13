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

def wallet(request):
    return render(request, 'dashboard/wallet.html')


def reset_password(request):
    return render(request, 'dashboard/resetpassword.html')


def change_password(request):
    return render(request, 'dashboard/changepassword.html')


def my_profile(request):
    return render(request, 'dashboard/profile.html')


def vehicle_report(request):
    return render(request, 'dashboard/vehicle-report.html')


def user_logout(request):
    return render(request, 'dashboard/logout.html')


