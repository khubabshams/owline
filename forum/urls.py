from .views import question, answer
from django.urls import path

urlpatterns = [
    path('', question.QuestionList.as_view(), name='home'),
    path('<slug:slug>/', question.QuestionDetail.as_view(), name='question'),
    path('<slug:slug>/update/', question.QuestionUpdate.as_view(),
         name='question_update'),
    path('<slug:slug>/delete/', question.QuestionDelete.as_view(),
         name='question_delete'),

    path('<slug:slug>/<pk>/update/', answer.AnswerUpdate.as_view(),
         name='answer_update'),
    path('<slug:slug>/<pk>/delete/', answer.AnswerDelete.as_view(),
         name='answer_delete'),
]
