from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    return render(request,'mac/index.html')

def about(request):
    return HttpResponse('you are at about')

def contact(request):
    return HttpResponse('you are at contactus')

def tracker(request):
    return HttpResponse('you are at tracker')

def search(request):
    return HttpResponse('you are at search')

def prodView(request):
    return HttpResponse('you are at productview')

def checkout(request):
    return HttpResponse('you are at checkout')

def products(request):
        return HttpResponse(models.Product.all)

