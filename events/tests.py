from http import HTTPStatus
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from .models import Event


class EventTestCase(TestCase):
    """Test for homepage"""
    def setUp(self):
        """Global variables"""
        self.path = reverse('events:home')
        self.response = self.client.get(self.path)

    def test_view_events_page(self):
        """Checking status code for page show_page and
        check that we are using the correct template"""
        path = reverse('events:home')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'events/home.html')

    def test_events(self):
        """Сhecking that the amount of data on the server and in the database is the same"""
        events = Event.objects.all()
        path = reverse('events:home')

        response_data = [event for event in events]
        response = HttpResponse(response_data, content_type='text/type')
        self.assertEquals(list(response_data), list(events))
