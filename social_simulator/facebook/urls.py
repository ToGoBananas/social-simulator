# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.FacebookView.as_view(),
        name='index'
    ),
    url(
        regex=r'^add_comment/$',
        view=views.AddCommentView.as_view(),
        name='add_comment'
    ),
    url(
        regex=r'^show_comments/$',
        view=views.ShowCommentsView.as_view(),
        name='show_comments'
    ),
    url(
        regex=r'^like/$',
        view=views.LikeView.as_view(),
        name='like'
    ),
]
