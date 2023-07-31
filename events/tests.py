from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class EventTestCase(TestCase):
    """Test for homepage"""
    def test_view(self):
        path = reverse('events:home')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'events/home.html')
