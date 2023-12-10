from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                # messages.info(request, "username already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                # messages.info(request, "user added successfully")
                return render(request, "login.html")
        else:
            # messages.info(request, "password not matching")
            return redirect('register')

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def btn(request):
    return render(request, "form.html")


