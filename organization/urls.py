#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-05 15:46
# @Author : wangjue
# @Site : 
# @File : urls.py
# @Software: PyCharm


from django.conf.urls import url

from .views import Organization, TransferOrganization, Department, UploadMember, DepartmentManage, DepartmentChildren

urlpatterns = [
    url(r'^org/(?P<id>\d+)/?$', Organization.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    url(r'^org/?$', Organization.as_view({'get': 'list', 'post': 'create'})),
    url(r'^transfer_organization/?$', TransferOrganization.as_view(), name='transfer_organization'),
    url(r'^upload_member/?$', UploadMember.as_view(), name='upload_member'),
    url(r'^department/?$', Department.as_view({'get': 'list', 'post': 'create', 'post': 'create'})),
    # 基础方法：传参，获取单条数据，更新单条数据，删除单条数据。
    url(r'^department/(?P<id>\d+)/?$', Department.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # url(r'^department/?$', Department.as_view(), name='edit_organization'),
    url(r'^department_manage/?$', DepartmentManage.as_view(), name='department_manage'),
    url(r'^department_children/?$', DepartmentChildren.as_view(), name='department_children'),

]
