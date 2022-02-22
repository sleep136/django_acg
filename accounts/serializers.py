#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-05 15:05
# @Author : wangjue
# @Site : 
# @File : serializers.py
# @Software: PyCharm

from rest_framework.serializers import Serializer
from rest_framework import serializers


class AccountSerializer(Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField( label="名字")
    slogan = serializers.CharField(label="签名")
    avatar = serializers.CharField(label= "头像")

