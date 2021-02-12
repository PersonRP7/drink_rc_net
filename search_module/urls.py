from . import views
from django.urls import path

app_name = 'search_module'
urlpatterns = [
    path('search_module_view/', views.search_module_view, name = 'search_module_view'),
    path('search_data/<str:query>/', views.search_data, name = 'search_data'),
    path('search/', views.search, name = 'search'),

]