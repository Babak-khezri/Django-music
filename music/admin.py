from django.contrib import admin
from .models import Music

admin.site.site_header = 'سایت موزیک Musician'

# Register your models here.


class MusicAdmin(admin.ModelAdmin):
    list_display = ['name', 'user','image_tag','artist_to_str', 'upload_date']  # Show in admin panel
    search_fields = ('name',)
    list_filter = (['name', 'artist'])  # make filter


admin.site.register(Music,MusicAdmin)
