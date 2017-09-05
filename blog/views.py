from django.shortcuts import render
from .models import Article
from django.views.generic import ListView
from django.utils import timezone
from django.shortcuts import render_to_response, get_object_or_404

def post_view(request, article_id):
    ind = 'blog/posts/post.html'
    post = Article.objects.get(pk=article_id)
    return render( request, ind, {'post':post})

def prev_view(request, new_id):
    ind = 'blog/posts/post.html'
    post = Article.objects.get(pk=new_id)
    return render( request, ind, {'post':post})

def next_view(request, new_id):
    ind = 'blog/posts/post.html'
    post = Article.objects.get(pk=new_id)
    return render( request, ind, {'post':post})

def blog_posts(request):
    words = Article.objects.filter(published__lte=timezone.now()).order_by('-published')
    return render( request, 'blog/blog_posts.html', {'words': words})


