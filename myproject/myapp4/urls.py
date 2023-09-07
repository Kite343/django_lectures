from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('user/add/', views.user_form, name='user_form'),
    path('forms/', views.many_fields_form, name='many_fields_form'),
    path('user/', views.add_user, name='add_user'),
    path('upload/', views.upload_image, name='upload_image'),
]