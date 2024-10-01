from django.shortcuts import render
from .models import Products
# Create your views here.

def index(request):
    allproducts = Products.objects.filter(status=0)
    return render(request,'index.html',{"allproducts":allproducts})