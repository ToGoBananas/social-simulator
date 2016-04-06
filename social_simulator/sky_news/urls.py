# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.SkyIndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<post_pk>[0-9]+)/$',
        view=views.SkyPostView.as_view(),
        name='post'
    ),
]
