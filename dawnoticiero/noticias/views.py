from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Noticia

def index(request):
    noticiasORM = Noticia.objects.all()
    context = {'noticiasTemplate': noticiasORM}
    return render(request, 'noticias/index.html', context)

def detalle_noticia(request, titulo):
    noticiaORM = Noticia.objects.get(titulo=titulo)
    context = {'noticiaTemplate': noticiaORM}
    return render(request, 'noticias/detalle.html', context)