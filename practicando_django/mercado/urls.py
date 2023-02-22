from django.urls import path
from . import views

app_name="mercado"
urlpatterns=[
    path("", views.index, name="index"),
    path("detalle/<int:id>/", views.detalle, name="detalle"),
    path("resultados/<int:id>/", views.resultados, name="resultados"),
    path("votos/<int:id>", views.votos, name="votos"),
]