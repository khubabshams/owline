from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from ..models import Question
from ..forms import AnswerForm


class QuestionList(generic.ListView):
    model = Question
    queryset = Question.objects.filter(archive=False).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 10


class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'create.html'
    fields = ['title', 'body']

    def get_success_url(self) -> str:
        """
        Get the url of the question
        """
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.slug,
        })

    def form_valid(self, form) -> HttpResponse:
        """
        Add current user to created and modified by and to vote users
        """
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.modified_by = self.request.user
        res = super().form_valid(form)
        self.object.vote_users.add(self.request.user)
        return res


class QuestionUpdate(LoginRequiredMixin, UpdateView):
    fields = ['title', 'body']
    template_name = 'update.html'
    model = Question

    def get_success_url(self) -> str:
        """
        Get the url of the question
        """
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.slug,
        })

    def form_valid(self, form) -> HttpResponse:
        """
        Update modified by user
        """
        self.object = form.save(commit=False)
        self.object.modified_by = self.request.user
        return super().form_valid(form)


class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs) -> HttpResponse:
        """
        Prevent non-admin to delete a question
        """
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super().delete(request, *args, **kwargs)


class QuestionDetail(View):

    def get(self, request, slug, *args, **kwargs) -> HttpResponse:
        """
        Handle get request of the detail view, get question and answers
        """
        queryset = Question.objects.filter(archive=False)
        question = get_object_or_404(queryset, slug=slug)
        answers = question.answers.filter(archive=False).order_by('-votes')
        context = {
            'question': question,
            'answers': answers,
            'answer_form': AnswerForm(),
        }
        return render(request, "question.html", context)
