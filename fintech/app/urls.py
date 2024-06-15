from django.urls import path
from .views import index,contactus,reachus



urlpatterns = [
    path('',index,name='index'),
    path('contactus/',contactus,name='contactus'),
    path('reachus/',reachus,name='reachus'),
]