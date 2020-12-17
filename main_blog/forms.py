from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the title of the post'}),
            'author': forms.Select(attrs={'class': 'form-select'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the title of the post'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class DeletePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the title of the post'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
