from django.contrib import admin
from django.urls import include, path

from api_rest import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
]
