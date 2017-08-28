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
    


