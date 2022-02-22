#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-05 11:43
# @Author : wangjue
# @Site : 
# @File : utils.py
# @Software: PyCharm
import json
from django.core.cache import cache
from django.contrib.sites.models import Site
from hashlib import md5
import logging

logger = logging.getLogger(__name__)


def get_request_args(func):
    def _get_request_args(self, request):
        if request.method == 'GET':
            args = request.GET
        else:
            body = request.body
            if body:
                try:
                    args = json.loads(body)
                except Exception as e:
                    print(e)
                    # return makeJsonResponse(status=StatusCode.EXECUTE_FAIL, message=str(e))
                    args = request.POST
            else:
                args = request.POST
        return func(self, request, args)

    return _get_request_args


def cache_decorator(expiration=3 * 60):
    def wrapper(func):
        def news(*args, **kwargs):
            try:
                view = args[0]
                key = view.get_cache_key()
            except BaseException:
                key = None
            if not key:
                unique_str = repr((func, args, kwargs))

                m = md5(unique_str.encode('utf-8'))
                key = m.hexdigest()
            value = cache.get(key)
            if value is not None:
                # logger.info('cache_decorator get cache:%s key:%s' % (func.__name__, key))
                if str(value) == '__default_cache_value__':
                    return None
                else:
                    return value
            else:
                logger.info(
                    'cache_decorator set cache:%s key:%s' %
                    (func.__name__, key))
                value = func(*args, **kwargs)
                if value is None:
                    cache.set(key, '__default_cache_value__', expiration)
                else:
                    cache.set(key, value, expiration)
                return value

        return news

    return wrapper


def send_email(emailto, title, content):
    from haid_project.signals import send_email_signal
    send_email_signal.send(
        send_email.__class__,
        emailto=emailto,
        title=title,
        content=content)


@cache_decorator()
def get_current_site():
    site = Site.objects.get_current()
    return site

def get_md5(str):
    m = md5(str.encode('utf-8'))
    return m.hexdigest()



def parse_dict_to_url(dict):
    from urllib.parse import quote
    url = '&'.join(['{}={}'.format(quote(k, safe='/'), quote(v, safe='/'))
                    for k, v in dict.items()])
    return url




def delete_view_cache(prefix, keys):
    from django.core.cache.utils import make_template_fragment_key
    key = make_template_fragment_key(prefix, keys)
    cache.delete(key)
