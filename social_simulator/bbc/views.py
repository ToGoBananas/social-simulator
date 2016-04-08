from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import BbcPost


class BbcListView(LoginRequiredMixin, TemplateView):
    template_name = 'bbc/index.html'

    def get_context_data(self, **kwargs):
        context = super(BbcListView, self).get_context_data()
        context['posts'] = BbcPost.objects.all()
        return context


class BbcPostView(TemplateView):
    template_name = 'bbc/post.html'

    def get_context_data(self, post_pk, **kwargs):
        context = super(BbcPostView, self).get_context_data()
        context['post'] = BbcPost.objects.get(pk=post_pk)
        return context
