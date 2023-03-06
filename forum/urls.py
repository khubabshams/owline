from .views import question
from django.urls import path

urlpatterns = [
    path('', question.QuestionList.as_view(), name='home'),
    path('<slug:slug>/', question.QuestionDetail.as_view(), name='question'),
    path('<slug:slug>/update/', question.QuestionUpdate.as_view(),
         name='question_update'),
]
