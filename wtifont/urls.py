#!/usr/bin/env python
#!coding=utf-8
#python2
'''
 Created by wuyq1 on 2017/3/29.
'''

from django.conf.urls import url
from wtifont import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^tests/$', views.test_list),
    url(r'^tests/(?P<test_id>[0-9]+)/$', views.test_detail),
]
