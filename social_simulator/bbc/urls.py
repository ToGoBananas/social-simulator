# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.BbcListView.as_view(),
        name='index'
    ),
    url(
        regex=r'^posts/(?P<post_pk>[0-9]+)/$',
        view=views.BbcPostView.as_view(),
        name='post'
    ),
]
