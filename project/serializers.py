#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-06 11:32
# @Author : wangjue
# @Site : 
# @File : serializers.py
# @Software: PyCharm

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-06 11:31
# @Author : wangjue
# @Site :
# @File : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from project.models import Project, Issue, Discussion, ProjectEmployee, ProjectTag, ProjectMajor


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializing Project
    """

    class Meta:
        model = Project
        fields = [
            'id', 'name', "desc", "cover"
        ]


class IssueSerializer(serializers.ModelSerializer):
    """
    Serializing Issue
    """

    class Meta:
        model = Issue
        fields = [
            'id', 'title', 'desc', 'project_id', 'project_serial_num', 'priority',
            'major', 'owner_uid', 'assigned_uid', 'second_assigned_uid1', 'second_assigned_uid2',
            'second_assigned_uid3', 'state_id', 'is_open', 'positioning', 'drawings', 'published_time', 'closed_time'
        ]


class ProjectEmployeeSerializer(serializers.ModelSerializer):
    """
    Serializing Issue
    """

    class Meta:
        model = ProjectEmployee
        fields = [
            'id', 'project_id', 'employee_id', 'role', 'is_admin'
        ]


class DiscussionSerializer(serializers.ModelSerializer):
    """
    Serializing Discussion
    """

    class Meta:
        model = Discussion
        fields = [
            'id', 'content', 'pics', 'published_time'
        ]


class ProjectTagSerializer(serializers.ModelSerializer):
    """
    Serializing ProjectTag
    """

    class Meta:
        model = ProjectTag
        fields = [
            'id', 'name', 'project_id'
        ]


class ProjectMajorSerializer(serializers.ModelSerializer):
    """
    Serializing ProjectMajor
    """

    class Meta:
        model = ProjectMajor
        fields = [
            'id', 'name', 'project_id'
        ]
