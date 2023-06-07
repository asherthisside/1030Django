from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('app1_intro', views.intro)
]
