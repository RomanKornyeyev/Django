from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

def index(request):
    preguntas = Question.objects.all()
    return render(request, "aplicacion/index.html", {
        'preguntas' : preguntas
    })

def detalle(request, id):
    pregunta = Question.objects.get(id=id)
    return render(request, "aplicacion/detalle.html", {
        'pregunta' : pregunta,
        'opciones' : Choice.objects.filter(question = pregunta)
    })

def votos(request, id):
    pregunta = get_object_or_404(Question, id=id)
    try:
        seleccionada = pregunta.options.get(id=request.POST['opcion'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'aplicacion/detalle.html', {
            'pregunta': pregunta,
            'error_message': "You didn't select a choice.",
        })
    else:
        seleccionada.votes += 1
        seleccionada.save()

        return HttpResponseRedirect(reverse('aplicacion:resultados', args=(pregunta.id,)))

def resultados(request, id):
    pregunta = Question.objects.get(id=id)
    return render(request, "aplicacion/resultados.html", {
        "pregunta" : pregunta,
        "opciones" : Choice.objects.filter(question = pregunta)
    })