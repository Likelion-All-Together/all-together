from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from diamoyeo.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace = 'accounts')),
    path('informations/', include('informations.urls', namespace = 'informations')),
    path('diamoyeo/', include('diamoyeo.urls', namespace = 'diamoyeo')),
    path('posts/', include('posts.urls', namespace = 'posts')),
    path('jobs/',include('jobs.urls',namespace = 'jobs')),
    path('', home_view, name='home'),
]

# 사용자가 추가한 프로필 이미지 저장을 위한 urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)