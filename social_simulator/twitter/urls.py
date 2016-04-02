# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.TwitterView.as_view(),
        name='index'
    ),
    url(
        regex=r'^retweet/$',
        view=views.RetweetView.as_view(),
        name='retweet'
    ),
]
