from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path('signup', views.signup),
    path('dashboard', views.dashboard),
    path('employees', views.employees),
    path('tasks', views.tasks),
]
