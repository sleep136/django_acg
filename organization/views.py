#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-05 15:46
# @Author : wangjue
# @Site : 
# @File : views.py.py
# @Software: PyCharm
from django.http import JsonResponse

from rest_framework.decorators import action
from rest_framework.views import APIView
from haid_project.utils import get_request_args
from organization.serializers import OrganizationSerializer, DepartmentSerializer
from organization.models import Department, Organization
from rest_framework import mixins, viewsets
from django.utils.decorators import method_decorator

# uid = openapi.Parameter("uid", openapi.IN_QUERY, description="用户id",
#                         type=openapi.TYPE_INTEGER)
# org_id = openapi.Parameter("org_id", openapi.IN_QUERY, description="组织id",
#                            type=openapi.TYPE_INTEGER)
#
# org_name = openapi.Parameter("org_name", openapi.IN_QUERY, description="组织名字",
#                              type=openapi.TYPE_STRING)
#
# org_short_name = openapi.Parameter("org_short_name", openapi.IN_QUERY, description="组织简称",
#                                    type=openapi.TYPE_STRING)
#
# logo_pic = openapi.Parameter("logo_pic", openapi.IN_QUERY, description="logo地址",
#                              type=openapi.TYPE_STRING)
#
# receive_uid = openapi.Parameter("receive_uid", openapi.IN_QUERY, description="转入的用户ID",
#                                 type=openapi.TYPE_INTEGER)
# request_uid = openapi.Parameter("request_uid", openapi.IN_QUERY, description="转出的用户id",
#                                 type=openapi.TYPE_INTEGER)
#
# cover = openapi.Parameter("name", openapi.IN_QUERY, description="封面",
#                           type=openapi.TYPE_STRING)
#
# department_id = openapi.Parameter("department_id", openapi.IN_QUERY, description="部门id",
#                                   type=openapi.TYPE_INTEGER)
#
# department_name = openapi.Parameter("department_name", openapi.IN_QUERY, description="部门名字",
#                                     type=openapi.TYPE_STRING)
#
# employee_id = openapi.Parameter("employee_id", openapi.IN_QUERY, description="成员id",
#                                 type=openapi.TYPE_INTEGER)
#
# employee_id_list = openapi.Parameter("employee_id_list", openapi.IN_QUERY, description="成员id列表拼接的字符串",
#                                      type=openapi.TYPE_STRING)
#
# employee_title = openapi.Parameter("employee_title", openapi.IN_QUERY, description="成员职称",
#                                    type=openapi.TYPE_STRING)
# employee_excel = openapi.Parameter("employee_excel", openapi.IN_BODY, description="公司成员excel",
#                                    type=openapi.TYPE_FILE)
# organization_response = openapi.Response('response description', OrganizationSerializer)
#department_response = openapi.Response('response description', DepartmentSerializer(many=True))


# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_summary='返回用户所属的所有组织',
#     manual_parameters=[uid],
#     responses={
#         '200': OrganizationSerializer(many=True),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='retrieve', decorator=swagger_auto_schema(
#     operation_summary='返回单条组织信息',
#     manual_parameters=[uid],
#     responses={
#         '200': OrganizationSerializer(many=False),
#         '400': 'Bad Request'
#     },
#
# ))
# @method_decorator(name='create', decorator=swagger_auto_schema(
#     operation_summary='创建组织',
#     request_body=OrganizationSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='update', decorator=swagger_auto_schema(
#     operation_summary='更新组织信息',
#     request_body=OrganizationSerializer,
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='destroy', decorator=swagger_auto_schema(
#     manual_parameters=[uid, org_id],
#     operation_summary='注销组织',
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
class Organization(viewsets.ModelViewSet):
    """
        组织信息

    retrieve:
        返回单条组织信息

    list:
        返回用户所属的所有组织

    create:
        创建组织

    destroy:
        注销组织

    partial_update:
        更新现有组织中的一个或多个字段（改：部分更改）

    update:
        更新组织信息

    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class TransferOrganization(APIView):
    # @swagger_auto_schema(
    #     operation_description="转让组织",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['receive_uid', "request_uid", 'org_id'],
    #         properties={
    #             'org_id': openapi.Schema(type=openapi.TYPE_INTEGER),
    #             'request_uid': openapi.Schema(type=openapi.TYPE_INTEGER),
    #             'receive_uid': openapi.Schema(type=openapi.TYPE_STRING),
    #
    #         },
    #         # manual_parameters=[uid, name],
    #     ),
    #     security=[],
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     operation_summary='转让组织'
    # )
    @get_request_args
    def post(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})
        pass


class CancelOrganization(APIView):
    # @swagger_auto_schema(
    #     operation_description="注销组织",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['receive_uid', 'uid'],
    #         properties={
    #             'org_id': openapi.Schema(type=openapi.TYPE_INTEGER),
    #             'uid': openapi.Schema(type=openapi.TYPE_INTEGER),
    #
    #         },
    #         # manual_parameters=[uid, name],
    #     ),
    #     security=[],
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     operation_summary='注销组织'
    # )
    @get_request_args
    def post(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})
        pass


# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_summary='获取部门列表',
#     manual_parameters=[employee_id, org_id],
#     responses={
#         '200': DepartmentSerializer(many=True),
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='retrieve', decorator=swagger_auto_schema(
#     operation_summary='获取部门信息',
#     manual_parameters=[employee_id, org_id, department_id],
#     responses={
#         '200': department_response,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='create', decorator=swagger_auto_schema(
#     operation_summary='新建部门信息',
#     request_body=openapi.Schema(
#         type=openapi.TYPE_OBJECT,
#         required=['parent_department_id', 'org_id', 'uid'],
#         properties={
#             'org_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             'uid': openapi.Schema(type=openapi.TYPE_INTEGER),
#             'parent_department_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             'cover': openapi.Schema(type=openapi.TYPE_STRING),
#             'desc': openapi.Schema(type=openapi.TYPE_STRING),
#         },
#         # manual_parameters=[uid, name],
#     ),
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='update', decorator=swagger_auto_schema(
#     operation_summary='编辑部门列表',
#     request_body=openapi.Schema(
#         type=openapi.TYPE_OBJECT,
#         required=['parent_department_id', 'org_id', 'uid'],
#         properties={
#             'org_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             'uid': openapi.Schema(type=openapi.TYPE_INTEGER),
#             'parent_department_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#             'cover': openapi.Schema(type=openapi.TYPE_STRING),
#             'desc': openapi.Schema(type=openapi.TYPE_STRING),
#         },
#         # manual_parameters=[uid, name],
#     ),
#     responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
# ))
# @method_decorator(name='destroy', decorator=swagger_auto_schema(
#     operation_summary='删除部门'
# ))
class Department(viewsets.ModelViewSet):
    """
        部门信息

    retrieve:
        返回一组（查）

    list:
        返回所有组（查）

    create:
        创建新组（增）

    destroy:
        删除现有的一组（删）

    partial_update:
        更新现有组中的一个或多个字段（改：部分更改）

    update:
        更新一组（改：全部更改）

    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class UploadMember(APIView):
    # @swagger_auto_schema(
    #     operation_description='POST /organization/upload/',
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=["department_name", 'uid', 'department_id', 'employee_excel'],
    #         properties={
    #             'department_id': openapi.Schema("department_id", openapi.IN_BODY, label="部门id",
    #                                             type=openapi.TYPE_INTEGER),
    #             'employee_excel': employee_excel,
    #             'uid': openapi.Schema("uid", openapi.IN_BODY, label="uid",
    #                                   type=openapi.TYPE_INTEGER),
    #             'employee_excel': employee_excel
    #         },
    #         # manual_parameters=[uid, name],
    #
    #     ),
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     security=[],
    #     operation_summary='上传公司成员'
    # )
    def post(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})


class ChangeEmployeeDepartment(APIView):
    # @swagger_auto_schema(
    #     operation_description='POST /organization/upload/',
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['uid', 'department_id'],
    #         properties={
    #             'department_id': openapi.Schema("department_id", openapi.IN_BODY, label="部门id",
    #                                             type=openapi.TYPE_INTEGER),
    #             'uid': openapi.Schema("uid", openapi.IN_BODY, label="uid",
    #                                   type=openapi.TYPE_INTEGER),
    #             'employee_excel': employee_excel
    #         },
    #         # manual_parameters=[uid, name],
    #
    #     ),
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     security=[],
    #     operation_summary='修改职员部门'
    # )
    def post(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})


class DepartmentManage(APIView):
    # @swagger_auto_schema(
    #     # operation_description='POST /organization/upload/',
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['uid', 'department_id', "parent_department_id"],
    #         properties={
    #             'department_id': openapi.Parameter("department_id", openapi.IN_BODY, description="部门id",
    #                                                type=openapi.TYPE_INTEGER),
    #             'parent_department_id': openapi.Parameter("parent_department_id", openapi.IN_BODY, description="父级部门id",
    #                                                       type=openapi.TYPE_INTEGER),
    #             'employee_id': openapi.Parameter("parent_department_id", openapi.IN_BODY, description="被编辑的员工id",
    #                                              type=openapi.TYPE_INTEGER),
    #             'uid': openapi.Parameter("uid", openapi.IN_BODY, description="uid",
    #                                      type=openapi.TYPE_INTEGER),
    #         },
    #         # manual_parameters=[uid, name],
    #
    #     ),
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     security=[],
    #     operation_summary='修改部门层级'
    # )
    def post(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})


class DepartmentChildren(APIView):
    # @swagger_auto_schema(operation_description="获取下属部门和成员信息",
    #                      # responses=openapi.Schema(
    #                      #     type=openapi.TYPE_OBJECT,
    #                      #     properties={
    #                      #         'email': email,
    #                      #         'mobile':mobile,
    #                      #         'avatar':avatar,
    #                      #         'sign':sign,
    #                      #         'mobile_checked': mobile_checked,
    #                      #         'email_checked': email_checked,
    #                      #
    #                      #     }),
    #                      responses={
    #                          '200': DepartmentSerializer(many=True),
    #                          '400': 'Bad Request'
    #                      },
    #                      manual_parameters=[uid, department_id, org_id],
    #                      operation_summary='获取下属部门和成员信息')
    @get_request_args
    def get(self, request, args):
        """
        "获取下属部门和成员信息"
        :param request:
        :param args:
        :return:
        """
        data = []
        id = args.get("id")
        # i = table.find_one({"_id": int(id)})
        data.append({'user_name': "", "content": ""})
        return JsonResponse({"data": data})

# class (APIView):
