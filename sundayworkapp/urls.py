from django.urls import path
from sundayworkapp.views import *

app_name='sundayworkapp'

urlpatterns =[
    #第一题
    path('go_welcome/',go_welcome,name='welcome'),
    path('login/',go_login,name='login'),
    path('gosuccess/',go_success,name='success'),
    path('user_login/',user_login,name='userlogin'),
    path('reg/',reg,name='reg'),
    #第二题
        path('go_upload/',go_upload),
    path('upload/',upload,name='upload'),
    #第三题
    # path('go_stu/',gostu),
    path('showstu/',showstu,name='show'),

]