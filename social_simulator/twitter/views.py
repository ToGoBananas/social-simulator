from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

from .models import TwitterPost, TwitterPostTwitts


class TwitterView(TemplateView):
    template_name = 'twitter/base.html'

    def get_context_data(self, **kwargs):
        context = super(TwitterView, self).get_context_data(**kwargs)
        context['posts'] = TwitterPost.objects.all()
        return context


class RetweetView(View):

    def post(self, request, *args, **kwargs):
        pk = request.POST['pk']
        post = TwitterPost.objects.get(pk=pk)
        retweets = TwitterPostTwitts.objects.get_or_create(post=post)[0]
        if request.user not in retweets.users.all():
            post.retweets += 1
            post.save()
            retweets.users.add(request.user)
            return HttpResponse('', status=200)
        else:
            return HttpResponse('', status=203)
