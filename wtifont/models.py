#!/usr/bin/env python
#!coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    language = models.CharField(max_length=100, default='python', )
    style = models.CharField(max_length=100, default='friendly', )
    upTime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    cTime = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
