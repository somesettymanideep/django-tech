from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'uifiles/index.html')

def contactus(request):
    return render(request, 'uifiles/contact.html')