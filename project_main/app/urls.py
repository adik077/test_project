from django.urls import path
from .views import main_site

urlpatterns=[
    path('',main_site,name='main_site'),
]