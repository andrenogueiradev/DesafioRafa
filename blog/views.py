from blog.models import Post
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post

#def home(request):
#    return render (request, 'home.html', {})

class HomeView(ListView):
    model= Post
    template_name = 'home.html'

def CategoryView(request, cats): 
    category_posts = Post.objects.all()
    return render(request, 'categories.html', {'cats': cats, 'category_posts':category_posts})   


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


