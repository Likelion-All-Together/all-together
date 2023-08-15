from django.contrib import admin
from .models import Class, Register
# Register your models here.

@admin.register(Class)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('name','age','school','cost','id')

@admin.register(Register)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('class_name','student_name','writer')