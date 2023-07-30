from django.shortcuts import render
from .models import Event


def get_func(request):
    event = Event.objects.last()
    return render(request, 'blog_server/get.html', {'event': event})
