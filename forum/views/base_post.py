from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from typing import Union

from ..models import Question, Answer


def get_updated_object(slug, pk) -> Union[Answer, Question]:
    """
    Get the needed object (answer or question) based on given params
    """
    queryset = Question.objects.filter(archive=False)
    question = get_object_or_404(queryset, slug=slug)

    updated_object = question
    if pk:
        answer_queryset = question.answers.filter(id=pk)
        updated_object = get_object_or_404(answer_queryset)
    return updated_object


def action_sign_user_post_vote(request, slug, pk, increase=True) \
        -> HttpResponseRedirect:
    """
    Sign user vote (upvote, downvote) and give the user feedback
    """
    user = request.user
    updated_object = get_updated_object(slug=slug, pk=pk)
    voters = updated_object.vote_users.all()
    post_name = pk and 'an answer' or 'a question'
    if user.id == updated_object.created_by.id:
        messages.error(request,
                       f"You cannot sign a vote for {post_name} of your own.")
    elif user.id not in voters.values_list('id', flat=True):
        vote = 1 if increase else -1
        updated_object.votes += vote
        updated_object.vote_users.add(user)
        updated_object.created_by.profile.score += vote
        updated_object.save()
        updated_object.created_by.profile.save()
        messages.success(request,
                         f"Your vote has been signed successfully.")
    else:
        messages.error(request,
                       f"You cannot sign a vote twice for {post_name}.")
    return redirect(f'/forum/{slug}/')


def action_accept_answer(request, slug, pk) -> HttpResponseRedirect:
    """
    Mark an answer as accepted, question as answered
    """
    user = request.user
    answer = get_updated_object(slug=slug, pk=pk)
    if not any([answer.accepted, answer.related_question.answered]) and\
            user == answer.related_question.created_by:
        answer.accepted = True
        answer.related_question.answered = True
        if user.id != answer.created_by.id:
            answer.votes += 3
            answer.created_by.profile.score += 3
            answer.created_by.profile.save()
        answer.save()
        answer.related_question.save()
        messages.success(request, "an Answer has been accepted successfully.")
    elif answer.accepted:
        messages.error(request, "Answer is already accepted before.")
    elif answer.related_question.answered:
        messages.error(request, "Question is already has an accepted answer.")
    else:
        # user.id != answer.related_question.created_by.id
        messages.error(request,
                       "You can only accept answers to your own questions.")
    return redirect(f'/forum/{slug}/')


@login_required
def upvote(request, slug=False, pk=False) -> HttpResponseRedirect:
    """
    Sign an upvote of question/ answer
    """
    return action_sign_user_post_vote(request=request, slug=slug, pk=pk)


@login_required
def downvote(request, slug=False, pk=False) -> HttpResponseRedirect:
    """
    Sign an downvote of question/ answer
    """
    return action_sign_user_post_vote(request=request, slug=slug, pk=pk,
                                      increase=False)


@login_required
def accept(request, slug=False, pk=False) -> HttpResponseRedirect:
    """
    Accept an answer
    """
    return action_accept_answer(request=request, slug=slug, pk=pk)
