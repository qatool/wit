#!/usr/bin/env python
#!coding=utf-8
#python2
'''
 Created by wuyq1 on 2017/3/29.
'''
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from wtifont.models import *


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('title', 'code', 'language', 'style',)

if __name__ == "__main__":
    pass