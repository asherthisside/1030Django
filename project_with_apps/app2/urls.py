from . import views
from django.urls import path

urlpatterns = [
    path('', views.explore),
    path('show_reel', views.show_reels)
]
