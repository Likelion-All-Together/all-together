import json
from django.shortcuts import render
from .models import RegionAndMulticultural, Afterschool
from django.http import HttpResponse,JsonResponse 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404

# 정보 보여주기
def information_view(request):
    
    # tab, align_mode, page 가져오기
    tab = request.GET.get('tab', 'region') # 기본은 지역 탭
    align_mode = request.GET.get('align_mode', 'recently') # 기본 최신순 정렬
    page = request.GET.get('page')
    
    # [지역] 탭인 경우
    if tab == 'region':
        item_list = RegionAndMulticultural.objects.filter(category='지역') # 지역만 가져오기
        tab = 'region'

    # [다문화] 탭인 경우
    elif tab == 'multicultural':
        item_list = RegionAndMulticultural.objects.filter(category='다문화') # 다문화만 가져오기
        tab = 'multicultural'
    
    # [방과후] 탭인 경우
    elif tab == 'afterschool':
        item_list = Afterschool.objects.all()
        tab = 'afterschool'        
    
    # 정렬을 반영한 item_list
    item_list = reflect_alignment(item_list, align_mode)
    
    # 페이지 처리
    page_obj, paginator = make_page_obj(item_list, page, 9) # 일단 한 페이지에 2개씩 보여주기
    
    # 그룹으로 나누기
    first_obj = page_obj[:3]
    second_obj = page_obj[3:6]
    third_obj = page_obj[6:9]
    
    # 보낼 context
    context = {
            'item_list' : item_list,
            'tab' : tab,
            'align_mode' : align_mode,
            'page_obj' : page_obj,
            'first_obj' : first_obj,
            'second_obj' : second_obj,
            'third_obj' : third_obj,
            'paginator' : paginator,
    }
    
    return render(request, 'informations/informations.html', context)

# 정렬 처리
def reflect_alignment(item_list, align_mode):
    if align_mode == 'recently':
        return item_list.order_by('-created_at')
    elif align_mode == 'scrap':
        return item_list.order_by('-scrap')
    
# 만들 리스트, 현재 페이지, 한 페이지당 보여줄 포스트 개수
def make_page_obj(item_list, page, num_of_post,):
    paginator = Paginator(item_list, num_of_post)
    try:
        page_obj = paginator.page(page)
        return page_obj, paginator
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
        return page_obj, paginator
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
        return page_obj, paginator
    
def scrap_view_region(request, bid):
    user = request.user
    item =  get_object_or_404(RegionAndMulticultural, id=bid)
    if item.scrap.filter(id =user.id).exists():
        item.scrap.remove(user)
        return JsonResponse({'message':'delete','like_count':item.scrap.count()})
    else:
        item.scrap.add(user)
        return JsonResponse({'message':'ok','like_count':item.scrap.count()})
    
def scrap_view_after(request, bid):
    item = get_object_or_404(Afterschool, id=bid)
    user = request.user
    
    if item.scrap.filter(id =user.id).exists():
        item.scrap.remove(user)
        return JsonResponse({'message':'delete','like_count':item.scrap.count()})
    else:
        item.scrap.add(user)
        return JsonResponse({'message':'ok','like_count':item.scrap.count()})
    
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
