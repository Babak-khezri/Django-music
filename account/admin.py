from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
UserAdmin.fieldsets[2][1]['fields'] = (
    'image',
    'is_active',
    'is_staff',
    'is_superuser',
    'groups',
    'user_permissions',
)
# Add information's for show in first look
UserAdmin.list_display = list(UserAdmin.list_display)
UserAdmin.list_display.insert(1,'image_tag')
admin.site.register(User,UserAdmin)
