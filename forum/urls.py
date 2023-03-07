from .views import question, answer
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
]
