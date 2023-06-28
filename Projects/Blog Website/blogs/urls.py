from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:id>', views.single),
    path('signup', views.signup),
    path('login', views.login),
    path('logout', views.logout),
]
