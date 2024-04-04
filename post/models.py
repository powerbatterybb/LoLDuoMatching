from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
