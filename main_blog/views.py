from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


# def home(request):
#     posts = Post.objects.all()
#     context = {'post', posts}
#     return render(request, 'home.html', context)


class BaseView(ListView):
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

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            # post.likes.remove(self.request.user)
            liked = True
        # else:
        #     if self.request.user.is_authenticated:
        #         post.likes.add(self.request.user)
        #         liked = False
        #     else:
        #         raise Exception("Error")

        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        context['total_likes'] = total_likes
        context['liked'] = liked
        print(liked)
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'main_blog/add_category.html'

    # fields = '__all__' because we add form_class

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = EditCategoryForm
    template_name = 'main_blog/update_category.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    form_class = DeleteCategoryForm
    template_name = 'main_blog/delete_category.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['categories_list'] = Category.objects.all()
        return context


def category_view(request, cats):
    category_posts = Category.objects.filter(category_name=cats).values_list('category_name', 'category_name')
    categories_list = Category.objects.all()
    categories_all = []
    for c in category_posts:
        categories_all.append(c)
    categories = [x[0] for x in categories_all]
    posts = Post.objects.filter(category__category_name=categories[0]).order_by('-posted_at')
    context = {
        'categories_list': categories_list,
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


def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))