# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include("social_simulator.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^dashboard/', include("social_simulator.dashboard.urls", namespace="dashboard")),
    url(r'^facebook/', include("social_simulator.facebook.urls", namespace="facebook")),
    url(r'^twitter/', include("social_simulator.twitter.urls", namespace="twitter")),
    url(r'^emails/', include("social_simulator.emails.urls", namespace="emails")),
    url(r'^sky_news/', include("social_simulator.sky_news.urls", namespace="sky_news")),
    url(r'^blog/', include("social_simulator.blog.urls", namespace="blog")),
    url(r'^bbc/', include("social_simulator.bbc.urls", namespace="bbc")),
    url(r'^telegraph/', include("social_simulator.telegraph.urls", namespace="telegraph")),
    url(r'^aljazeera/', include("social_simulator.al_jazeera.urls", namespace="aljazeera")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permission Denied")}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
    ]
