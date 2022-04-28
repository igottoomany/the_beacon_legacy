from django.shortcuts import render
from django.http import HttpResponse
from journalist.models import Post, Journalist
from django.views.generic import ListView
from django.template import loader


def article(request, article_id):
    context = {
        'post': Post.objects.get(pk=article_id),
    }
    return render(request, 'article.html', context)


class Index(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']
