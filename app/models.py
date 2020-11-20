from django.db import models
from django.contrib.auth.models import User


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    about = models.TextField()
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    headshot = models.ImageField(upload_to='author_headshots')
    last_login = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    about = models.TextField()
    publication_date = models.DateField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
