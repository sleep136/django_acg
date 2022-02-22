#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-05 17:34
# @Author : wangjue
# @Site : 
# @File : views.py
# @Software: PyCharm


from rest_framework.views import APIView
from project.models import Project as ProjectModel, Issue, Discussion, ProjectEmployee, ProjectTag, ProjectMajor

from project.serializers import ProjectSerializer, IssueSerializer, DiscussionSerializer, ProjectEmployeeSerializer, \
    ProjectTagSerializer, ProjectMajorSerializer
from rest_framework import mixins, viewsets
from rest_framework import generics
from django.http import JsonResponse
from django.utils.decorators import method_decorator

# project_name = openapi.Parameter("project_name", openapi.IN_QUERY, description="项目名字",
#                                  type=openapi.TYPE_STRING)
#
# uid = openapi.Parameter("uid", openapi.IN_QUERY, description="用户id",
#                         type=openapi.TYPE_INTEGER)
# issue_id = openapi.Parameter("issue_id", openapi.IN_QUERY, description="问题id",
#                              type=openapi.TYPE_INTEGER)
# project_id = openapi.Parameter("project_id", openapi.IN_QUERY, description="项目id",
#                                type=openapi.TYPE_INTEGER)
# employee_id = openapi.Parameter("employee_id", openapi.IN_QUERY, description="职员id",
#                                 type=openapi.TYPE_INTEGER)
#
# add_employee_id = openapi.Parameter("add_employee_id", openapi.IN_QUERY, description="被增加的职员id",
#                                     type=openapi.TYPE_INTEGER)
#
# project_tag_id = openapi.Parameter("project_tag_id", openapi.IN_QUERY, description="项目标签id",
#                                    type=openapi.TYPE_INTEGER)
# org_id = openapi.Parameter("org_id", openapi.IN_QUERY, description="组织id",
#                            type=openapi.TYPE_INTEGER)
# project_major_id = openapi.Parameter("project_major_id", openapi.IN_QUERY, description="项目专业id",
#                                    type=openapi.TYPE_INTEGER)
#
# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_summary='返回用户所属的所有项目',
#     manual_parameters=[employee_id, org_id],
#     responses={
#         '200': ProjectSerializer(many=True),
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='retrieve', decorator=swagger_auto_schema(
#     operation_summary='返回单条项目信息',
#     manual_parameters=[employee_id, org_id, project_id],
#
#     responses={
#         '200': ProjectSerializer(many=False),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='create', decorator=swagger_auto_schema(
#     operation_summary='创建项目',
#     request_body=ProjectSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='update', decorator=swagger_auto_schema(
#     operation_summary='更新项目信息',
#     required=['employee_id', 'name', 'desc'],
#     request_body=ProjectSerializer,
#     properties={
#         'name': openapi.Parameter("name", openapi.IN_BODY, description="项目名",
#                                   type=openapi.TYPE_INTEGER),
#         'desc': openapi.Parameter("desc", openapi.IN_BODY, description="简介",
#                                   type=openapi.TYPE_INTEGER),
#         'employee_id': openapi.Parameter("parent_department_id", openapi.IN_BODY, description="被编辑的员工id",
#                                          type=openapi.TYPE_INTEGER),
#
#     },
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
class Project(viewsets.ModelViewSet):
    """
        项目信息

    retrieve:
        返回单条项目信息

    list:
        返回用户所属的所有项目

    create:
        创建项目


    partial_update:
        更新现有项目中的一个或多个字段（改：部分更改）

    update:
        更新项目信息

    """
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer


class ArchiveProject(APIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

    # @method_decorator(name='put', decorator=swagger_auto_schema(
    #     manual_parameters=[uid, project_id],
    #     operation_summary='冻结项目',
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    # ))
    def put(self):
        pass


# class AddProjectMember(generics.CreateAPIView):
#     """
#     增加项目成员
#     """
#     queryset = Discussion.objects.all()
#     serializer_class = DiscussionSerializer
#
#     @method_decorator(name='post', decorator=swagger_auto_schema(
#         request_body=ProjectEmployeeSerializer,
#         operation_summary='增加项目成员',
#         responses={
#             '200': openapi.TYPE_BOOLEAN,
#             '400': 'Bad Request'
#         },
#     ))
#     def post(self):
#         pass


# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_summary='返回项目下所属的所有成员',
#     manual_parameters=[project_id, uid],
#     responses={
#         '200': ProjectEmployeeSerializer(many=True),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='create', decorator=swagger_auto_schema(
#     operation_summary='项目增加新成员',
#     request_body=ProjectEmployeeSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='retrieve', decorator=swagger_auto_schema(
#     operation_summary='返回成员信息',
#     manual_parameters=[project_id, employee_id],
#     responses={
#         '200': ProjectEmployeeSerializer(many=False),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='update', decorator=swagger_auto_schema(
#     operation_summary='设置成员职责',
#     request_body=ProjectEmployeeSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='destroy', decorator=swagger_auto_schema(
#     manual_parameters=[uid],
#     operation_summary='移除成员',
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
class ProjectEmployee(viewsets.ModelViewSet):
    """
        项目成员

        retrieve:
            返回成员信息

        list:
            返回项目下所属的所有成员

        create:
            项目增加新的成员

        destroy:
            项目移除成员


        update:
            更新成员职责

        """
    queryset = ProjectEmployee.objects.all()
    serializer_class = ProjectEmployeeSerializer


# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_summary='返回项目下所属的所有问题',
#     manual_parameters=[employee_id, project_id],
#     responses={
#         '200': IssueSerializer(many=True),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='retrieve', decorator=swagger_auto_schema(
#     operation_summary='返回问题信息',
#     manual_parameters=[employee_id, project_id, issue_id],
#     responses={
#         '200': IssueSerializer(many=False),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='create', decorator=swagger_auto_schema(
#     operation_summary='创建问题',
#     properties={
#         'title': openapi.Parameter("title", openapi.IN_BODY, description="问题名",
#                                    type=openapi.TYPE_STRING, required=True),
#         'project_id': openapi.Parameter("project_id", openapi.IN_BODY, description="项目id",
#                                         type=openapi.TYPE_INTEGER, required=True),
#         'employee_id': openapi.Parameter("parent_department_id", openapi.IN_BODY, description="员工id",
#                                          type=openapi.TYPE_INTEGER, required=True),
#         'desc': openapi.Parameter("title", openapi.IN_BODY, description="描述",
#                                   type=openapi.TYPE_STRING, required=True),
#
#     },
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='update', decorator=swagger_auto_schema(
#     operation_summary='更新问题信息',
#     request_body=IssueSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='destroy', decorator=swagger_auto_schema(
#     manual_parameters=[uid, issue_id],
#     operation_summary='删除问题',
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
class Issue(viewsets.ModelViewSet):
    """
        问题信息

    retrieve:
        返回单条问题信息

    list:
        返回项目下所属的所有问题

    create:
        创建问题

    destroy:
        删除问题

    partial_update:
        更新现有问题中的一个或多个字段（改：部分更改）

    update:
        更新问题信息

    """
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer


class Discussion(generics.CreateAPIView, generics.ListAPIView):
    """
        问题信息

    list:
        返回项目下所属的所有问题

    create:
        创建问题


    """
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

    # @method_decorator(name='list', decorator=swagger_auto_schema(
    #     operation_summary='返回项目下问题下的所有回复',
    #     manual_parameters=[issue_id, employee_id],
    #     responses={
    #         '200': DiscussionSerializer(many=True),
    #         '400': 'Bad Request'
    #     },
    #
    # ))
    def get(self, request, args):
        """
        "返回项目下问题下的所有回复"
        :param request:
        :param args:
        :return:
        """
        data = []
        id = args.get("id")
        # i = table.find_one({"_id": int(id)})
        data.append({'user_name': "", "content": ""})
        return JsonResponse({"data": data})

    # @method_decorator(name='create', decorator=swagger_auto_schema(
    #     operation_summary='回复问题',
    #     request_body=DiscussionSerializer,
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    # ))
    def post(self, request, args):
        """
        "回复问题"
        :param request:
        :param args:
        :return:
        """
        data = []
        id = args.get("id")
        # i = table.find_one({"_id": int(id)})
        data.append({'user_name': "", "content": ""})
        return JsonResponse({"data": data})


# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_summary='返回项目下所属的所有标签',
#     manual_parameters=[employee_id, project_id],
#     responses={
#         '200': ProjectTagSerializer(many=True),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='retrieve', decorator=swagger_auto_schema(
#     operation_summary='返回标签信息',
#     manual_parameters=[employee_id, project_id, project_tag_id],
#     responses={
#         '200': ProjectTagSerializer(many=False),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='create', decorator=swagger_auto_schema(
#     operation_summary='创建标签',
#     request_body=ProjectTagSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='update', decorator=swagger_auto_schema(
#     operation_summary='编辑标签',
#     request_body=ProjectTagSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='destroy', decorator=swagger_auto_schema(
#     manual_parameters=[uid, project_tag_id],
#     operation_summary='删除标签',
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
class ProjectTag(viewsets.ModelViewSet):
    """
        项目标签

    retrieve:
        返回单条标签

    list:
        返回项目下所属的所有标签

    create:
        创建标签

    destroy:
        删除标签

    update:
        编辑标签

    """
    queryset = ProjectTag.objects.all()
    serializer_class = ProjectTagSerializer


# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_summary='返回项目下所属的专业',
#     manual_parameters=[uid, project_id],
#     responses={
#         '200': ProjectMajorSerializer(many=True),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='retrieve', decorator=swagger_auto_schema(
#     operation_summary='返回专业信息',
#     manual_parameters=[uid,project_major_id],
#     responses={
#         '200': ProjectMajorSerializer(many=False),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='create', decorator=swagger_auto_schema(
#     operation_summary='创建专业',
#     request_body=ProjectMajorSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='update', decorator=swagger_auto_schema(
#     operation_summary='编辑专业',
#     request_body=ProjectMajorSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='destroy', decorator=swagger_auto_schema(
#     manual_parameters=[uid,project_major_id],
#     operation_summary='删除专业',
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
class ProjectMajor(viewsets.ModelViewSet):
    """
        项目专业

    retrieve:
        返回专业信息

    list:
        返回项目下所属的所有专业

    create:
        创建专业

    destroy:
        删除专业



    update:
        编辑专业

    """
    queryset = ProjectMajor.objects.all()
    serializer_class = ProjectMajorSerializer
