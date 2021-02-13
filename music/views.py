from django.shortcuts import render
from .models import Music
from django.core.paginator import Paginator

# Create your views here.


def home(request):
  return render(request, 'music/index.html')


def music_list(request,page=1):
  music_list = Music.objects.all()
  paginator = Paginator(music_list,3)
  musics = paginator.get_page(page)
  context = {
    'musics' : musics,
    'pages' : paginator,
    'current_page': page,
  }
  return render(request, 'music/music-list.html',context)
