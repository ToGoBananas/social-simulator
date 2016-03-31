from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView
from django.http import HttpResponse

from .models import FacebookPost, Comment, FacebookPostLikes


class FacebookView(TemplateView):
    template_name = 'facebook/base.html'

    def get_context_data(self, **kwargs):
        context = super(FacebookView, self).get_context_data(**kwargs)
        context['posts'] = FacebookPost.objects.all()
        return context


class AddCommentView(View):

    def post(self, request, *args, **kwargs):
        pk = request.POST['pk']
        text = request.POST['text']
        Comment.objects.create(post=FacebookPost.objects.get(pk=pk), user=request.user, text=text)
        return ShowCommentsView.as_view()(request)


class ShowCommentsView(View):

    def post(self, request, *args, **kwargs):
        pk = request.POST['pk']
        comments = FacebookPost.objects.get(pk=pk).comments[:5]
        return render(request, 'facebook/comments.html', {
            'comments': comments
        })


class LikeView(View):

    def post(self, request, *args, **kwargs):
        pk = request.POST['pk']
        post = FacebookPost.objects.get(pk=pk)
        likes = FacebookPostLikes.objects.get_or_create(post=post)[0]
        if request.user not in likes.users.all():
            post.likes += 1
            post.save()
            likes.users.add(request.user)
            return HttpResponse('', status=200)
        else:
            return HttpResponse('', status=203)
