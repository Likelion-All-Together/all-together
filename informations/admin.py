from django.contrib import admin
from .models import RegionAndMulticultural, Afterschool

@admin.register(RegionAndMulticultural)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'phone')
    pass

@admin.register(Afterschool)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('region', 'title', 'status')
    pass