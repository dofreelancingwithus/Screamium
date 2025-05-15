from django.shortcuts import render,HttpResponse
from datetime import datetime
from screamium.models import Order
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request,'services.html')

def servicescopy(request):
    return render(request,'servicescopy.html')

def otherservices(request):
    return render(request,'otherservices.html')

def order(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email') 
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        order=Order(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        order.save()
        messages.success(request, "The Order has been Noted !!")
    return render(request, 'order.html')

