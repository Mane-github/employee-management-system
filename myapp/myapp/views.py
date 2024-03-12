from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    date=datetime.datetime.now()
    isActive=True
    name="Mahendra"
    
    data={
        'isActive':isActive,
        'date':date,
        'name':name
    }
    
    return render(request,"home.html",data)


def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})