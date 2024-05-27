from django.shortcuts import render

from .models import Question

# Create your views here.
def home(request):
    # return HttpResponse("welcome come")
    questions = Question.objects.all()
    return render(request, 'polls/home.html', {
        "questions": questions
    })

def vote(request, q_id):
    pass

def results(request, q_id):
    pass