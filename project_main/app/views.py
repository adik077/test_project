from django.shortcuts import render
from .models import Products

def main_site(request):
    products = Products.objects.all()
    return render(request,'main_site.html',{'products':products})
