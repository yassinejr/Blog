from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.views.generic.list import MultipleObjectMixin
from django.urls import reverse_lazy
from .models import *
from .forms import *


# def home(request):
#     posts = Post.objects.all()
#     context = {'post', posts}
#     return render(request, 'home.html', context)


class HomeView(ListView):
    template_name = 'main_blog/base.html'
    model = Category

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context


class HomeView(ListView):
    template_name = 'main_blog/home.html'
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Post.objects.order_by('-posted_at')


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'main_blog/article_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main_blog/add_post.html'
    # fields = '__all__' because we add form_class

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context

class PostUpdateView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'main_blog/update_post.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context

class PostDeleteView(DeleteView):
    model = Post
    form_class = DeletePostForm
    template_name = 'main_blog/delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'main_blog/category_details.html'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'main_blog/add_category.html'
    # fields = '__all__' because we add form_class


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = EditCategoryForm
    template_name = 'main_blog/update_category.html'


class CategoryDeleteView(DeleteView):
    model = Category
    form_class = DeleteCategoryForm
    template_name = 'main_blog/delete_category.html'
    success_url = reverse_lazy('home')


def category_view(request, cats):
    category_posts = Category.objects.filter(category_name=cats).values_list('category_name', 'category_name')
    categories_list = []
    for c in category_posts:
        categories_list.append(c)
    categories = [x[0] for x in categories_list]
    posts = Post.objects.filter(category__category_name=categories[0]).order_by('-posted_at')
    context = {
        'category': categories[0],
        'cats': cats,
        'posts': posts
    }
    print(posts)
    print(cats)
    print(categories)
    print(type(categories))
    print(type(category_posts))
    return render(request, 'main_blog/categories.html', context)
