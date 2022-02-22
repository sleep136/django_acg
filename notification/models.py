#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-08 16:34
# @Author : wangjue
# @Site : 
# @File : models.py
# @Software: PyCharm


from django.db import models
from django.utils.timezone import now
from django.conf import settings
from haid_project.utils import cache_decorator, cache

import logging

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('创建时间', default=now)
    update_time = models.DateTimeField('修改时间', default=now)

    class Meta:
        abstract = True


class Notification(BaseModel):
    """通知"""
    # emloyee_id = models.CharField('职员id', max_length=20)
    employee_id = models.IntegerField('职员id')
    is_read = models.IntegerField('是否已读')
    org_id = models.IntegerField('组织id')
    issue_id = models.IntegerField('问题id')
    discussion_id = models.IntegerField('回复id')
    project_id = models.IntegerField('项目id')
    content = models.CharField('内容', max_length=255)
    sender_employee_id = models.IntegerField('发送人id')
    sender_account_id = models.IntegerField('发送人账户id（特殊场景存）')
    type = models.IntegerField('类型： 1:发起问题 2:回答了问题 3:关闭问题 4:加入组织申请 5:邀请加入项目')

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
