from django.shortcuts import render, redirect
from .models import RegionAndMulticultural, Afterschool
from django.views.decorators.http import require_POST

# 지역 정보 전체
def information_view(request):
    
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        region = RegionAndMulticultural.objects.filter(category='지역')
        multicultural = RegionAndMulticultural.objects.filter(category='다문화')
        afterschool = Afterschool.objects.all()
        
        context = {
            'region_list' : region,
            'multicultural_list' : multicultural,
            'afterschool_list' : afterschool,
        }
        
        return render(request, 'informations/informations-all.html', context)
    
# 지역 복지 정보
def region_view(request):
    if request.method == 'GET':
        
        region = RegionAndMulticultural.objects.filter(category='지역') # 지역만 가져오기
        
        align_mode = request.GET.get('align_mode', 'recently') # 기본 최신순 정렬
        
        if align_mode == 'recently': # 최신순 정렬
            region = region.order_by('-created_at')
        else: # 인기순(스크랩순) 정렬
            pass # **아직 스크랩 기능 안만들어서 일단 오래된순으로 보이게 해놓음**
            
        context = {
            'region_list' : region,
        }
        
        return render(request, 'informations/informations-region.html', context)

# 다문화 일자리
def multicultural_view(request):
    if request.method == 'GET':
        multicultural = RegionAndMulticultural.objects.filter(category='다문화')
        
        align_mode = request.GET.get('align_mode', 'recently') # 기본 최신순 정렬
        
        if align_mode == 'recently': # 최신순 정렬
            multicultural = multicultural.order_by('-created_at')
        else: # 인기순(스크랩순) 정렬
            pass # **아직 스크랩 기능 안만들어서 일단 오래된순으로 보이게 해놓음**
        
        context = {
            'multicultural_list' : multicultural,
        }
        
        return render(request, 'informations/informations-multicultural.html', context)

# 방과후
def afterschool_view(request):
    if request.method == 'GET':
        afterschool = Afterschool.objects.all()
        
        align_mode = request.GET.get('align_mode', 'recently') # 기본 최신순 정렬
        
        if align_mode == 'recently': # 최신순 정렬
            afterschool = afterschool.order_by('-created_at')
        else: # 인기순(스크랩순) 정렬
            pass # **아직 스크랩 기능 안만들어서 일단 오래된순으로 보이게 해놓음**
        
        context = {
            'afterschool_list' : afterschool,
        }
        
        return render(request, 'informations/informations-afterschool.html', context)