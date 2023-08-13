from django.shortcuts import render,redirect
from .models import Class
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
import json

# Create your views here.

def jobs_main_view(request):
    if request.method == 'GET':
        return render(request, 'jobs/jobs-all.html')
    return render(request, 'jobs/jobs-all.html')

def jobs_creat_view(request):
    if request.method == 'GET':
        return render(request, 'jobs/jobs-create.html')   
    elif request.method == 'POST':
        writer = request.user
        name = request.POST.get('name') #이름
        image = request.FILES.get('image') #프로필 사진
        gender = request.POST.get('gender') #성별
        age = request.POST.get('age') #나이
        school = request.POST.get('education')  #학력
        cost = int(request.POST.get('cost')) #비용
        info = request.POST.getlist('teacher') #강사정보
        student = request.POST.getlist('student')#수업대상
        feature = request.POST.get('feature')#특이사항
        group = request.POST.getlist('class') #수업 분류
        selected_cells = request.POST.get('selected_cells') #선택된 시간 (리스트형태)
        if selected_cells:
            selected_cells = json.loads(selected_cells)
        #테스트용 출력
        print(student)
        print(info)
        print(group)
        print(selected_cells)
        
        class_name = Class.objects.create(
            writer = writer,
            name=name,
            image = image,
            gender = gender,
            age=age,
            school = school,
            cost = cost,
            info = info,
            student = student,
            feature = feature,
            group = group,
            times = selected_cells,
        )
        return redirect('jobs:jobs_main')
    return render(request, 'jobs/jpbs-create.html')
        

def jobs_teacher_view(request): # 선생님 전체 페이지
    if request.method == 'GET':
        teacher_list = Class.objects.all()
        context = {
            'teacher_list':teacher_list,
        }
        return render(request, 'jobs/jobs-teacher.html',context)
    return render(request, 'jobs/jobs-teacher.html',context)

def jobs_teacher_detail_view(request,id): #선생님 상세 페이지
    teacher = get_object_or_404(Class, id=id)
    if request.method == 'GET':
        context = {
            'teacher':teacher,
        }
        return render(request, 'jobs/jobs-detail.html',context)
    
    return render(request, 'jobs/jobs-detail.html')

def class_apply_view(request, id):
    teacher = get_object_or_404(Class, id=id)
    if request.method == 'GET':
        context = {
            'teacher':teacher
        }
        return render(request, 'jobs/jobs-apply.html', context)
    return render(request, 'jobs/jobs-apply.html', context)


# 인증 뷰 (해야됨)
