from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('parse/', include('parse.urls')),
    path('admin/', admin.site.urls),
]
