from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostsTestCase(TestCase):
    """Test for show_post page"""
    def test_view(self):
        path = reverse('posts:show_post')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/show_post.html')


