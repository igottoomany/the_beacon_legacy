from django.shortcuts import render
from django.http import HttpResponse
from journalist.models import Post, Journalist
from django.template import loader

def index(request):
    template = loader.get_template("article.html")
    context = {
        'post': Post.objects.get(pk=1),
    }

    return HttpResponse(template.render(context, request))
