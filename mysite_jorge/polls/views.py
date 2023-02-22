from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 2

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')

"""
def index(request):
    # ORM Pedir preguntas
    preguntas = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {
        'latest_question_list': preguntas,
        'titulo': 'hola mundo'
    })
"""

class CosasDePreguntas(generic.DetailView):
    model = Question
    context_object_name = 'encuesta'

class DetailView(CosasDePreguntas):
    template_name = 'polls/detalle.html'

"""
def detalle(request, id):
    # Pide al ORM la pregunta con ese id
    # y si no la encuentras, levanta una excepción 404
    encuesta = get_object_or_404(Question, pk=id)
    return render(
        request,
        'polls/detalle.html',
        {
            'encuesta': encuesta
        }
    )
"""



def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)


    try:
        selected_choice = question.options.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detalle.html', {
            'encuesta': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return HttpResponseRedirect(f"/polls/{question.id}/resultado/")
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:resultado', args=(question.pk,)))




class ResultsView(CosasDePreguntas):
    template_name = 'polls/resultados.html'

"""
def resultado(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'polls/resultados.html', {
        'encuesta': question
    })
"""



from rest_framework import viewsets
from .serializer import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('pub_date')
    serializer_class = QuestionSerializer