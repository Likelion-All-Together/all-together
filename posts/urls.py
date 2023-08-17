from django.urls import path
from .views import post_list_view, post_create_view, post_detail_view, like_view,delete_comment

app_name = 'posts'

urlpatterns = [
    path('', post_list_view, name = 'post-list-all'),
    path('create/', post_create_view, name = 'post-create'),
    path('<int:id>/', post_detail_view , name = 'post-detail'),
    path('like/<int:bid>',like_view), #좋아요
    path('<int:id>/<int:comment_id>', delete_comment , name = 'comment_delete'),
]