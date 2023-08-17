from django.shortcuts import render
from posts.models import Post
from jobs.models import Class

import random
def home_view(request):
        teacher_list = Class.objects.all()
        random_teacher_list = random.sample(list(teacher_list), 4)
        filter_list = Post.objects.exclude(writer__username = '관리자').order_by('-created_at') # 일반 사용자들 글
        prandom_post_list = random.sample(list(filter_list), 3)
        context = {
            'teacher_list':random_teacher_list,
            'post_list':prandom_post_list,
        }
        return render(request, 'diamoyeo/home.html',context)