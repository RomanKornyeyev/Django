from django.urls import path
from . import views

app_name = "aplicacion"
urlpatterns = [
    path('', views.index, name='index'),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
]