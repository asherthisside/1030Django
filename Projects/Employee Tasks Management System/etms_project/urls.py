from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', include('etms_app.urls')),
    path('admin/', include('admin_app.urls')),
]
