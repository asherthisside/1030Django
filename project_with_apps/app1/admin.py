from django.contrib import admin
from .models import Employee_manager

# Register your models here.
admin.site.register(Employee_manager)


# App Create -> Register in settings.INSTALLED_APPS -> Create Model -> Make migrations -> Migrate -> Register models in admin.py