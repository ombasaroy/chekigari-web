from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('vehicle-report/', views.vehicle_report, name='vehicle-report'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('change-password/', views.change_password, name='change-password'),
]
