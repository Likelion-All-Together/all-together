from django.urls import path
from .views import information_view

app_name = 'informations'

urlpatterns = [
    path('/', information_view, name = 'information'),   
]