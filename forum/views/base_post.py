from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Question, Answer


def sign_user_post_vote(user, slug, pk, increase=True):
    queryset = Question.objects.filter(archive=False)
    question = get_object_or_404(queryset, slug=slug)

    updated_object = question
    if pk:
        answer_queryset = question.answers.filter(id=pk)
        updated_object = get_object_or_404(answer_queryset)
    voters = updated_object.vote_users.all()
    if user.id not in voters.values_list('id', flat=True):
        updated_object.votes += 1 if increase else -1
        updated_object.vote_users.add(user)
        updated_object.save()
        return True
    return False


@login_required
def upvote(request, slug=False, pk=False):
    result = sign_user_post_vote(request.user, slug, pk)
    if result:
        return redirect(f'/forum/{slug}')
    # todo: handle user in voters & user == created_by
    return redirect(f'/forum/{slug}')


@login_required
def downvote(request, slug=False, pk=False):
    result = sign_user_post_vote(request.user, slug, pk, increase=False)
    if result:
        return redirect(f'/forum/{slug}')
    # todo: handle user in voters & user == created_by
    return redirect(f'/forum/{slug}')
