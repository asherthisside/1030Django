from django.contrib import admin
from .models import Employee, Task

# Register your models here.
admin.site.register([Employee, Task])