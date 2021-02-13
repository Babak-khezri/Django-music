from django.db import models
from django.utils.html import format_html

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام خواننده')
    image = models.ImageField(upload_to='images/artists',verbose_name='تصویر')

    class Meta:
        verbose_name = "هنرمند"
        verbose_name_plural = "هنرمند ها"
        ordering = ['name']

    def __str__(self):
        return self.name

    def image_tag(self):  # show image in admin panel
        return format_html("<img width=100 height=75 style='border-radius: 5px;'src={}>".format(self.image.url))
    image_tag.short_description = 'تصویر خواننده'