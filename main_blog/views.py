from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


# def home(request):
#     posts = Post.objects.all()
#     context = {'post', posts}
#     return render(request, 'home.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
