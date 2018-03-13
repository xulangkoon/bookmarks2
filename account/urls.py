# -*- coding: utf-8 -*-  
# author: xulang time: 18-3-9

from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),  # 都是使用django内置的方法完成登录，退出，修改...相应的form也是已经内置好了的
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^test/$', views.test, name='test'),
    # 修改密码的url
    url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    # 修改完成后的URL
    url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    # 重置密码的URL
    url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),

    url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),

    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),

    url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),


    url(r'^register/$', views.register, name='register'),
    # 让用户有自己的页面来编辑他们自己的profile
    url(r'^edit/$', views.edit, name='edit')
]