from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    # path('', views.home, name = 'home'),
    path('', views.home2, name = 'home2'),
    path('introduction/', views.introduction, name = 'introduction'),
    path('service/', views.service, name = 'service'),
]
