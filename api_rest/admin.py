from django.contrib import admin

# Register your models here.

# Importar nossos models
from .models import User

admin.site.register(User)