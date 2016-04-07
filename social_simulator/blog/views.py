from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import BlogPost


class BlogListView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data()
        context['posts'] = BlogPost.objects.all()
        return context


class BlogPostView(TemplateView):
    template_name = 'blog/post.html'

    def get_context_data(self, post_pk, **kwargs):
        context = super(BlogPostView, self).get_context_data()
        context['post'] = BlogPost.objects.get(pk=post_pk)
        return context
