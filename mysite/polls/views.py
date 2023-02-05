from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/index.html', context)

def detalle_question(request, question_text):
    preguntaORM = Question.objects.get(question_text=question_text)
    context = {'preguntaTemplate': preguntaORM}
    return render(request, 'polls/question.html', context)