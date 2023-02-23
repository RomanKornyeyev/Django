from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Linea, Estacion, Incidencia
from django.urls import reverse

# Create your views here.
def listado(request):
    lineas = Linea.objects.all()
    estaciones = Estacion.objects.all()
    return render(request, "incidencias/listado.html", {
        "lineas" : lineas,
        "estaciones" : estaciones
    })

def formulario(request, id, ide):
    linea = Linea.objects.get(id=id)
    estacion = Estacion.objects.get(id=ide)
    return render(request, "incidencias/formulario.html", {
        "estacion" : estacion,
        "linea" : linea
    })

def envio(request, id, ide):
    linea = Linea.objects.get(id=id)
    estacion = Estacion.objects.get(id=ide)
    try:
        texto = Incidencia.estaciones.get(id=request.POST["texto"])
    except(KeyError, Incidencia.DoesNotExist):
        return render(request, "mercado/detalle.html", {
            "linea" : linea,
            "estacion" : estacion,
            "error" : "Error al enviar"
        })
    else:
        texto.texto = request.POST["texto"]
        texto.save()

        return HttpResponseRedirect(reverse('mercado:resultados', args=(estacion.id,)))

