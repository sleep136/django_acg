#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-06 11:31
# @Author : wangjue
# @Site : 
# @File : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from organization.models import Organization, Department


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Serializing Organization
    """

    class Meta:
        model = Organization
        fields = [
            'id', 'name', "short_name", "logo_pic"
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializing Department
    """

    class Meta:
        model = Department
        fields = [
            'id', 'name'
        ]
