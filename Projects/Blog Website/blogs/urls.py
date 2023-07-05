from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:id>', views.single),
    path('signup', views.signup),
    path('login', views.login),
    path('logout', views.logout),
    path('author_reg', views.author_reg),
    path('author_dashboard', views.author_dashboard),
    path('author_add_blog', views.author_add_blog),
    path('author_update_blog/<int:pk>', views.author_update_blog),
    path('author_delete_blog/<int:pk>', views.author_delete_blog),
    path('category/<str:name>', views.category_wise),
]