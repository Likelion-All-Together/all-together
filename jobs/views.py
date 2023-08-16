from django.shortcuts import render,redirect
from .models import Class, Register
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
        name = request.POST.get('named') #이름
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
        nationality = request.POST.get('nationality') #국적
        language = request.POST.get('language') #언어
        account = request.POST.get('pay') #계좌
        
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
            language = language,
            nationality = nationality,
            account = account,
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
        time_list = (teacher.times).split("'")
        info_list = (teacher.info).split("'")
        stu_list = (teacher.student).split("'")
        group_list = (teacher.group).split("'")
        remove_list = {', ','[',']'}
        time_lists = [i for i in time_list if i not in remove_list]
        time = len(time_lists)
        info_lists = [i for i in info_list if i not in remove_list]
        stu_lists = [i for i in stu_list if i not in remove_list]
        group_lists = [i for i in group_list if i not in remove_list]
        print(time_lists)
        context = {
            'teacher':teacher,
            'time_list':time_lists, #시간대
            'info_list':info_lists, #경력
            'stu_list':stu_lists,   #학생
            'group_list':group_lists, #수업 종류(비지니스, 유학 등)
            'time':time
            
        }
        return render(request, 'jobs/jobs-detail.html',context)
    
    return render(request, 'jobs/jobs-detail.html')

def class_apply_view(request, id):
    teacher = get_object_or_404(Class, id=id)
    if request.method == 'GET':
        time_lists = (teacher.times).split("'")
        remove_list = {', ','[',']'}
        time_lists = [i for i in time_lists if i not in remove_list]
        
        date_list9 = ['월9','화9','수9','목9','금9','토9','일9']
        date_list10 = ['월10','화10','수10','목10','금10','토10','일10']
        date_list11 = ['월11','화11','수11','목11','금11','토11','일11']
        date_list12 = ['월12','화12','수12','목12','금12','토12','일12']
        date_list13 = ['월13','화13','수13','목13','금13','토13','일13']
        date_list14 = ['월14','화14','수14','목14','금14','토14','일14']
        date_list15 = ['월15','화15','수15','목15','금15','토15','일15']
        date_list16 = ['월16','화16','수16','목16','금16','토16','일16']
        
        context = {
            'time_lists' : time_lists,
            'teacher':teacher,
            'date_list9':date_list9,
            'date_list10':date_list10,
            'date_list11':date_list11,
            'date_list12':date_list12,
            'date_list13':date_list13,
            'date_list14':date_list14,
            'date_list15':date_list15,
            'date_list16':date_list16,
        }
        return render(request, 'jobs/jobs-apply.html', context)
    elif request.method == 'POST':
        class_name = Class.objects.get(id=id)
        writer = request.user
        student_name = request.POST.get('name')
        student_age = request.POST.get('age')
        student_phone = request.POST.get('phone')
        student_email = request.POST.get('email')
        pay = request.POST.get('pay')
        student_image = request.FILES.get('image')
        times = request.POST.get('selected_cells') #선택된 시간 (리스트형태)

        if times:
            times = json.loads(times)
        #테스트용 출력
        print(times)
        cost = teacher.cost * len(times)
        
        if student_image :     # 수업 비용 추가해야 함
            Register.objects.create(
                class_name=class_name,
                writer = writer,
                student_name=student_name,
                student_age = student_age,
                student_phone = student_phone,
                student_image = student_image,
                student_email = student_email,
                pay = pay,
                times = times,
                cost = cost,
            )
        else:
            Register.objects.create(
                class_name=class_name,
                writer = writer,
                student_name=student_name,
                student_age = student_age,
                student_phone = student_phone,
                pay = pay,
                times = times,
                cost = cost,
            )
        return redirect('jobs:jobs_main')
    return render(request, 'jobs/jobs-apply.html', context)


# 인증 뷰 (해야됨)
