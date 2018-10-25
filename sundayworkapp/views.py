import os
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.cache import cache_page

from DjangoDay10.settings import BASE_DIR
from sundayworkapp.forms import LoginForm, RegisterForm
from sundayworkapp.models import MyUserModel, Student


#第一题
def go_welcome(request):
    return render(request,'welcome.html')

def go_login(request):
    return render(request,'login.html')

def go_success(request):
    login_name=request.GET.get('login_name',"")
    return render(request,'success.html',locals())

def reg(request):
    regname=request.POST['regname']
    regpwd=request.POST['regpwd']
    regaddress=request.POST['regaddress']
    regtel=request.POST['regtel']
    #添加到数据库中的auth_user表，create_user()对密码进行加密
    MyUserModel.objects.create_user(username=regname,password=regpwd,address=regaddress,phone=regtel)
    return HttpResponseRedirect('/sunday/login/')

def user_login(request):
    logname=request.POST['logname']
    logpwd=request.POST['logpwd']
    user=authenticate(username=logname,password=logpwd)
    print('logname',logname,'logpwd',logpwd,'user',user)
    if user:
        login(request,user)
        return HttpResponseRedirect('/sunday/gosuccess/?login_name=+logname')
    else:
        return render(request,'login.html',{"msg":"用户名或密码错误，请重新登陆！"})
#第二题
def go_upload(request):
    return render(request,'myupload.html')

def upload(request):
    upload_obj=request.FILES.get('myfile')
    dest_file=os.path.join(BASE_DIR,'sundayworkapp','static',upload_obj.name)
    with open(dest_file,'wb') as f:
        for chunk in upload_obj.chunks():
            f.write(chunk)
            imgpath=upload_obj.name
    return render(request,'img.html',{'imgpath':imgpath})
#第三题

# def gostu(request):
#     return render(request,'go_student.html')
@cache_page(60)
def showstu(request):
    students=Student.objects.all()
    # stu_list=[]
    # for stu in students:
    #     stu_dict={}
    #     stu_dict['id']=stu.id
    #     stu_dict['name']=stu.name
    #     stu_dict['age']=stu.age
    #     stu_dict['sex']=stu.sex
    #     stu_dict['price']=stu.price
    #     stu_list.append(stu_dict)
    # return JsonResponse({'students':stu_list})
    if request.method=='POST':
        return render(request,'showstudent.html',{'students':students})
    else:
        return render(request,'showstudent.html')

#用Form实现注销登陆，修改密码
def mylogin(request):
    error=[]
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            username=data['username']
            password=data['password']
            if login_validate(request,username,password):
                return render_to_response('welcome.html',{'user':username})
            else:
                error.append('Please input the correct password')
        else:
            error.append('Please input both username and password')
    else:
        form=LoginForm()
    return render_to_response('logiin.html',{'error':error,'form':form})

def login_validate(request,useranme,password):
    rtvalue=False
    user=authenticate(useranme=useranme,password=password)
    if user is not None:
        if user.is_active:#判断用户是否被激活
            auth_login(request,user)
            return True
        return rtvalue

def register(request):
    error=[]
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            username=data['username']
            email=data['email']
            password=data['password']
            password2=data['password2']
            if not User.objects.all().filter(username=username):
                if form.pwd_validate(password,password2):
                    user=User.objects.create_user(username,email,password)
                    user.save()
                    login_validate(request,username,password)
                    return render_to_response('welcome.html',{'user',username})
                else:
                    error.append('Please input the same password')
            else:
                error.append('The username has existed,please change your username')

    else:
        form=RegisterForm()
    return render_to_response('register.html',{'form':form,'error':error})
#注销
def mylogout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

def changepassword(request):
    error=[]
    if request.method=='POST':
        form=ChangepwdForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(username=username,password=data['old_pwd'])
            if user is not None:
                if data['new_pwd']==data['new_pwd2']:
                    newuser=User.objects.get(username_exact=username)
                    newuser.set_password(data['new_pwd'])
                    newuser.save()
                    return HttpResponseRedirect('/login/')
                else:
                    error.append('Please input the same password')
            else:
                error.append('Please correct the old password')
        else:
            error.append('Please input the required domain')
    else:
        form=ChangepwdForm()
    return render_to_response('changepassword.html',{'form':form,'error':error})