from django.urls import path
from .views import artist_list,artist_music_list
app_name = 'artist'

urlpatterns = [
  path('artist-list/', artist_list, name='artist_list'),
  path('artist-list/page/<int:page>', artist_list, name='artist_list'),
  path('artist-music-list/<int:pk>',artist_music_list, name='artist_music_list'),
  path('artist-music-list/<int:pk>/page/<int:page>',artist_music_list, name='artist_music_list'),

]