from django.db import models
from account.models import User
from django.utils.html import format_html
from artist.models import Artist

# Create your models here.
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3']
    if not ext.lower() in valid_extensions:
        raise ValidationError('unsuported file')


class Music(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام آهنگ')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name='کاربر')
    artist = models.ManyToManyField(Artist,verbose_name='خواننده')
    file = models.FileField(upload_to='music/tracks',validators=[validate_file_extension],verbose_name='فایل آهنگ')
    image = models.ImageField(upload_to='images/covers',verbose_name='کاور')
    upload_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ اضافه کردن')

    class Meta:
        verbose_name = 'موزیک'
        verbose_name_plural = 'موزیک ها'
        ordering = ('-upload_date',)

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;'src={}>".format(self.image.url))
    image_tag.short_description = 'کاور'

    def artist_to_str(self):
        return  ", ".join([artist.name for artist in self.artist.all()])
    artist_to_str.short_description = 'خواننده'

    def artist_list(self):
        return [artist for artist in self.artist.all()]
