from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='polls_index'),
    path('<str:question_text>/', views.detalle_question, name='polls_detalle_question')
]