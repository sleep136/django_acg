#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-05 17:34
# @Author : wangjue
# @Site : 
# @File : urls.py
# @Software: PyCharm

from django.conf.urls import url

from project.views import Project, Issue, Discussion, ArchiveProject, ProjectEmployee, ProjectTag, ProjectMajor

urlpatterns = [
    url(r'^proj/(?P<id>\d+)/?$', Project.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    url(r'^proj/?$', Project.as_view({'get': 'list', 'post': 'create'})),
    url(r'^issue/(?P<id>\d+)/?$', Issue.as_view({'get': 'retrieve', 'put': 'update'})),
    url(r'^issue/?$', Issue.as_view({'get': 'list', 'post': 'create'})),
    url(r'^project_employee/(?P<id>\d+)/?$',
        ProjectEmployee.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    url(r'^project_employee/?$', ProjectEmployee.as_view({'get': 'list', 'post': 'create'})),
    url(r'^discussion/?$', Discussion.as_view(), name='discussion'),
    url(r'^archive_project/?$', ArchiveProject.as_view(), name='discussion'),
    url(r'^project_tag/?$', ProjectTag.as_view({'get': 'list', 'post': 'create'})),
    url(r'^project_tag/(?P<id>\d+)/?$',
        ProjectTag.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    url(r'^project_major/?$', ProjectMajor.as_view({'get': 'list', 'post': 'create'})),
    url(r'^project_major/(?P<id>\d+)/?$',
        ProjectMajor.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
