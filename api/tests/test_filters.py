from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Movie, Book, Review
from ..filters import MovieFilter, BookFilter, ReviewFilter

class FiltersTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='This is a test movie',
            rating=5,
            director='Test Director',
            release_date='2022-01-01',
            genre='Action',
            length=120,
            language='English',
            country='USA'
        )
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='This is a test book',
            published_date='2022-01-01',
            genre='Fiction',
            language='English',
            pages=200,
            isbn='1234567890123'
        )
        self.review = Review.objects.create(
            user=self.user,
            content='This is a test review',
            rating=4,
            movie=self.movie
        )

    def test_movie_filter(self):
        data = {
            'title': 'Test Movie',
            'description': 'This is a test movie',
            'rating': 5,
            'director': 'Test Director',
            'release_date': '2022-01-01',
            'genre': 'Action',
            'length': 120,
            'language': 'English',
            'country': 'USA'
        }
        queryset = Movie.objects.all()
        filtered_queryset = MovieFilter(data=data, queryset=queryset).qs
        self.assertEqual(len(filtered_queryset), 1)
        self.assertEqual(filtered_queryset[0], self.movie)

    def test_book_filter(self):
        data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'description': 'This is a test book',
            'published_date': '2022-01-01',
            'genre': 'Fiction',
            'language': 'English',
            'pages': 200,
            'isbn': '1234567890123'
        }
        queryset = Book.objects.all()
        filtered_queryset = BookFilter(data=data, queryset=queryset).qs
        self.assertEqual(len(filtered_queryset), 1)
        self.assertEqual(filtered_queryset[0], self.book)

    def test_review_filter(self):
        data = {
            'user': self.user.id,
            'content': 'This is a test review',
            'rating': 4,
            'movie': self.movie.id
        }
        queryset = Review.objects.all()
        filtered_queryset = ReviewFilter(data=data, queryset=queryset).qs
        self.assertEqual(len(filtered_queryset), 1)
        self.assertEqual(filtered_queryset[0], self.review)