from django.shortcuts import render
from django.views.generic import View, TemplateView

from .models import FacebookPost


class FacebookView(TemplateView):
    template_name = 'facebook/base.html'

    def get_context_data(self, **kwargs):
        context = super(FacebookView, self).get_context_data(**kwargs)
        context['posts'] = FacebookPost.objects.all()
        return context
