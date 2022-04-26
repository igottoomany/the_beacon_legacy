from django.shortcuts import render
from django.http import HttpResponse
from journalist.models import Post
from django.template import loader

def index(request):
    template = loader.get_template("article.html")
    context = {}

    return HttpResponse(template.render(context, request))
