from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=120, default='no category')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.category_name)

    def get_absolute_url(self):
        from django.urls import reverse
        # return reverse('article-detail', args=[str(self.id)])
        return reverse('base')


class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)

    def get_absolute_url(self):
        from django.urls import reverse
        # return reverse('article-detail', args=[str(self.id)])
        return reverse('home')

    def total_likes(self):
        return self.likes.count()