from django.urls import path
from .views import main_site, add_products

urlpatterns=[
    path('',main_site,name='main_site'),
    path('add_products/',add_products,name='add_products'),
]