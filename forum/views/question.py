from django.shortcuts import render
from django.views import generic
from ..models import Question


class QuestionList(generic.ListView):
    model: Question
    queryset = Question.objects.filter(archive=False).order_by('-created_on')
    template_name = 'index.html'
    paginated_by = 5
