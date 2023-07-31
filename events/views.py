from django.shortcuts import render
from .models import Event


def home(request):
    """Homepage"""
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})
