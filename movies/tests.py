from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from .models import Movie, Comment

# Create your tests here.

class MovieModelTests(TestCase):
    def test_movie_creation(self):
        movie = Movie.objects.create(
            title = "Jake's Home",
            description = "Jake's testing time movie!",
            image = "http://placehold.it/300x200"
        )
        now = timezone.now()
        self.assertLess(movie.created_at, now)

class CommentModelTest(TestCase):
    def test_comment_creation(self):
        movie = Movie.objects.create(
            title = "Movie for Comment",
            description = "Description for the comment movie",
            image = "blank",
        )

        comment = Comment.objects.create(
            author = "Jake",
            content = "This is a simple test comment, hello!",
            movie = movie,
        )
        now = timezone.now()
        self.assertLess(comment.created_at, now)

class MovieViewsTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title = "View Test Movie",
            description = "View Test Movie Description",
        )

        self.movie2 = Movie.objects.create(
            title = "View Test Movie 2",
            description = "View Test Movie Description 2",
        )

        self.comment = Comment.objects.create(
            author = "Ryan",
            content = "This is Ryan here.",
            movie = self.movie
        )

    def test_movie_list_view(self):
        res = self.client.get(reverse('movies:list'))
        self.assertEqual(res.status_code, 200)
        self.assertIn(self.movie, res.context['movies'])
        self.assertIn(self.movie2, res.context['movies'])
        self.assertTemplateUsed(res, 'movies/index.html')
        self.assertContains(res, self.movie.title)

    def test_movie_show_view(self):
        key = self.movie.id
        res = self.client.get(reverse('movies:show', args=[key]))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.movie, res.context['movie'])
        self.assertTemplateUsed(res, 'movies/show.html')
        self.assertContains(res, self.movie.title)

    def test_movie_new_view(self):
        res = self.client.get(reverse('movies:new'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'movies/new.html')
        self.assertContains(res, "Add New Movie")
