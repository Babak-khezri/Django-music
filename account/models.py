from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls.conf import path
from django.utils.html import format_html


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='images/profile', blank=True,default='images/profile/defalt.jpg', verbose_name='تصویر')

    def image_tag(self):  # show image in admin panel
        return format_html("<img width=75 height=75 style='border-radius: 50px;'src={}>".format(self.image.url))
    image_tag.short_description = 'تصویر پروفایل'
