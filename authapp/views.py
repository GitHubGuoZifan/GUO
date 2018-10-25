from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
@login_required
def go_vip(request):
    return render(request,'user_vip.html')


def go_register(request):
    return render(request,'user_register.html')

def go_login(request):
    return render(request,'uesr_login.html')

def go_success(request):
    return render(request,'user_success.html')

def reg(request):
    regname=request.POST['regname']
    regpwd=request.POST['regpassword']
    User.objects.create(username=regname,password=regpwd)
    return HttpResponseRedirect('/authapp/gologin/')

def login(request):
    logname = request.POST['logname']
    logpwd = request.POST['logpwd']
    authenticate(username=logname,password=logpwd)