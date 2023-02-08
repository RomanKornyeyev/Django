from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Noticia

def index(request):
    noticiasORM = Noticia.objects.all()
    context = {'noticiasTemplate': noticiasORM}
    return render(request, 'noticias/index.html', context)

def detalle_noticia(request, titulo):
    # noticiaORM = Noticia.objects.get(titulo=titulo)
    # context = {'noticiaTemplate': noticiaORM}
    # MANERA 2
    # quitamos el contexto para meterlo DIRECTAMENTE
    # return render(request,'noticias/detalle.html', {
    #     'noticiaTemplate': Noticia.objects.get(titulo=titulo),
    #     'publicidad': ['a', 'b', 'c']
    # })
    # MANERA 3
    # get_object_or_404 nos proporciona una función para hacerlo mucho más cómodo
    # Django de manera predeterminada en la excepcion 404 redirige al 404.html de los templates
    # es automagico
    return render(request,'noticias/detalle.html', {
        'noticiaTemplate': get_object_or_404(Noticia, titulo=titulo),
    })