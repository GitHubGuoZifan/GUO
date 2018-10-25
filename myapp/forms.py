from django import forms

class UserForm(forms.Form):
    name=forms.CharField(label="用户名",max_length=10)
    password=forms.CharField(label="密码",max_length=10,widget=forms.PasswordInput)
    repassword=forms.CharField(label="重复密码",max_length=10,widget=forms.PasswordInput)
    email=forms.EmailField(label="邮箱")
    QQ=forms.CharField(label='QQ号',required=False)