from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *


# def home(request):
#     posts = Post.objects.all()
#     context = {'post', posts}
#     return render(request, 'home.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'main_blog/home.html'
    ordering = ['-posted_at']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'main_blog/article_details.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main_blog/add_post.html'
    # fields = '__all__' because we add form_class


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'main_blog/update_post.html'


class PostDeleteView(DeleteView):
    model = Post
    form_class = DeletePostForm
    template_name = 'main_blog/delete_post.html'
    success_url = reverse_lazy('home')
