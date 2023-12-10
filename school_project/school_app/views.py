from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Department
# Create your views here.

def Alldep(request):
    dep = Department.objects.all()

    return render(request,'index.html', {'dept':dep})



