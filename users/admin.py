from django.contrib import admin
from .models import Profile


# Register your models here.
# 将Profile注册到管理后台
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'mobile', 'created', 'updated']
