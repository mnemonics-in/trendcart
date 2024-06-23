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
from Order import views
app_name="Order"
urlpatterns = [
    path('/place_order/', views.place_order, name='place_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/<int:p>', views.order_detail, name='order_detail'),
    path('order_view/<int:p>', views.order_view, name='order_view'),
    path('/update_order_status/<int:p>', views.update_order_status, name='update_order_status'),
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),

]
