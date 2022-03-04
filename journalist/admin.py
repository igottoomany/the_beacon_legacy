from django.contrib import admin
from .models import Journalist, Post

admin.site.register(Post)
admin.site.register(Journalist)
