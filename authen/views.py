from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_(request):
    if request.method == 'POST':
        usernamelog=request.POST['username']
        passnamelog=request.POST['password']
        print(usernamelog,passnamelog)
        u=authenticate(username=usernamelog,password=passnamelog)
        print(u)
        if u is not None:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'wrong.html')
    return render(request,'login_.html')
def reg(request):
    if request.method =='POST':
        first=request.POST['firstname']
        second=request.POST['lastname']
        email1=request.POST['email']
        userdata=request.POST['username']
        password1=request.POST['password']
        print(userdata,password1)
        u=User.objects.create(first_name=first,last_name=second,email=email1,username=userdata,password=password1)
        u.set_password(password1)
        u.save()
        return redirect('login_')
    return render(request,'reg.html')
def logout_(request):
    logout(request)
    return redirect('login_')
@login_required(login_url='login_')
def profile(request):
    return render(request,'profile.html')