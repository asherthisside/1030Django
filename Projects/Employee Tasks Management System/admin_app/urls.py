from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('employees',views.employees ),
    path('tasks', views.tasks),
]
