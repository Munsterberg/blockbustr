from django.db import models

# Create your models here.
class Movie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return self.author