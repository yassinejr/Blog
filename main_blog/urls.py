from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('article/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('article/<int:pk>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<str:cats>/', category_view, name='category_view'),
    path('add_category/', CategoryCreateView.as_view(), name='add_category'),
    path('category/edit/<int:pk>', CategoryUpdateView.as_view(), name='update_category'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='delete_category'),
    path('like/<int:pk>', like_post, name='like_post'),
    path('add_comment/', CommentCreateView.as_view(), name='add_comment'),
]