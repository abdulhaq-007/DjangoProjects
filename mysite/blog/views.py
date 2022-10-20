from django.shortcuts import render
from .models import Category, Post, Comment
# Create your views here.

def homePage(request):
    posts = Post.objects.all()
    data = {
        'posts':posts,
    }
    return render(request, 'index.html', context=data)