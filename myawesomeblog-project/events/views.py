from django.shortcuts import render
from .models import Event
# from requests import request
# Create your views here.


def home(request):
    events = Event.objects
    return render(request, 'events/home.html', {'events': events})