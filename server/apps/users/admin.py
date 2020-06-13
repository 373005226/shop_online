from django.contrib import admin
from .models import *
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username','mobile','is_staff','name']


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(VerifyCode)
