from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse

from ..models import Answer


class AnswerUpdate(UpdateView):
    fields = ['body',]
    model = Answer

    def get_success_url(self):
        return reverse('question', current_app='forum', kwargs={
            'slug': self.object.related_question.slug,
        })


class AnswerDelete(DeleteView):
    model = Answer
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('question', current_app='forum', kwargs={
            'slug': self.object.related_question.slug,
        })
