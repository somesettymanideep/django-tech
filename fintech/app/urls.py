from django.urls import path
from .views import index,contactus



urlpatterns = [
    path('',index,name='index'),
    path('contactus/',contactus,name='contactus'),
]