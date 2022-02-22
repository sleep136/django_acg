#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-08 16:35
# @Author : wangjue
# @Site : 
# @File : views.py
# @Software: PyCharm


from rest_framework.views import APIView
from notification.models import Notification

from notification.serializers import NotificationSerializer
from rest_framework import mixins, viewsets
from rest_framework import generics
from django.http import JsonResponse
from django.utils.decorators import method_decorator

# uid = openapi.Parameter("uid", openapi.IN_QUERY, description="用户id",
#                         type=openapi.TYPE_INTEGER)
# issue_id = openapi.Parameter("issue_id", openapi.IN_QUERY, description="问题id",
#                              type=openapi.TYPE_INTEGER)
# project_id = openapi.Parameter("project_id", openapi.IN_QUERY, description="项目id",
#                                type=openapi.TYPE_INTEGER)
# org_id = openapi.Parameter("org_id", openapi.IN_QUERY, description="项目id",
#                            type=openapi.TYPE_INTEGER)


# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_summary='返回项目下所属的所有通知',
#     manual_parameters=[uid, project_id, org_id],
#     responses={
#         '200': NotificationSerializer(many=True),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='retrieve', decorator=swagger_auto_schema(
#     operation_summary='返回标签信息',
#     manual_parameters=[uid],
#     responses={
#         '200': NotificationSerializer(many=False),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='update', decorator=swagger_auto_schema(
#     operation_summary='编辑标签',
#     request_body=NotificationSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
class Notification(viewsets.ModelViewSet):
    """
        通知

    retrieve:
        返回单条通知

    list:
        返回项目下所属的所有标签


    update:
        编辑通知状态

    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
