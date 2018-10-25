from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
    QQ=models.CharField(max_length=20,null=True)
    #blank空的，等于True，可以为空  ,null空的，等于True,可以为空