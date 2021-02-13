from django.urls import path
from .views import home, music_list

app_name = 'music'

urlpatterns = [
  path('', home, name='home'),
  path('music-list/', music_list, name='music-list'),
  path('music-list/page/<int:page>', music_list, name='music-list'),
]
