"""
URL configuration for TrendCart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Email import views

app_name="Email"
urlpatterns = [
    path('send_email/', views.send_custom_email, name='send_custom_email'),
    path('password_reset/', views.password_reset_request, name='password_reset_request'),
    path('reset_password/<str:token>/', views.password_reset_confirm, name='password_reset_confirm'),
]
