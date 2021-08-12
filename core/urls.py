from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import TestForm, Results, CarForm, CarResults, registerUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register', registerUser, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('form', TestForm.as_view(), name='form'),
    path('results', Results.as_view(), name='results'),
    path('car_form', CarForm.as_view(), name='car_form'),
    path('car_results', CarResults.as_view(), name='car_results')
]
