from django.contrib import admin
from .models import Category, Blog, Author 

# Register your models here.
admin.site.register([Category, Blog, Author])