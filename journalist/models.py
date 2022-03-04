from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)


class Journalist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dream_name = models.CharField(max_length=10, null=True)
    bio = models.TextField(max_length=255)

    def __str__(self):
        return self.dream_name


