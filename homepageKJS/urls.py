"""
URL configuration for homepageCAPD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views
from saleapp import views as saleapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    path('api/register/', saleapp_views.register_user, name='register_user'),
    path('api/users/', saleapp_views.list_users, name='list_users'),  # new endpoint
    path('api/users/<int:pk>/', saleapp_views.user_detail, name='user_detail'),
    
    path('login/', saleapp_views.login_view, name='login'),

    path('logout/', saleapp_views.logout_view, name='logout_html'),
    path('users/', saleapp_views.users_html, name='users_html'),

]

#version carl