from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.blog_posts, name='wordscramble'),
    url(r'^posts/(?P<article_id>[0-9]+)$', views.post_view, name='post-view')

]
