#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-02-03 16:55
# @Author : wangjue
# @Site : 
# @File : models.py
# @Software: PyCharm

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


# Create your models here.

class HaidUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    avatar = models.CharField(max_length=255, verbose_name="头像图片地址", default="")
    slogan = models.CharField(max_length=255, verbose_name="签名", default="")
    def __str__(self):
        return self.email
    class Meta:
        ordering = ['-id']
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
