from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def index(request):
    topics = Topic.objects.all()
    questions = Question.objects.all().order_by('-pub_date')

    q = request.GET.get('q') if request.GET.get('q') is not None else None

    if q is not None:
        questions = Question.objects.filter(topic__topic_text=q).order_by('-pub_date')

    context = {'questions': questions, 'topics': topics}

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

def create_question(request):


    context = {

    }
    return render(request, 'create_question.html', context)
