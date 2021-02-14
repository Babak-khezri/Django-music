from django.shortcuts import render, HttpResponse
from .models import Music
from artist.models import Artist
from django.core.paginator import Paginator


# Create your views here.


def home(request):
    return render(request, 'music/index.html')


def music_list(request, page=1):
    music_list = Music.objects.all()
    paginator = Paginator(music_list, 3)
    musics = paginator.get_page(page)
    context = {
        'musics': musics,
        'pages': paginator,
        'current_page': page,
    }
    return render(request, 'music/music-list.html', context)


def search_list(request, page=1):
    keyword = request.POST.get('search')
    if keyword != '':
        artists = search_function(keyword, Artist.objects.all())
        musics = search_function(keyword, Artist.objects.all())
        context = {
            'artists': artists,
            'musics': musics,
        }
        return render(request, 'music/search-list.html', context)
    from django.core.exceptions import ValidationError
    raise ValidationError(request,'hello')


def search_function(keyword, objects):
    object_list = []
    for obj in objects:
        if keyword.lower() in obj.name.lower():
            object_list.append(obj)
    return object_list
