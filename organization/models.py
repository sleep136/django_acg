#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-06 12:56
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

    # def save(self, *args, **kwargs):
    #     is_update_views = isinstance(
    #         self,
    #         Article) and 'update_fields' in kwargs and kwargs['update_fields'] == ['views']
    #     if is_update_views:
    #         Article.objects.filter(pk=self.pk).update(views=self.views)
    #     else:
    #         if 'slug' in self.__dict__:
    #             slug = getattr(
    #                 self, 'title') if 'title' in self.__dict__ else getattr(
    #                 self, 'name')
    #             setattr(self, 'slug', slugify(slug))
    #         super().save(*args, **kwargs)
    #
    # def get_full_url(self):
    #     site = get_current_site().domain
    #     url = "https://{site}{path}".format(site=site,
    #                                         path=self.get_absolute_url())
    #     return url

    class Meta:
        abstract = True


class Organization(BaseModel):
    """组织"""

    name = models.CharField('名字', max_length=200, unique=True)
    short_name = models.CharField('简称', max_length=50, unique=True)
    logo_pic = models.CharField('logo地址', max_length=200)
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




class Department(BaseModel):
    """部门"""

    name = models.CharField('名字', max_length=200, unique=True)

    organization = models.ForeignKey(
        'Organization',
        verbose_name='公司',
        on_delete=models.CASCADE,
        blank=False,
        null=False)


    def __str__(self):
        return self.name



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def employee_list(self):
        cache_key = 'department_employee_{id}'.format(id=self.id)
        value = cache.get(cache_key)
        if value:
            logger.info('get department comments:{id}'.format(id=self.id))
            return value
        else:
            comments = self.comment_set.filter(is_enable=True)
            cache.set(cache_key, comments, 60 * 100)
            logger.info('set article comments:{id}'.format(id=self.id))
            return comments

class Employee(BaseModel):
    """职员"""

    name = models.CharField('名字', max_length=200, unique=True)

    organization = models.ForeignKey(
        'Organization',
        verbose_name='公司',
        on_delete=models.CASCADE,
        blank=False,
        null=False)

    def __str__(self):
        return self.name



class Title(BaseModel):
    """职位"""

    name = models.CharField('名字', max_length=200, unique=True)

    organization = models.ForeignKey(
        'Organization',
        verbose_name='公司',
        on_delete=models.CASCADE,
        blank=False,
        null=False)

    def __str__(self):
        return self.name