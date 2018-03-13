# -*- coding: utf-8 -*-  
# author: xulang time: 18-3-9
from django import forms
from django.contrib.auth.models import User
from .models import Profile


#class LoginForm(forms.Form):
 #   username = forms.CharField()
  #  password = forms.CharField(widget=forms.PasswordInput)  # 使用Password控件来渲染HTML的input元素,包含type="password"属性


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    # 给这个表单加入了Meta类，它包含元数据，我们让该表单包含了model中的username, first_name,email字段
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    # 当我们在view中执行is_valid()方法时会自动执行这个方法
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match')
        return cd['password2']

# 让用户编辑他们自己的first_name, last_name, e-mail这些储存在User model中设置的字段
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

#  让用户能够编辑我们自己定制的储存在Profile中的额外字段date_of_birth和photo,而user字段在注册时已经被view获取，不用编辑。
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
