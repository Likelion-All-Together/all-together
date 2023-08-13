import json
from django.shortcuts import render
from .models import RegionAndMulticultural, Afterschool
from django.http import HttpResponse
import json

# 정보 보여주기
def information_view(request):
    
    # tab과 align_mode 가져오기
    tab = request.GET.get('tab', 'region') # 기본은 지역 탭
    align_mode = request.GET.get('align_mode', 'recently') # 기본 최신순 정렬
    
    # [지역] 탭인 경우
    if tab == 'region':
        item_list = RegionAndMulticultural.objects.filter(category='지역') # 지역만 가져오기
        tab = 'region'
        
        # 정렬 기준 처리
        if align_mode == 'recently':
            item_list = item_list.order_by('-created_at')
        elif align_mode == 'scrap':
            item_list = item_list.order_by('-scrap')
    
    
    # [다문화] 탭인 경우
    elif tab == 'multicultural':
        item_list = RegionAndMulticultural.objects.filter(category='다문화') # 다문화만 가져오기
        tab = 'multicultural'
    
        # 정렬 기준 처리
        if align_mode == 'recently':
            item_list = item_list.order_by('-created_at')
        elif align_mode == 'scrap':
            item_list = item_list.order_by('-scrap')
    
    # [방과후] 탭인 경우
    elif tab == 'afterschool':
        item_list = Afterschool.objects.all()
        tab = 'afterschool'
        
            # 정렬 기준 처리
        if align_mode == 'recently':
            item_list = item_list.order_by('-created_at')
        elif align_mode == 'scrap':
            item_list = item_list.order_by('-scrap')
    
    # 보낼 context
    context = {
            'item_list' : item_list,
            'tab' : tab,
    }
    
    return render(request, 'informations/informations.html', context)

# 스크랩 기능
def scrap(request): 
    
    item_name = request.GET['item_name']
    item_id = request.GET['item_id']
    
    if(item_name == 'region' or item_name == 'multicultural'): # [지역] 또는 [다문화] 인 경우
        item = RegionAndMulticultural.objects.get(id = item_id)
    
    elif(item_name == 'afterschool'): # [방과후] 인 경우
        item = Afterschool.objects.get(id = item_id)
        
    user = request.user #request.user : 현재 로그인한 유저
    if item.scrap.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
        item.scrap.remove(user) #like field에 현재 유저 추가
        message = "좋아요 취소" #화면에 띄울 메세지
    else: #좋아요를 누르지 않은 유저일 때
        item.scrap.add(user) #like field에 현재 유저 삭제
        message = "좋아요" #화면에 띄울 메세지 
    
    context = {'scrap_count' : item.scrap.count(),"message":message}
    return HttpResponse(json.dumps(context), content_type='application/json')  