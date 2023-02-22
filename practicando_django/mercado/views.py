from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

# Create your views here.
def index(request):
    preguntas = Question.objects.all()
    return render(request, "mercado/index.html", {
        "preguntas" : preguntas
    })

def detalle(request, id):
    pregunta = Question.objects.get(id=id)
    return render(request, "mercado/detalle.html", {
        "pregunta" : pregunta,
        "opciones" : Choice.objects.filter(question = pregunta)
    })


def votos(request, id):
    pregunta = Question.objects.get(id=id)
    try:
        opcionElegida = pregunta.options.get(id=request.POST["opcion"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "mercado/detalle.html", {
            "pregunta" : Question.objects.get(id=id),
            "opciones" : Choice.objects.filter(question = pregunta),
            "error" : "Error al enviar"
        })
    else:
        opcionElegida.votes += 1
        opcionElegida.save()

        return HttpResponseRedirect(reverse('mercado:resultados', args=(pregunta.id,)))

def resultados(request, id):
    pregunta = Question.objects.get(id=id)
    return render(request, "mercado/resultados.html", {
        "pregunta" : pregunta,
        "opciones" : Choice.objects.filter(question = pregunta)
    })