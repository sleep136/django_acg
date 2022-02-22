#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-03 16:55
# @Author : wangjue
# @Site : 
# @File : urls.py
# @Software: PyCharm

from django.conf.urls import url
from django.urls import path, include
from . import views
# from .views import GetOneNews
from .views import RegisterEmailAccount, AccountInfo, ResetPassword, ResetPasswordByEmail, ResetPasswordByMobile, \
    AccountInfoViewsSet, \
    CheckMobole

# ,ArticleViewSet, PostViewSet
# from rest_framework.routers import SimpleRouter
# router = SimpleRouter()
# router.register('', AccountInfoViewsSet, basename='codes')

urlpatterns = [
    path('account_index', views.account_index, name='account_index'),
    # url(r'^getOneNews/?$', GetOneNews.as_view(), name='get_one_news'),

    url(r'^account_info/(?P<id>\d+)/?$', AccountInfo.as_view(), name='register_email_account'),
    url(r'^reset_password/?$', ResetPassword.as_view(), name='reset_password'),

    # url(r'^check_email/?$', CheckEmail.as_view(), name='reset_password_by_email'),


    # url(r'^test1/?$', ArticleViewSet.as_view(), name='reset_password_by_mobile123'),
    # url(r'^test132/?', ArticleViewSet.as_view(), name='reset_password_by_email212'),
    # url(r'^test/?$', AccountInfo.phone(), name='reset_password_by_email2123'),
    #  path('', include(router.urls)),

]
