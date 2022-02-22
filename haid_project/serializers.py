#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-04 17:10
# @Author : wangjue
# @Site : 
# @File : seriallzers.py
# @Software: PyCharm

from rest_framework import serializers
from haid_project.models import APIInfo


class APIInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIInfo
        fields = "__all__"


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = APIInfo
        fields = "__all__"
