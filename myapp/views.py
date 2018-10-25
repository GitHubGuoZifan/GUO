from django.http import HttpResponseRedirect
from django.shortcuts import render
from myapp.models import User
from myapp.forms import UserForm
# Create your views here.
def register(request):
    if request.method=='POST':
       userForm= UserForm(request.POST)  #接收表单的POST提交数据
       if userForm.is_valid():
           name=userForm.cleaned_data['name']
           password=userForm.cleaned_data['password']
           repassword=userForm.cleaned_data['repassword']
           email=userForm.cleaned_data['email']
           QQ=userForm.cleaned_data['QQ']
           if password!=repassword:
               return HttpResponseRedirect("/myapp/reg/")
           else:
               User.objects.create(username=name,password=password,email=email,QQ=QQ)#注册，插入数据库
               return render(request,'success.html')

       else:
           return HttpResponseRedirect("/myapp/reg/")
    else:
        userForm=UserForm()
        return render(request,'register.html',{'regform':userForm})