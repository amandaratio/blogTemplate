from django.db import models
from django.utils import timezone

# blog

class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Category(models.Model):
    type = models.CharField(max_length=2);
    def __str__(self):
        return self.type

class Article(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateField()
    def publish(self):
        self.published = timezone.now
        self.save()
    def __str__(self):
        return self.title
    def next(self):
        if(self.id<Article.objects.count()):
            return 't'
        else:
            return 'f'
    def prev(self):
        if(self.id>1):
            return 't'
        else:
            return 'f'
    def next_id(self):
        if(self.id<Article.objects.count()):
            return self.id+1
        else:
            return self.id
    def prev_id(self):
        if(self.id>1):
            return self.id-1
        else:
            return self.id



