from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    status = models.CharField(
        max_length=10, default="Drafted"
    )
    author_id = models.PositiveIntegerField()