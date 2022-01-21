
from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.urls
from mainAuthApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(django.contrib.auth.urls)),
    path('', views.Homepage, name="home"),
    path('register', views.register, name="register"),
]
