from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Artist
from music.models import Music
# Create your views here.


def artist_list(request, page=1):
    artist_list = Artist.objects.all()
    paginator = Paginator(artist_list, 10)
    artists = paginator.get_page(page)
    context = {
        'artists': artists,
    }
    return render(request, 'artist/artist-list.html', context)


def artist_music_list(request, pk, page=1):
    artist = get_object_or_404(Artist, pk=pk)
    music_list = Music.objects.filter(artist=artist)
    paginator = Paginator(music_list, 10)
    musics = paginator.get_page(page)
    context = {
        'musics': musics,
        'artist':artist,
        
    }
    return render(request, 'artist/artist-music-list.html', context)
