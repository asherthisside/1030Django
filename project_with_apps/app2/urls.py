from . import views
from django.urls import path

urlpatterns = [
    path('', views.explore),
    path('show_reel', views.show_reels),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete),
    path('add', views.add_employee)
]