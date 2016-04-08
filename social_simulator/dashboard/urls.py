# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.DashboardView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<post_class_name>.+)/$',
        view=views.DashboardSpecificView.as_view(),
        name='specific'
    ),
]
