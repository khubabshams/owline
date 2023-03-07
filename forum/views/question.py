from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from ..models import Question
from ..forms import AnswerForm, QuestionForm


class QuestionList(generic.ListView):
    model = Question
    queryset = Question.objects.filter(archive=False).order_by('-created_on')
    template_name = 'index.html'
    paginated_by = 5


class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'create.html'
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.slug,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.created_by = self.request.user
        self.object.modified_by = self.request.user
        return super().form_valid(form)


class QuestionUpdate(LoginRequiredMixin, UpdateView):
    fields = ['title', 'body']
    template_name = 'update.html'
    model = Question

    def get_success_url(self):
        return reverse('question_details', current_app='forum', kwargs={
            'slug': self.object.slug,
        })


class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'delete.html'
    success_url = '/'


class QuestionDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Question.objects.filter(archive=False)
        question = get_object_or_404(queryset, slug=slug)
        answers = question.answers.filter(archive=False).order_by('-votes')
        context = {
            'question': question,
            'answers': answers,
            'answer_form': AnswerForm(),
            'question_form': QuestionForm(),
        }
        return render(request, "question.html", context)
