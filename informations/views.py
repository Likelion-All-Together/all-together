import json
from django.shortcuts import render, redirect
from .models import RegionAndMulticultural, Afterschool
from django.http import HttpResponse,JsonResponse
import json

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
            'item_list' : region,
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
            'item_list' : multicultural,
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
            'item_list' : afterschool,
        }
        
        return render(request, 'informations/informations-afterschool.html', context)
    
# 스크랩 기능
def scrap(request): 
    
    # if request.is_ajax(): #ajax 방식일 때 아래 코드 실행
    
    item_name = request.GET['item_name']
    
    # [지역] 또는 [다문화] 인 경우
    if(item_name == '지역' or item_name == '다문화'):
        item_id = request.GET['item_id']
        item = RegionAndMulticultural.objects.get(id = item_id) 
    # [방과후] 인 경우
    else:
        item_id = request.GET['item_id']
        item = Afterschool.objects.get(id = item_id)
            
    user = request.user #request.user : 현재 로그인한 유저
    if item.scrap.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
        item.scrap.remove(user) #like field에 현재 유저 추가
        message = "좋아요 취소" #화면에 띄울 메세지
    else: #좋아요를 누르지 않은 유저일 때
        item.scrap.add(user) #like field에 현재 유저 삭제
        message = "좋아요" #화면에 띄울 메세지
    # post.like.count() : 게시물이 받은 좋아요 수  
    context = {'scrap_count' : item.scrap.count(),"message":message}
    return HttpResponse(json.dumps(context), content_type='application/json')  
    