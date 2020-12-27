from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'header_image', 'snippet', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the title of the post'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'author', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-select'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'header_image', 'snippet', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the title of the post'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class DeletePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the title of the post'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)
        widgets = {
            'category_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'enter the name of the category'}),
        }


class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)
        widgets = {
            'category_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'enter the name of the category'}),
        }


class DeleteCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)
        widgets = {
            'category_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'enter the name of the category'}),
        }


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'comment',)
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'author', 'type': 'hidden'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
