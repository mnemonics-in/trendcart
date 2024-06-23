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
from Accounts import views
app_name="Accounts"
urlpatterns = [
    path('', views.index, name="index"),
    path('signup',views.signup,name="signup"),
    path('accounts/login/',views.user_login,name="login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('user_home',views.user_home,name="user_home"),
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('user_list',views.user_list,name="user_list"),
    path('user_detail/<int:user_id>', views.user_detail, name='user_detail'),
    path('user_detail/deactivate/<int:user_id>', views.deactivate_user, name='deactivate_user'),
    path('user_detail/activate/<int:user_id>', views.activate_user, name='activate_user'),
    path('user_detail/delete/<int:user_id>', views.delete_user, name='delete_user'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('profile', views.profile, name='profile'),
    path('update_profile/<int:p>', views.update_profile, name='update_profile'),
    path('change_password/<int:p>', views.change_password, name='change_password'),
    # path('product_detail/<int:p>', views.product_detail, name='product_detail'),
    # path('<int:user_id>/deactivate/', views.deactivate_user, name='deactivate_user'),
    # path('<int:user_id>/delete/', views.delete_user, name='delete_user'),
]
