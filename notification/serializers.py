#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-08 16:35
# @Author : wangjue
# @Site : 
# @File : serializers.py
# @Software: PyCharm


from rest_framework import serializers
from notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializing Project
    """

    class Meta:
        model = Notification
        fields = [
            'id', 'employee_id', "is_read", "org_id", "discussion_id", "issue_id", "project_id", "content",
            "sender_employee_id", "sender_account_id", "type"
        ]
