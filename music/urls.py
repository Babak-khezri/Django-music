from django.urls import path
from .views import home, music_list,search_list

app_name = 'music'

urlpatterns = [
  path('', home, name='home'),
  path('music_list/', music_list, name='music_list'),
  path('music_list/page/<int:page>', music_list, name='music_list'),
  path('search_list/', search_list, name='search_list'),
  path('search_list/page/<int:page>', search_list, name='search_list'),

]
