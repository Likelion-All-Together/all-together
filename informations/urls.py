from django.urls import path
from .views import information_view, region_view, multicultural_view, afterschool_view

app_name = 'informations'

urlpatterns = [
    path('', information_view, name = 'information'),
    path('region/', region_view, name = 'region'), # 지역 복지 제도
    path('multicultural/', multicultural_view, name = 'multicultural'), # 다문화 일자리
    path('afterschool/', afterschool_view, name = 'afterschool'), # 방과후
]