from django.contrib import admin
from .models import Class
# Register your models here.

@admin.register(Class)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('name','age','school','cost','id')