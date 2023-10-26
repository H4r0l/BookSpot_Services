from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    rating = models.IntegerField()
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    length = models.IntegerField()
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    pages = models.IntegerField()
    isbn = models.CharField(max_length=13)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()
    # Relaciona la reseña con una película o un libro (uno a uno)
    movie = models.OneToOneField(Movie, null=True, blank=True, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, null=True, blank=True, on_delete=models.CASCADE)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user}'s wishlist"
    