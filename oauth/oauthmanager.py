#!/usr/bin/env python
# encoding: utf-8


"""

"""

from abc import ABCMeta, abstractmethod, abstractproperty
from oauth.models import OAuthUser,OAuthConfig
from django.conf import settings
import requests
import json
import logging
import urllib.parse
from haid_project.utils import parse_dict_to_url, cache_decorator

logger = logging.getLogger(__name__)


class OAuthAccessTokenException(Exception):
    '''
    oauth授权失败异常
    '''


class BaseOauthManager(metaclass=ABCMeta):
    """获取用户授权"""
    AUTH_URL = None
    """获取token"""
    TOKEN_URL = None
    """获取用户信息"""
    API_URL = None
    '''icon图标名'''
    ICON_NAME = None

    def __init__(self, access_token=None):
        self.access_token = access_token
        # self.openid = openid

    @property
    def is_access_token_set(self):
        return self.access_token is not None

    @property
    def is_authorized(self):
        return self.is_access_token_set and self.access_token is not None
    @abstractmethod
    def get_authorization_url(self, nexturl='/'):
        pass

    @abstractmethod
    def get_access_token_by_code(self, code):
        pass

    @abstractmethod
    def get_oauth_userinfo(self):
        pass

    def do_get(self, url, params, headers=None):
        rsp = requests.get(url=url, params=params, headers=headers)
        logger.info(rsp.text)
        return rsp.text

    def do_post(self, url, params, headers=None):
        rsp = requests.post(url, params, headers=headers)
        logger.info(rsp.text)
        return rsp.text

    def get_config(self):
        value = OAuthConfig.objects.filter(type=self.ICON_NAME)
        return value[0] if value else None







@cache_decorator(expiration=100 * 60)
def get_oauth_apps():
    configs = OAuthConfig.objects.filter(is_enable=True).all()
    if not configs:
        return []
    configtypes = [x.type for x in configs]
    applications = BaseOauthManager.__subclasses__()
    apps = [x() for x in applications if x().ICON_NAME.lower() in configtypes]
    return apps


def get_manager_by_type(type):
    applications = get_oauth_apps()
    if applications:
        finds = list(
            filter(
                lambda x: x.ICON_NAME.lower() == type.lower(),
                applications))
        if finds:
            return finds[0]
    return None
