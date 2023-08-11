from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('title','content','writer','category','view_count')
    
@admin.register(Comment)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('post','content')