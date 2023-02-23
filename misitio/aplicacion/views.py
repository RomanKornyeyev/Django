from django.shortcuts import render
from django.http import HttpResponse
from .models import Biblioteca, Libro

# Create your views here.
def index(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, "aplicacion/index.html", {
        'bibliotecas' : bibliotecas
    })

def detalle(request, id):
    biblioteca = Biblioteca.objects.get(id=id)
    return render(request, "aplicacion/detalle.html", {
        "biblioteca" : biblioteca,
        "libros" : Libro.objects.filter(bibliotecas=biblioteca)
    })