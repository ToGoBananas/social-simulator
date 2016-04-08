from django.shortcuts import render
from django.views.generic import TemplateView

from .models import AljazeeraPost


class AljazeeraIndexView(TemplateView):
    template_name = 'al_jazeera/index.html'

    def get_context_data(self, **kwargs):
        context = super(AljazeeraIndexView, self).get_context_data()
        context['posts'] = AljazeeraPost.objects.all()
        return context


class AljazeeraPostView(TemplateView):
    template_name = 'al_jazeera/post.html'

    def get_context_data(self, post_pk, **kwargs):
        context = super(AljazeeraPostView, self).get_context_data()
        context['post'] = AljazeeraPost.objects.get(pk=post_pk)
        return context
