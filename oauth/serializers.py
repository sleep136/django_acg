#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-20 11:42
# @Author : wangjue
# @Site : 
# @File : serializers.py
# @Software: PyCharm


from rest_framework import serializers
from .models import  OAuthUser


class OauthSerializer(serializers.ModelSerializer):
    """
    Serializing Project
    """

    class Meta:
        model =  OAuthUser
        fields = [
            'id', 'type',  'nickname', 'token', 'picture', 'type'
        ]
