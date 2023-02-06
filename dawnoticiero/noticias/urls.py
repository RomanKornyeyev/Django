from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='noticias_index'),
    path('<str:titulo>/', views.detalle_noticia, name='noticias_detalle')
]