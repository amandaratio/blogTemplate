from django.shortcuts import render
from .models import Article
from django.utils import timezone


def blog_posts(request):
    words = Article.objects.filter(published__lte=timezone.now()).order_by('published')
    return render( request, 'blog/blog_posts.html', {'words': words})
