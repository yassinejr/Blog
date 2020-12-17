from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        from django.urls import reverse
        # return reverse('article-detail', args=[str(self.id)])
        return reverse('home')
