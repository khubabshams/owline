from .views import question
from django.urls import path

urlpatterns = [
    path('', question.QuestionList.as_view(), name='home'),
]
