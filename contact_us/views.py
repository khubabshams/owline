from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Message


class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    template_name = 'contactus.html'
    fields = ['email', 'name', 'body']
    success_url = '/'
