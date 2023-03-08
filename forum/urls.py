from .views import question, answer, upvote, downvote, accept
from django.urls import path

urlpatterns = [
    path('', question.QuestionList.as_view(), name='home'),
    path('forum/', question.QuestionList.as_view(), name='forum'),

    path('forum/create/', question.QuestionCreate.as_view(),
         name='question_create'),
    path('forum/<slug:slug>/', question.QuestionDetail.as_view(),
         name='question_details'),
    path('forum/<slug:slug>/update/', question.QuestionUpdate.as_view(),
         name='question_update'),
    path('forum/<slug:slug>/delete/', question.QuestionDelete.as_view(),
         name='question_delete'),

    path('forum/<slug:slug>/create/', answer.AnswerCreate.as_view(),
         name='answer_create'),
    path('forum/<slug:slug>/<pk>/update/', answer.AnswerUpdate.as_view(),
         name='answer_update'),
    path('forum/<slug:slug>/<pk>/delete/', answer.AnswerDelete.as_view(),
         name='answer_delete'),

    path('<slug:slug>/up', upvote, name='question_upvote'),
    path('<slug:slug>/down', downvote, name='question_downvote'),

    path('<slug:slug>/<pk>/up', upvote, name='answer_upvote'),
    path('<slug:slug>/<pk>/down', downvote, name='answer_downvote'),
    path('<slug:slug>/<pk>/accept', accept, name='answer_accept'),
]
