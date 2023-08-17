from django.urls import path
from .views import identify_view, class_apply_view, jobs_creat_view, jobs_main_view, jobs_teacher_view, jobs_teacher_detail_view

app_name = 'jobs'

urlpatterns = [
    path('', jobs_main_view, name='jobs_main'),
    path('teacher/',jobs_teacher_view, name='teacher'),
    path('teacher/<int:id>/',jobs_teacher_detail_view, name='teacher_detail'),
    path('create/',jobs_creat_view, name='jobs_create'),
    path('create/certify/',identify_view, name='identify'), #인증
    path('apply/<int:id>/',class_apply_view, name = 'jobs_apply')    #수업 신청서
]
