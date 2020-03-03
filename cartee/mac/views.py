from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,User
from django.contrib.auth.decorators import login_required
from . import models
from .models import Product,Contact,Orders,OrderUpdate
from . forms import CreateUserForm
from math import ceil
import jwt,datetime
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
@login_required(login_url='login')
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
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'mac/tracker.html')

def search(request):
    return HttpResponse('you are at search')

def prodView(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,'mac/prodView.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'mac/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'mac/checkout.html')


def products(request):
        return HttpResponse(models.Product.all)

def register(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.SUCCESS(request,'Account successfully created:'+user)
            return redirect('mac/login')
    context={'form':form}

    return render(request,'registration/register.html',context)



def login(request):

    user=User()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')    
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            redirect('mac')
        else:
            messages.info(request,'Username or Password Incorrect')
        
    
    context={}
    return render(request,'registration/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('mac/login')







 