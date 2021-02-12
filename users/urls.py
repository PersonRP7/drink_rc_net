from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "users/logout.html"), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('profile/<str:username>/', views.profile, name = 'profile'),
    path('userprofile_redirect/', views.userprofile_redirect, name = 'userprofile_redirect'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate_account, name='activate'),
]
