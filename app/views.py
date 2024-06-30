from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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

def signup_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.save()

    return render(request, 'signup.html', {'form': form})

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

    return render(request, 'logout.html')

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse('invalid')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('invalid username or password')

    return render(request, 'login_page.html')

@api_view(['POST'])
def test_page(request):
    print(request.data)

    return Response({'message': 'Hello'}, status=status.HTTP_400_BAD_REQUEST)


