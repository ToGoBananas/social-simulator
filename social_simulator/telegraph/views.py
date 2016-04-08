from django.shortcuts import render
from django.views.generic import TemplateView

from .models import TelegraphPost


class TelegraphIndexView(TemplateView):
    template_name = 'telegraph/index.html'

    def get_context_data(self, **kwargs):
        context = super(TelegraphIndexView, self).get_context_data()
        context['posts'] = TelegraphPost.objects.all()
        return context


class TelegraphPostView(TemplateView):
    template_name = 'telegraph/post.html'

    def get_context_data(self, post_pk, **kwargs):
        context = super(TelegraphPostView, self).get_context_data()
        context['post'] = TelegraphPost.objects.get(pk=post_pk)
        return context
