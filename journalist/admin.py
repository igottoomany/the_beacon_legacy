from django.contrib import admin
from .models import Journalist, Post, Category

admin.site.register(Post)
admin.site.register(Journalist)
admin.site.register(Category)
