from django.urls import path
from authapp.views import *
app_name='authapp'
urlpatterns =[
    path('gologin/',go_login),

]