from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Product,Contact
from math import ceil

# Create your views here.

def index(request):
    products=Product.objects.all()
    allProds=[]
    catProds=Product.objects.values('category')
    cats={item['category'] for item in catProds}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    param={'allProds':allProds}
    return render(request,'mac/index.html',param)

def about(request):
    return render(request,'mac/about.html')

def contact(request): 
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    return render(request,'mac/contact.html')

def tracker(request):
    return render(request,'mac/tracker.html')

def search(request):
    return HttpResponse('you are at search')

def prodView(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,'mac/prodView.html',{'product':product[0]})

def checkout(request):
    return HttpResponse('you are at checkout')

def products(request):
        return HttpResponse(models.Product.all)

