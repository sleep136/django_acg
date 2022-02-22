#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-08 16:35
# @Author : wangjue
# @Site : 
# @File : urls.py
# @Software: PyCharm


from django.conf.urls import url

from notification.views import Notification

urlpatterns = [

    url(r'^noti/?$', Notification.as_view({'get': 'list'})),
    url(r'^noti/(?P<id>\d+)/?$', Notification.as_view({'get': 'retrieve', 'put': 'update'})),

]
