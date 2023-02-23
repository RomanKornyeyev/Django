from django.urls import path
from . import views

app_name = "incidencias"
urlpatterns = [
    path('listado/', views.listado, name='listado'),
    path('incidencias/<int:id>/<int:ide>/', views.formulario, name='formulario'),
]