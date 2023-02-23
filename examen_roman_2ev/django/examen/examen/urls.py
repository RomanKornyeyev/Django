from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('incidencias/', include('incidencias.urls')),
    path('admin/', admin.site.urls),
]