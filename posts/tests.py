from http import HTTPStatus
from django.http import HttpResponse

from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostsTestCase(TestCase):
    """Test for show_post page"""
    fixtures = ['fixtures/posts.json']

    def test_view_posts_page(self):
        """Checking status code for page show_page and
         check that we are using the correct template"""
        path = reverse('posts:show_post')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/show_post.html')

    def test_posts_db(self):
        """Сhecking that the amount of data on the server and in the database is the same"""
        posts = Post.objects.all()
        path = reverse('posts:show_post')
        response_data = [post for post in posts]
        response = HttpResponse(response_data, content_type='text/type')
        self.assertEquals(list(response_data), list(posts))
