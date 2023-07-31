from django.urls import path
from .views import ProductClassView

urlpatterns = [
    path('products', ProductClassView.as_view()),
    path('products/<int:pk>', ProductClassView.as_view()),
]
