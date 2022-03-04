from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('contactUs', views.contactUs, name="contactUs"),
    path('hireUs', views.hireUs, name="hireUs"),
    path('mobileApps', views.mobileApps, name="mobileApps"),




]
