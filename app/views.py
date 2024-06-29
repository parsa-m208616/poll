from django.shortcuts import render
from .models import *


def index(request):

    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'index.html', context)

def question_detail(request, question_id):

    return render(request, 'question_detail.html')

