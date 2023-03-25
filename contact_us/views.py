from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Message


class MessageList(generic.ListView):
    model = Message
    queryset = Message.objects.filter(archive=False).order_by('-created_on')
    template_name = 'inbox.html'
    paginated_by = 10


class MessageDetail(View):

    def get(self, request, pk, *args, **kwargs) -> HttpResponse:
        """
        Handle get request of the view, if message is unread change it to false
        """
        queryset = Message.objects.filter(archive=False)
        message = get_object_or_404(queryset, pk=pk)
        if message.unread:
            message.unread = False
            message.save()
        context = {
            'message': message,
        }
        return render(request, "message.html", context)


class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    template_name = 'contactus.html'
    fields = ['email', 'name', 'body']
    success_url = '/'
