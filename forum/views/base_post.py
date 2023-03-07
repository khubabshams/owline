from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Question, Answer


@login_required
def upvote(request, slug=False, pk=False):
    if slug:
        queryset = Question.objects.filter(archive=False)
        question = get_object_or_404(queryset, slug=slug)

        question.votes += 1
        question.save()
        return redirect(f'/forum/{slug}')
    return redirect(f'/forum/{slug}')


@login_required
def downvote(request, slug=False, pk=False):
    pass
