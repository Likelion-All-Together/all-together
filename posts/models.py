from django.db import models

class Post(models.Model):
    image = models.ImageField(verbose_name = '이미지')
    content = models.TextField(verbose_name = '내용')
    created_at = models.DateTimeField(verbose_name = '작성일')
    view_count = models.ImageField(verbose_name = '조회수')
    
class Comment(models.Model):
    content = models.TextField(verbose_name = '내용')