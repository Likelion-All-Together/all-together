from django.urls import path
from .views import information_view, scrap

app_name = 'informations'

urlpatterns = [
    path('scrap/', scrap, name = 'scrap'), # 스크랩 기능
    path('', information_view, name = 'information'), # 탭에 따라 정보 보기
]