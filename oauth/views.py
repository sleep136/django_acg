#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-19 10:03
# @Author : wangjue
# @Site : 
# @File : views.py
# @Software: PyCharm

import datetime
import logging
import random
# Create your views here.
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import HaidUser
from accounts.serializers import AccountSerializer
from haid_project.settings import REDIS_EXPIRE_TIME_EMAIL_VERIFICATION_CODE
from haid_project.settings import REGISTER_CACHE_KEY
from haid_project.utils import get_request_args
from haid_project.utils import send_email, get_current_site, get_md5
from oauth.forms import RequireEmailForm
from oauth.oauthmanager import get_manager_by_type, OAuthAccessTokenException
from accounts.models import HaidUser
from .models import OAuthUser
from .serializers import OauthSerializer

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

logger = logging.getLogger(__name__)


class RegisterEmailAccountView(APIView):
    '''
    list:
        Return one news
    '''
    serializer_class = OauthSerializer
    queryset = HaidUser.objects.all()

    # @swagger_auto_schema(
    #     operation_description="api view post description override",
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['email', 'verification_code', 'password'],
    #         properties={'email': openapi.Schema(type=openapi.TYPE_STRING),
    #                     'verification_code': openapi.Schema(type=openapi.TYPE_STRING),
    #                     'password': openapi.Schema(type=openapi.TYPE_STRING)}
    #     ),
    #     # responses=openapi.Schema(
    #     #     type=openapi.TYPE_BOOLEAN),
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     security=[],
    #     operation_summary='通过邮箱注册账号',
    # )
    def post(self, request):
        data = []
        # data_request = request.get_json()
        data_request = request.data if isinstance(request.data, dict) else {}
        email = data_request.get("email")
        verification_code = data_request.get("verification_code")
        system_verification_code = cache.get(REGISTER_CACHE_KEY + email)
        if (verification_code is None) or (system_verification_code is None):
            logger.warning("system_verification_code:%s system_verification_code:%s" % (
            verification_code, system_verification_code))
            return JsonResponse({"data": False, "msg": "无效的验证码"})
        if str(verification_code) != str(system_verification_code):
            logger.warning("system_verification_code:%s system_verification_code:%s" % (
                verification_code, system_verification_code))
            return JsonResponse({"data": False, "msg": "无效的验证码"})
        if check_token_in_db("email", email):
            return JsonResponse({"data": False, "msg": "邮箱地址已经注册过"})
        authentication_classes = ()
        data_request["type"] = 'email'
        data_request["nickname"] = ''
        #account = HaidUser.objects.create(password=data_request['password'])
        OAuthUser.objects.create(type='email', token=email, nickname='')
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


def get_redirect_url(request):
    nexturl = request.GET.get('next_url', None)
    if not nexturl or nexturl == '/login/' or nexturl == '/login':
        nexturl = '/'
        return nexturl
    p = urlparse(nexturl)
    if p.netloc:
        site = get_current_site().domain
        if not p.netloc.replace('www.', '') == site.replace('www.', ''):
            logger.info('非法url:' + nexturl)
            return "/"
    return nexturl


def oauthlogin(request):
    type = request.GET.get('type', None)
    if not type:
        return HttpResponseRedirect('/')


def authorize(request):
    type = request.GET.get('type', None)
    if not type:
        return HttpResponseRedirect('/')
    manager = get_manager_by_type(type)
    if not manager:
        return HttpResponseRedirect('/')
    code = request.GET.get('code', None)
    try:
        rsp = manager.get_access_token_by_code(code)
    except OAuthAccessTokenException as e:
        logger.warning("OAuthAccessTokenException:" + str(e))
        return HttpResponseRedirect('/')
    except Exception as e:
        logger.error(e)
        rsp = None
    nexturl = get_redirect_url(request)
    if not rsp:
        return HttpResponseRedirect(manager.get_authorization_url(nexturl))
    user = manager.get_oauth_userinfo()
    if user:
        if not user.nikename or not user.nikename.strip():
            import datetime
            user.nikename = "haid" + datetime.datetime.now().strftime('%y%m%d%I%M%S')
        try:
            temp = OAuthUser.objects.get(type=type)
            temp.picture = user.picture
            temp.matedata = user.matedata
            temp.nikename = user.nikename
            user = temp
        except ObjectDoesNotExist:
            pass

        if user.email:
            with transaction.atomic():
                author = None
                try:
                    author = get_user_model().objects.get(id=user.author_id)
                except ObjectDoesNotExist:
                    pass
                if not author:
                    result = get_user_model().objects.get_or_create(email=user.email)
                    author = result[0]
                    if result[1]:
                        try:
                            get_user_model().objects.get(username=user.nikename)
                        except ObjectDoesNotExist:
                            author.username = user.nikename
                        else:
                            author.username = "haid" + datetime.datetime.now().strftime('%y%m%d%I%M%S')
                        author.source = 'authorize'
                        author.save()

                user.author = author
                user.save()

                login(request, author)
                return HttpResponseRedirect(nexturl)
        else:
            user.save()
            url = reverse('oauth:require_email', kwargs={
                'oauthid': user.id
            })

            return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect(nexturl)


def emailconfirm(request, id, sign):
    if not sign:
        return HttpResponseForbidden()
    if not get_md5(
            settings.SECRET_KEY +
            str(id) +
            settings.SECRET_KEY).upper() == sign.upper():
        return HttpResponseForbidden()
    oauthuser = get_object_or_404(OAuthUser, pk=id)
    with transaction.atomic():
        if oauthuser.author:
            author = get_user_model().objects.get(pk=oauthuser.author_id)
        else:
            result = get_user_model().objects.get_or_create(email=oauthuser.email)
            author = result[0]
            if result[1]:
                author.source = 'emailconfirm'
                author.username = oauthuser.nikename.strip() if oauthuser.nikename.strip(
                ) else "haid" + datetime.datetime.now().strftime('%y%m%d%I%M%S')
                author.save()
        oauthuser.author = author
        oauthuser.save()
    # oauth_user_login_signal.send(
    #     sender=emailconfirm.__class__,
    #     id=oauthuser.id)
    login(request, author)

    site = get_current_site().domain
    content = '''
     <p>恭喜您，您已经成功绑定您的邮箱，您可以使用{type}来直接免密码登录本网站.欢迎您继续关注本站，地址是</p>

                <a href="{url}" rel="bookmark">{url}</a>

                再次感谢您！
                <br />
                如果上面链接无法打开，请将此链接复制至浏览器。
                {url}
    '''.format(type=oauthuser.type, url='http://' + site)

    send_email(emailto=[oauthuser.email, ], title='恭喜您绑定成功!', content=content)
    url = reverse('oauth:bindsuccess', kwargs={
        'oauthid': id
    })
    url = url + '?type=success'
    return HttpResponseRedirect(url)


class RequireEmailView(FormView):
    form_class = RequireEmailForm

    # template_name = 'oauth/require_email.html'

    def get(self, request, *args, **kwargs):
        oauthid = self.kwargs['oauthid']
        oauthuser = get_object_or_404(OAuthUser, pk=oauthid)
        if oauthuser.email:
            pass
            # return HttpResponseRedirect('/')

        return super(RequireEmailView, self).get(request, *args, **kwargs)

    def get_initial(self):
        oauthid = self.kwargs['oauthid']
        return {
            'email': '',
            'oauthid': oauthid
        }

    def get_context_data(self, **kwargs):
        oauthid = self.kwargs['oauthid']
        oauthuser = get_object_or_404(OAuthUser, pk=oauthid)
        if oauthuser.picture:
            kwargs['picture'] = oauthuser.picture
        return super(RequireEmailView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        oauthid = form.cleaned_data['oauthid']
        oauthuser = get_object_or_404(OAuthUser, pk=oauthid)
        oauthuser.email = email
        oauthuser.save()
        sign = get_md5(settings.SECRET_KEY +
                       str(oauthuser.id) + settings.SECRET_KEY)
        site = get_current_site().domain
        if settings.DEBUG:
            site = '127.0.0.1:8000'
        path = reverse('oauth:email_confirm', kwargs={
            'id': oauthid,
            'sign': sign
        })
        url = "http://{site}{path}".format(site=site, path=path)

        content = """
                <p>请点击下面链接绑定您的邮箱</p>

                <a href="{url}" rel="bookmark">{url}</a>

                再次感谢您！
                <br />
                如果上面链接无法打开，请将此链接复制至浏览器。
                {url}
                """.format(url=url)
        send_email(emailto=[email, ], title='绑定您的电子邮箱', content=content)
        url = reverse('oauth:bindsuccess', kwargs={
            'oauthid': oauthid
        })
        url = url + '?type=email'
        return HttpResponseRedirect(url)


def bindsuccess(request, oauthid):
    type = request.GET.get('type', None)
    oauthuser = get_object_or_404(OAuthUser, pk=oauthid)
    if type == 'email':
        title = '绑定成功'
        content = "恭喜您，还差一步就绑定成功了，请登录您的邮箱查看邮件完成绑定，谢谢。"
    else:
        title = '绑定成功'
        content = "恭喜您绑定成功，您以后可以使用{type}来直接免密码登录本站啦，感谢您对本站对关注。".format(
            type=oauthuser.type)
    return render(request, 'oauth/bindsuccess.html', {
        'title': title,
        'content': content
    })


class GetVerificationCode(APIView):
    '''
    list:
        Return one news
    '''

    # @swagger_auto_schema(
    #     operation_description="apiview post description override",
    #
    #     manual_parameters=[email],
    #     security=[],
    #     responses={
    #         '200': openapi.TYPE_BOOLEAN,
    #         '400': 'Bad Request'
    #     },
    #     operation_summary='获取邮箱验证码'
    # )
    @get_request_args
    def get(self, request, args):
        return get_verification_code(request)


def get_verification_code(request):
    email = request.GET.get('email', None)
    verification_code = random.randint(100000, 999999)
    if email is None:
        return JsonResponse({"data": False, "msg": "请输入正确的邮箱地址"})

    cache.set(REGISTER_CACHE_KEY + email, verification_code, REDIS_EXPIRE_TIME_EMAIL_VERIFICATION_CODE)

    title = '邮箱验证'
    content = "您好，您的邮箱验证码是{code}，请在5分钟内在网页上输入您的邮箱验证码，谢谢。".format(
        code=verification_code)
    send_email([email], title, content)

    return JsonResponse({"data": True})


def check_token_in_db(type, token):
    """
    判断该登录方式及数据是否已经在数据库中
    :param type:
    :param token:
    :return:
    """
    verify_records = OAuthUser.objects.filter(type=type, token=token).all()
    if verify_records:
        return True
    return False
