from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Question, Answer


def get_updated_object(slug, pk):
    queryset = Question.objects.filter(archive=False)
    question = get_object_or_404(queryset, slug=slug)

    updated_object = question
    if pk:
        answer_queryset = question.answers.filter(id=pk)
        updated_object = get_object_or_404(answer_queryset)
    return updated_object


def action_sign_user_post_vote(user, slug, pk, increase=True):
    updated_object = get_updated_object(slug=slug, pk=pk)
    voters = updated_object.vote_users.all()
    if user.id not in voters.values_list('id', flat=True):
        vote = 1 if increase else -1
        updated_object.votes += vote
        updated_object.vote_users.add(user)
        updated_object.created_by.profile.score += vote
        updated_object.save()
        updated_object.created_by.profile.save()
        return True
    return False


def action_accept_answer(user, slug, pk):
    answer = get_updated_object(slug=slug, pk=pk)
    if not any([answer.accepted, answer.related_question.answered,
                user == answer.created_by]) and\
            user == answer.related_question.created_by:
        answer.related_question.answered = True
        answer.accepted = True
        answer.related_question.save()
        answer.save()
        return True
    return False


@login_required
def upvote(request, slug=False, pk=False):
    result = action_sign_user_post_vote(user=request.user, slug=slug, pk=pk)
    if result:
        return redirect(f'/forum/{slug}')
    # todo: handle user in voters & user == created_by
    return redirect(f'/forum/{slug}')


@login_required
def downvote(request, slug=False, pk=False):
    result = action_sign_user_post_vote(user=request.user, slug=slug, pk=pk,
                                        increase=False)
    if result:
        return redirect(f'/forum/{slug}')
    # todo: handle user in voters & user == created_by
    return redirect(f'/forum/{slug}')


@login_required
def accept(request, slug=False, pk=False):
    result = action_accept_answer(user=request.user, slug=slug, pk=pk)
    if result:
        return redirect(f'/forum/{slug}')
    # todo: handle already accepted & user == created_by &
    # found other accepted answer & user != question.created_by
    return redirect(f'/forum/{slug}')
