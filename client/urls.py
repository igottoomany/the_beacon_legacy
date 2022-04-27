from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index.as_view(template_name="index_backend.html"), name='index'),
    path('article/<int:article_id>', views.article, name='article')
]
