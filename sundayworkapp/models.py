from django.contrib.auth.models import AbstractUser
from django.db import models

#第一题
class MyUserModel(AbstractUser):
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20,null=True)


#第三题
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    sex=models.CharField(max_length=20)
    price=models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="学生信息"
