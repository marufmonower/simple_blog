from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post_create/',views.post_create,name = 'post_create'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]