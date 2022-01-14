from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Products
from .forms import AddProductForm

def main_site(request):
    products = Products.objects.all()
    return render(request,'main_site.html',{'products':products})

def add_products(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.user = request.user
            form2.save()
            return HttpResponseRedirect(reverse('main_site'))
    form = AddProductForm()
    return render(request,'add_products.html',{'form':form})