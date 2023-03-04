from .views import question
from django.urls import path

urlpatterns = [
    path('', views.QuestionList.as_view(), name='home'),
]
