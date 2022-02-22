#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-03 16:54
# @Author : wangjue
# @Site : 
# @File : views.py
# @Software: PyCharm

from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from accounts.serializers import AccountSerializer
from haid_project.utils import get_request_args
from accounts.models import HaidUser
from django.core.cache import cache
from haid_project.settings import REGISTER_CACHE_KEY

# email = openapi.Parameter("email", openapi.IN_QUERY, description="邮箱地址",
#                           type=openapi.TYPE_STRING)
#
# verification_code = openapi.Parameter("verification_code", openapi.IN_QUERY, description="校验码",
#                                       type=openapi.TYPE_INTEGER)
#
# password = openapi.Parameter("password", openapi.IN_QUERY, description="密码",
#                              type=openapi.TYPE_STRING)
# uid = openapi.Parameter("uid", openapi.IN_QUERY, description="用户id",
#                         type=openapi.TYPE_INTEGER)
#
# origin_password = openapi.Parameter("origin_password", openapi.IN_QUERY, description="原始密码",
#                                     type=openapi.TYPE_STRING)
#
# new_password = openapi.Parameter("new_password", openapi.IN_QUERY, description="新密码",
#                                  type=openapi.TYPE_STRING)
#
# avatar = openapi.Parameter("avatar", openapi.IN_QUERY, description="头像地址",
#                            type=openapi.TYPE_STRING)
#
# name = openapi.Parameter("name", openapi.IN_QUERY, description="用户昵称",
#                          type=openapi.TYPE_STRING)
#
# slogan = openapi.Parameter("slogan", openapi.IN_QUERY, description="签名",
#                            type=openapi.TYPE_STRING)
#
# mobile = openapi.Parameter("mobile", openapi.IN_QUERY, description="联系方式",
#                            type=openapi.TYPE_INTEGER)
#
# mobile_checked = openapi.Parameter("mobile_checked", openapi.IN_QUERY, description="联系方式是否已验证",
#                                    type=openapi.TYPE_BOOLEAN)
#
# email_checked = openapi.Parameter("email_checked", openapi.IN_QUERY, description="邮箱是否已验证",
#                                   type=openapi.TYPE_BOOLEAN)
# account_info_response = openapi.Response('response description', AccountSerializer)


class RegisterEmailAccount(APIView):
    '''
    list:
        Return one news
    '''
    serializer_class = AccountSerializer
    queryset =  HaidUser.objects.all()
    # @swagger_auto_schema(
    #     operation_description="apiview post description override",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['email', "verification_code", 'pass_word'],
    #         properties={
    #             'email': openapi.Schema(type=openapi.TYPE_STRING),
    #             'verification_code': openapi.Schema(type=openapi.TYPE_STRING),
    #             'password': openapi.Schema(type=openapi.TYPE_STRING)
    #
    #         },
    #         manual_parameters=[email, verification_code, password],
    #     ),
    #     security=[],
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     operation_summary='通过邮箱注册账号'
    # )
    @get_request_args
    def post(self, request, args):
        data = []
        data_request = request.get_json()
        data_request = data_request if isinstance(data_request, dict) else {}
        verification_code = data_request.get("verification_code")
        system_verification_code = cache.get(REGISTER_CACHE_KEY + email)
        if (verification_code is None) or (verification_code != system_verification_code):
            return JsonResponse({"data": False, "msg": "无效的验证码"})


        authentication_classes = ()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        cache.set(REGISTER_CACHE_KEY + email,)
        return Response(data=True, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()


class AccountInfo(generics.UpdateAPIView, generics.GenericAPIView):
    '''

    '''

    # @swagger_auto_schema(operation_description="获取账号信息",
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
    #                          '200': account_info_response,
    #                          '400': 'Bad Request'
    #                      },
    #                      manual_parameters=[uid],
    #                      operation_summary='获取账号信息')
    @get_request_args
    def get(self, request, args):
        """
        "获取账号信息"
        :param request:
        :param args:
        :return:
        """
        data = []
        id = args.get("id")
        # i = table.find_one({"_id": int(id)})
        data.append({'user_name': "", "content": ""})
        return JsonResponse({"data": data})

    #@swagger_auto_schema(method='get', operation_description="GET /articles/{id}/image/")
    @action(
        methods=["GET"],
        detail=True,
        # ...
        # suffix="List",  # 将这个 action 返回的结果标记为列表，否则 drf-yasg 会根据 detail=True 误判为这是返回单个资源的接口
        # pagination_class=LimitOffsetPagination,
        serializer_class=AccountSerializer,
    )
    def list_comments(self, request, *args, **kwargs):
        data = []
        id = args.get("id")
        # i = table.find_one({"_id": int(id)})
        data.append({'user_name': "", "content": ""})
        return JsonResponse({"data": data})

    # @swagger_auto_schema(
    #     operation_description="api view post description override",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['email', "verification_code", 'pass_word'],
    #         properties={
    #             'uid': uid,
    #             'avatar': avatar,
    #             'name': name,
    #             'slogan': slogan,
    #             'mobile': mobile
    #
    #         },
    #     ),
    #     # responses=openapi.Schema(
    #     #     type=openapi.TYPE_BOOLEAN),
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     security=[],
    #     operation_summary='编辑用户信息'
    # )
    def put(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})
        pass

    # @swagger_auto_schema(
    #     operation_description="api view post description override",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=[],
    #         properties={
    #             'uid': uid,
    #             'avatar': avatar,
    #             'name': name,
    #             'slogan': slogan,
    #             'mobile': mobile
    #
    #         },
    #     ),
    #     # responses=openapi.Schema(
    #     #     type=openapi.TYPE_BOOLEAN),
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     security=[],
    #     operation_summary='编辑用户单条信息'
    # )
    def patch(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})


class ResetPassword(APIView):
    '''

    '''

    # @swagger_auto_schema(
    #     operation_description="重置密码",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['uid', "origin_password", 'new_password'],
    #         properties={
    #             'uid': uid,
    #             'origin_password': origin_password,
    #             'new_password': new_password
    #
    #         },
    #     ),
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     security=[],
    #     operation_summary='重置密码'
    # )
    def post(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})
        pass


class ResetPasswordByMobile(APIView):
    # mobile = openapi.Parameter("mobile", openapi.IN_QUERY, description="手机号",
    #                            type=openapi.TYPE_INTEGER)
    #
    # verification_code = openapi.Parameter("verification_code", openapi.IN_QUERY, description="校验码",
    #                                       type=openapi.TYPE_INTEGER)
    #
    # password = openapi.Parameter("password", openapi.IN_QUERY, description="新密码",
    #                              type=openapi.TYPE_STRING)
    #
    # @swagger_auto_schema(
    #     operation_description="api view post description override",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['mobile', "verification_code", 'password'],
    #         properties={
    #             'mobile': mobile,
    #             'verification_code': verification_code,
    #             'password': password,
    #
    #         }
    #     ),
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     security=[],
    #     operation_summary='通过手机重置密码'
    # )
    def post(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})
        pass


class ResetPasswordByEmail(APIView):
    '''

    '''

    # email = openapi.Parameter("email", openapi.IN_QUERY, description="邮箱地址",
    #                           type=openapi.TYPE_STRING)
    #
    # mobile = openapi.Parameter("mobile", openapi.IN_QUERY, description="联系方式",
    #                            type=openapi.TYPE_INTEGER)
    #
    # verification_code = openapi.Parameter("verification_code", openapi.IN_QUERY, description="校验码",
    #                                       type=openapi.TYPE_INTEGER)
    #
    # password = openapi.Parameter("password", openapi.IN_QUERY, description="密码",
    #                              type=openapi.TYPE_STRING)
    #
    # @swagger_auto_schema(
    #     operation_description="api view post description override",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['email', "verification_code", 'pass_word'],
    #         properties={
    #             'email': email,
    #             'verification_code': verification_code,
    #             'password': password,
    #
    #         },
    #     ),
    #     security=[],
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     operation_summary='通过邮箱重置密码'
    # )
    def post(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})
        pass


# class CheckEmail(APIView):
#     '''
#
#     '''
#
#     @swagger_auto_schema(method='get', operation_description="GET /check_email/", responses={
#         '200': openapi.TYPE_BOOLEAN,
#         '400': 'Bad Request'
#     },
#                          manual_parameters=[email],
#                          operation_summary='邮箱验证')
#     @action(
#         methods=["GET"],
#         detail=True,
#     )
#     def get(self, request, args):
#         data = []
#         id = args.get("id")
#         user_name = args.get("user_name")
#         i = {}
#         data.append({'user_name': i.get("user_name"), "content": i.get("content")})
#         return JsonResponse({"data": data})
#         pass


class CheckMobole(APIView):
    '''

    '''

    # @swagger_auto_schema(method='get', responses={
    #     '200': openapi.TYPE_BOOLEAN,
    #     '400': 'Bad Request'
    # },
    #                      manual_parameters=[mobile],
    #                      operation_summary='手机验证')
    @action(
        methods=["GET"],
        detail=True,

    )
    def get(self, request, args):
        data = []
        id = args.get("id")
        user_name = args.get("user_name")
        i = {}
        data.append({'user_name': i.get("user_name"), "content": i.get("content")})
        return JsonResponse({"data": data})
        pass


class AccountInfoViewsSet(viewsets.ModelViewSet):
    queryset = HaidUser.objects.all()
    serializer_class = AccountSerializer


def account_index(request):
    return HttpResponse("account index.")
