from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from ..models import Answer, Question


class AnswerCreate(LoginRequiredMixin, CreateView):
    model = Answer
    login_url = '/index/'
    redirect_field_name = 'index'
    template_name = 'create.html'
    fields = ['body']

    def get_success_url(self):
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.related_question.slug,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        queryset = Question.objects.filter(archive=False)
        question = get_object_or_404(queryset, slug=self.kwargs.get("slug"))

        self.object.related_question = question
        self.object.created_by = self.request.user
        self.object.modified_by = self.request.user
        return super().form_valid(form)


class AnswerUpdate(UpdateView):
    fields = ['body',]
    template_name = 'update.html'
    model = Answer

    def get_success_url(self):
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.related_question.slug,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.modified_by = self.request.user
        return super().form_valid(form)


class AnswerDelete(DeleteView):
    model = Answer
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.related_question.slug,
        })
