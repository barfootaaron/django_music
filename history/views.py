from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Artist, Song


def index(request):
    artist_list = Artist.objects.all()
    context = {
        'artist_list': artist_list,
    }
    return render(request, 'history/index.html', context)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'history/detail.html', {'artist': artist})

def artist(request, artist_id):
    response = "You're looking at the results of artist %s."
    return HttpResponse(response % artist_id)
