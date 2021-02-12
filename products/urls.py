from . import views
from django.urls import path

app_name = 'products'
urlpatterns = [
    path('all/', views.products_all, name = 'products_all'),
    path('product_specific/<slug:slug>/', views.product_specific, name = 'product_specific'),
    path('coffee_sort/<str:title>/', views.coffee_sort, name = 'coffee_sort'),
    path('coffee_overview/', views.coffee_overview, name = 'coffee_overview'),
    path('machine_overview/', views.machine_overview, name = 'machine_overview'),
    path('vending_machine/', views.vending_machine, name = 'vending_machine'),
    path('capsule_machine/', views.capsule_machine, name = 'capsule_machine'),
    path('snack_machine/', views.snack_machine, name = 'snack_machine'),
    path('water_dispenser/', views.water_dispenser, name = 'water_dispenser'),
    path('search_data/<str:query>/', views.search_data, name = 'search_data'),
    path('search/', views.search, name = 'search'),
   
]
