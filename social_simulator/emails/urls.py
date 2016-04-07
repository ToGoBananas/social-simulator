# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.MessageListView.as_view(),
        name='index'
    ),
    url(
        regex=r'^create/$',
        view=views.MessageCreateView.as_view(),
        name='create'
    ),
]
