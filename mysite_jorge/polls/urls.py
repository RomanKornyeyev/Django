from django.urls import path, re_path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

app_name = 'polls'
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detalle'),
    path('<int:pk>/vote/', views.vote, name='vote'),
    path('<int:pk>/resultado/', views.ResultsView.as_view(), name='resultado')
]