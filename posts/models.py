from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

CHOICES = (
    ('알바','알바'),
    ('과외','과외'),
    ('취준','취준'),
    ('경력단절','경력단절'),
    ('공지','공지'), # 운영자만 공지 글 작성 가능
    ('이벤트','이벤트'), #운영자만 공지 글 작성 가능
)

class Post(models.Model):
    title = models.TextField(verbose_name='제목',null=True, blank=True)
    category = models.CharField(max_length=20, choices=CHOICES, default='알바')
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(verbose_name = '이미지',null=True, blank=True)
    content = models.TextField(verbose_name = '내용')
    created_at = models.DateTimeField(verbose_name = '작성일',default=timezone.now)
    view_count = models.ImageField(verbose_name = '조회수',null=True, blank=True)
    file = models.FileField(verbose_name = '파일',null=True, blank=True)
    
    
class Comment(models.Model):
    content = models.TextField(verbose_name = '내용')
    post = models.ForeignKey(to='Post',on_delete=models.CASCADE, null=True)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True, blank = True)
    created_at = models.DateTimeField(verbose_name='작성일',default = timezone.now)
    
