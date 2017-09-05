from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.blog_posts, name='wordscramble'),
    url(r'^posts/(?P<article_id>[0-9]+)$', views.post_view, name='post-view'),
    url(r'^posts/(?P<new_id>[0-9]+)$', views.prev_view, name='prev-view'),
    url(r'^posts/(?P<new_id>[0-9]+)$', views.next_view, name='next-view')

]
