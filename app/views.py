from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def index(request):

    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'index.html', context)

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choices = question.choice_set.all()

    if request.method == 'POST':
        the_choice = choices.get(choice_text=request.POST['choice'])
        the_choice.votes += 1
        the_choice.save()

    context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'question_detail.html', context)

