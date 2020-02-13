from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='mycarthome'),
    path('products',views.products,name='Products'),
    path('about',views.about,name='AboutUs'),
    path('contact',views.contact,name='ContactUs'),
    path('tracker',views.tracker,name='TrackingStatus'),
    path('search',views.search,name='Search'),
    path('product/<int:myid>',views.prodView,name='ProductView'),
    path('checkout',views.checkout,name='Checkout'),
    path('register',views.register,name='register'),

]
