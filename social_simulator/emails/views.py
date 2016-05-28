from django.shortcuts import render
from django.views.generic import ListView, View, CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import Message
from .forms import MessageCreateForm


class MessageListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Message.objects.filter(recipients__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(MessageListView, self).get_context_data()
        context['form'] = MessageCreateForm()
        return context


class MessageCreateView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        form = MessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=203)
