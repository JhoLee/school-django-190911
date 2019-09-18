from django.shortcuts import render
from .models import Question

# Create your views here.

def index(req):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(req, 'polls/index.html', context)
