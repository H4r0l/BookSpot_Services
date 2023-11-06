from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Movie, Book, Review, Wishlist

class ModelsTestCase(TestCase):
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
        self.wishlist = Wishlist.objects.create(
            user=self.user,
            movie=self.movie,
            book=self.book
        )

    def test_movie_model(self):
        self.assertEqual(self.movie.title, 'Test Movie')
        self.assertEqual(self.movie.description, 'This is a test movie')
        self.assertEqual(self.movie.rating, 5)
        self.assertEqual(self.movie.director, 'Test Director')
        self.assertEqual(str(self.movie.release_date), '2022-01-01')
        self.assertEqual(self.movie.genre, 'Action')
        self.assertEqual(self.movie.length, 120)
        self.assertEqual(self.movie.language, 'English')
        self.assertEqual(self.movie.country, 'USA')

    def test_book_model(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.description, 'This is a test book')
        self.assertEqual(str(self.book.published_date), '2022-01-01')
        self.assertEqual(self.book.genre, 'Fiction')
        self.assertEqual(self.book.language, 'English')
        self.assertEqual(self.book.pages, 200)
        self.assertEqual(self.book.isbn, '1234567890123')

    def test_review_model(self):
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.content, 'This is a test review')
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.movie, self.movie)

    def test_wishlist_model(self):
        self.assertEqual(self.wishlist.user, self.user)
        self.assertEqual(self.wishlist.movie, self.movie)
        self.assertEqual(self.wishlist.book, self.book)