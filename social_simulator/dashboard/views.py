# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from social_simulator.emails.models import Message
from .models import Post


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        posts = []
        for post_provider in Post.__subclasses__():
            posts.append(post_provider.objects.last())
        context['posts'] = posts
        context['emails'] = Message.objects.filter(recipients__in=[self.request.user])
        return context


class DashboardSpecificView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/specific.html'

    def get_context_data(self, post_class_name, **kwargs):
        context = super(DashboardSpecificView, self).get_context_data(**kwargs)

        for post in Post.__subclasses__():
            if str(post.__name__) == post_class_name:
                context['posts'] = post.objects.all()
        return context

