from django.shortcuts import render

from .models import RegionAndMulticultural, Afterschool

# 회원가입
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
        
        return render(request, 'informations/home.html', context)