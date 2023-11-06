import django_filters
from .models import Movie, Book, Review

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            'title': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'rating': ['exact'],
            'director': ['exact', 'icontains'],
            'release_date': ['exact', 'gte', 'lte'],
            'genre': ['exact', 'icontains'],
            'length': ['exact', 'gte', 'lte'],
            'language': ['exact'],
            'country': ['exact', 'icontains']

        }

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'published_date': ['exact', 'gte', 'lte'],
            'genre': ['exact', 'icontains'],
            'language': ['exact'],
            'pages': ['exact', 'gte', 'lte'],
            'isbn': ['exact']
        }

class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = {
            'user': ['exact'],
            'content': ['exact', 'icontains'],
            'rating': ['exact'],
            'movie': ['exact'],
            'book': ['exact']
        }