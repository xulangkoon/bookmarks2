from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
#from . forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages


#def user_login(request):  # 当该方法被GET请求调用,就会返回一个新的登录表单
    #if request.method == "POST":
        #form = LoginForm(request.POST)  # 如果被POST调用,就实例化一个表单
        #if form.is_valid():
            #cd = form.cleaned_data
            #user = authenticate(username=cd['username'], password=cd['password'])  # 如果数据有效，使用authenticate()通过数据库对该用户进行认证，成功就返回用户对象
            #if user is not None:
           #     if user.is_active:  # 这是在User模型(model)里的属性
          #          login(request, user)
         #           return HttpResponse('登录成功')
        #        else:
       #             return HttpResponse('未注册帐号')
      #      else:
     #           return HttpResponse('登录无效')
    #else:
     #   form = LoginForm()
    #return render(request,'account/login.html', {'form': form})


@login_required  # 如果已经登录，它会定向到你要到的位置，如果检测到未登录，会记录你要到的位置在next中当定向到登录页面。
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@login_required  # 这是一个测试，如果你想访问account/test这个url，login_required会检测你是否登录，如果没有，会有next这个变量来记录你要访问的account/test地址，但会跳转到登录页面，等登录成功后才跳到你要取得test。
def test(request):
    return render(request, 'account/test.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # 创建了一个用户实例但先不保存它
            new_user = user_form.save(commit=False)
            # 为了保护用户的隐私，使用set_password()方法来用户的原密码进行加密再保存
            new_user.set_password(user_form.cleaned_data['password'])
            # 保存用户实例
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # 使用messages框架
            messages.success(request, '信息完善成功！')
        else:
            messages.error(request, '信息完善失败')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})







