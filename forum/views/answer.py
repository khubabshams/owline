from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from ..models import Answer, Question


class AnswerCreate(LoginRequiredMixin, CreateView):
    model = Answer
    template_name = 'create.html'
    fields = ['body']

    def get_success_url(self) -> str:
        """
        Get the url of the related question
        """
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.related_question.slug,
        })

    def form_valid(self, form) -> HttpResponse:
        """
        Add user to created and modified by, and related question
        """
        self.object = form.save(commit=False)
        queryset = Question.objects.filter(archive=False)
        question = get_object_or_404(queryset, slug=self.kwargs.get("slug"))
        self.object.related_question = question
        self.object.created_by = self.request.user
        self.object.modified_by = self.request.user
        res = super().form_valid(form)
        self.object.vote_users.add(self.request.user)
        return res


class AnswerUpdate(LoginRequiredMixin, UpdateView):
    fields = ['body',]
    template_name = 'update.html'
    model = Answer

    def get_success_url(self) -> str:
        """
        Get the url of the related question
        """
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.related_question.slug,
        })

    def form_valid(self, form) -> HttpResponse:
        """
        Update modified by with current user
        """
        self.object = form.save(commit=False)

        self.object.modified_by = self.request.user
        return super().form_valid(form)


class AnswerDelete(LoginRequiredMixin, DeleteView):
    model = Answer
    template_name = 'delete.html'

    def get_success_url(self) -> str:
        """
        Get the url of the related question
        """
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.related_question.slug,
        })

    def delete(self, request, *args, **kwargs) -> HttpResponse:
        """
        Prevent non-admin to delete an answer
        """
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super().delete(request, *args, **kwargs)
