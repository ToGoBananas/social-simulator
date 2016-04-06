from django.shortcuts import render
from django.views.generic import TemplateView

from .models import SkyPost


class SkyIndexView(TemplateView):
    template_name = 'sky_news/index.html'

    def get_context_data(self, **kwargs):
        context = super(SkyIndexView, self).get_context_data()
        context['posts'] = SkyPost.objects.all()
        return context


class SkyPostView(TemplateView):
    template_name = 'sky_news/post.html'

    def get_context_data(self, post_pk, **kwargs):
        context = super(SkyPostView, self).get_context_data()
        context['post'] = SkyPost.objects.get(pk=post_pk)
        return context
