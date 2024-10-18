from django.contrib import admin
from django.urls import include, path

from api_rest import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<int:idade>', views.get_by_idade),
    path('user/<str:apelido>', views.get_by_apelido),
    path('data/', views.user_manager, name='user_manager'),  # Rota para user_manager

]

