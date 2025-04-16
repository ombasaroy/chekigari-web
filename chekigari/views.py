from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def user_login(request):
    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
        
    context = {
        "form": form
    }

    return render(request, 'dashboard/login.html', context)


def user_register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfuly")
            return redirect('login')
    
    else:
        form = CreateUserForm()

    context={
        "form": form
    }

    return render(request, 'dashboard/register.html', context)

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required(login_url='login')
def wallet(request):
    return render(request, 'dashboard/wallet.html')


def reset_password(request):
    return render(request, 'dashboard/resetpassword.html')


def change_password(request):
    return render(request, 'dashboard/changepassword.html')

@login_required(login_url='login')
def my_profile(request):
    return render(request, 'dashboard/profile.html')

@login_required(login_url='login')
def vehicle_report(request):
    return render(request, 'dashboard/vehicle-report.html')


def user_logout(request):

    if request.user.is_authenticated:  # Ensure user is logged in
        username = request.user.username  # Store username before logout
        logout(request)
        messages.info(request, f"{username} has logged out")  # Use f-string for cleaner formatting
    else:
        messages.warning(request, "You are not logged in")

    return redirect('login')  # Redirect to login page


