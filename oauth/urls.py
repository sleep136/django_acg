#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-19 10:03
# @Author : wangjue
# @Site : 
# @File : urls.py
# @Software: PyCharm

from django.conf.urls import url

from oauth.views import GetVerificationCode, RegisterEmailAccountView, ResetPasswordByEmail, ResetPasswordByMobile, \
    CheckMobole

app_name = "oauth"
urlpatterns = [
    url(r'^get_verification_code/?$', GetVerificationCode.as_view(), name='get_verification_code'),
    url(r'^reset_password_by_email/?$', ResetPasswordByEmail.as_view(), name='reset_password_by_mobile'),
    url(r'^reset_password_by_mobile/?$', ResetPasswordByMobile.as_view(), name='reset_password_by_email'),
    url(r'^check_mobile/?$', CheckMobole.as_view(), name='reset_password_by_email'),
    url(r'^register_email_account$', RegisterEmailAccountView.as_view(), name='register_email_account'),

    # path(
    #     r'oauth/authorize',
    #     views.authorize)
    # path(
    #     r'oauth/requireemail/<int:oauthid>.html',
    #     views.RequireEmailView.as_view(),
    #     name='require_email'),
    # path(
    #     r'oauth/emailconfirm/<int:id>/<sign>.html',
    #     views.emailconfirm,
    #     name='email_confirm'),
    # path(
    #     r'oauth/bindsuccess/<int:oauthid>.html',
    #     views.bindsuccess,
    #     name='bindsuccess'),
    # path(
    #     r'oauth/oauthlogin',
    #     views.oauthlogin,
    #     name='oauthlogin')
]
