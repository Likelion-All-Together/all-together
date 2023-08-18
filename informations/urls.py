from django.urls import path
from .views import information_view, scrap, scrap_view_after,  scrap_view_region

app_name = 'informations'

urlpatterns = [
    path('scrap/after/<int:bid>', scrap_view_after , name = 'scrap'), # 스크랩 기능
    path('scrap/region/<int:bid>', scrap_view_region , name = 'scrap'), # 스크랩 기능
    path('', information_view, name = 'information'), # 탭에 따라 정보 보기
]