#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-06 13:56
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


class Project(BaseModel):
    """项目"""

    name = models.CharField('名字', max_length=200)
    desc = models.CharField('项目简介', max_length=200)
    cover = models.CharField('封面', max_length=200)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='拥有者',
        blank=False,
        null=False,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def employee_list(self):
        cache_key = 'organization_employee_{id}'.format(id=self.id)
        value = cache.get(cache_key)
        if value:
            logger.info('get organization employee:{id}'.format(id=self.id))
            return value
        else:
            comments = self.comment_set.filter(is_enable=True)
            cache.set(cache_key, comments, 60 * 100)
            logger.info('set organization employee:{id}'.format(id=self.id))
            return comments


class Issue(BaseModel):
    """问题"""

    title = models.CharField('标题', max_length=200)
    desc = models.CharField('描述', max_length=200)
    project_id = models.IntegerField('项目id')
    project_serial_num = models.IntegerField('项目自增单号')
    priority = models.IntegerField('优先级')
    major = models.IntegerField('问题所属专业')
    owner_uid = models.IntegerField('拥有者uid')
    assigned_uid = models.IntegerField('指派uid')
    second_assigned_uid1 = models.IntegerField('二级责任人1')
    second_assigned_uid2 = models.IntegerField('二级责任人2')
    second_assigned_uid3 = models.IntegerField('二级责任人3')
    state_id = models.IntegerField('状态id')
    is_open = models.IntegerField('是否开启')
    positioning = models.TextField('轴线定位')
    drawings = models.TextField('图纸')
    published_time = models.IntegerField('发布时间')
    closed_time = models.IntegerField('关闭时间')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Discussion(BaseModel):
    """回复"""
    issue_id = models.IntegerField('问题id')
    content = models.CharField('描述', max_length=200)
    pics = models.TextField('图片')
    published_time = models.IntegerField('发布时间')

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ProjectEmployee(BaseModel):
    """项目成员"""
    project_id = models.IntegerField('项目id')
    employee_id = models.IntegerField('成员id')
    role = models.IntegerField('角色')
    is_admin = models.IntegerField('是否为管理员')

    def __str__(self):
        return self.role

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ProjectTag(BaseModel):
    """项目标签"""
    name = models.CharField('标签名', max_length=20)
    project_id = models.IntegerField('项目id')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ProjectMajor(BaseModel):
    """项目专业"""
    name = models.CharField('专业名', max_length=20)
    project_id = models.IntegerField('项目id')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
