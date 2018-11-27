# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 2018-11-15 21:36

from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', et),
    url(r'^et/', et),
    url(r'^serverData/', serverData),
    url(r'^serverList/', serverList),
    url(r'^serverList1/', serverList1),

]

urlpatterns +=[
    url(r'^gateone/', gateone),
    url(r'^gateonev2/', gateonev2),
    url(r'^gateValid/', gateValid),

]