from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

SUPPORT_CYCLE_CHOICES = (
    ('일', '일'),
    ('월', '월'),
    ('년', '년'),
)

TAG_CHOICES = (
    ('태그1', '태그1'),
    ('태그2', '태그2'),
)

INFORMATION_CATEGORY = (
    ('지역', '지역'),
    ('다문화', '다문화'),
)

DAY = (
    ('월요일', '월요일'),
    ('화요일', '화요일'),
    ('수요일', '수요일'),
    ('목요일', '목요일'),
    ('금요일', '금요일'),
    ('토요일', '토요일'),
    ('일요일', '일요일'),
)

STATUS = (
    ('접수 전', '접수 전'),
    ('접수중', '접수중'),
    ('접수마감', '접수마감'),
)
class RegionAndMulticultural(models.Model):
    title = models.CharField(verbose_name = '제목', max_length = 20, null = False, blank = False)
    content = models.CharField(verbose_name = '내용', max_length = 100, null = False, blank = False)
    phone = models.CharField(verbose_name = '전화번호', max_length = 20, null = False, blank = False)
    support_cycle = models.CharField(verbose_name = '지원 주기', max_length = 50)
    type = models.CharField(verbose_name = '제공 유형', max_length = 20, null = False, blank = False)
    department = models.CharField(verbose_name = '담당 부서', max_length = 20, null = False, blank = False)
    tag = models.CharField(verbose_name = '태그', max_length = 20, choices = TAG_CHOICES , default = None) 
    category = models.CharField(verbose_name = '지역/다문화 정보', max_length = 20, choices = INFORMATION_CATEGORY ,default = '일')
    user = models.ForeignKey(User,on_delete = models.CASCADE, null = True, blank = True)
    scrap = models.ManyToManyField(User, related_name = 'scrap1', null = True, blank = True)
    created_at = models.DateTimeField(default = timezone.now)
    url = models.CharField(verbose_name = 'URL', max_length = 250, default = None, null = True) 

class Afterschool(models.Model):
    region = models.CharField(verbose_name = '동 명', max_length = 20, null = False, blank = False)
    title = models.CharField(verbose_name = '프로그램명', max_length = 20, null = False, blank = False)
    receipt_start = models.DateField(verbose_name = '접수 시작 날짜')
    receipt_end = models.DateField(verbose_name = '접수 마감 날짜')
    training_start = models.DateField(verbose_name = '교육 시작 날짜')
    training_end = models.DateField(verbose_name = '교육 마감 날짜')
    day = models.CharField(verbose_name = '요일', max_length = 20, choices = DAY)
    tuition = models.IntegerField(verbose_name = '수강료')
    number_of_member = models.IntegerField(verbose_name = '정원')
    status = models.CharField(verbose_name = '상태', max_length = 20, choices = STATUS, default = '접수중')
    user = models.ForeignKey(User,on_delete = models.CASCADE, null = True, blank = True) # 추가
    scrap = models.ManyToManyField(User, related_name = 'scrap2', null = True, blank = True) # 추가
    created_at = models.DateTimeField(default=timezone.now)
    url = models.CharField(verbose_name = 'URL', max_length = 250, default = None, null = True)