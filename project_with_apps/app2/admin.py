from django.contrib import admin
from .models import Employee, Student, Guest, Room

# Register your models here.
admin.site.register([Employee, Student, Guest, Room])