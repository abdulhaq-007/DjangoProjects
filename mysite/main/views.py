from django.shortcuts import render

from main.models import Question

# Create your views here.

def home(request):
    question = Question.objects.all()
    context = {
        'questions':question,
    }
    return render(request, 'index.html', context)

def result(request):
    return render(request, 'result.html')

def contact(request):
    return render(request, 'contact.html')       