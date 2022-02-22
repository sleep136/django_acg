#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-19 17:27
# @Author : wangjue
# @Site : 
# @File : db_redis.py
# @Software: PyCharm

import traceback
from haid_project.settings import REDIS_PASSWORD
import redis


def get_redis_conn(opts={}, decode_responses=True):
    """
    获取redis连接实例
    :param opts: dict redis参数, {'host': '127.0.0.1', 'port': 6379, 'db': 0, 'timeout': 1}
    :param decode_responses bool 是否decode，默认为True
    :return: object 返回redis连接对象
    """
    try:
        redis_conn = redis.Redis(
            host=opts.get('host', '127.0.0.1'),

            port=int(opts.get('port', 6379)),
            password=REDIS_PASSWORD,
            socket_timeout=int(opts.get('timeout', 1)),
            db=int(opts.get('db', 0)),
            decode_responses=decode_responses

        )
    except:
        raise redis.ConnectionError(traceback.format_exc())
    return redis_conn


def get_redis_conn_pool(opts={}, decode_responses=True):
    """
    获取redis连接池
    :param opts: dict redis参数, {'host': '127.0.0.1', 'port': 6379, 'db': 0, 'timeout': 1}
    :param decode_responses: decode_responses bool 是否decode，默认为True
    :return: object 返回redis连接池对象
    """
    pool = redis.ConnectionPool(
        host=opts.get('host', 'localhost'),
        port=int(opts.get('port', 6379)),
        socket_timeout=int(opts.get('timeout', 1)),
        db=int(opts.get('db', 0)),
        decode_responses=decode_responses
    )
    return redis.Redis(connection_pool=pool)