from django.db import models
from .base_post import BasePost
from .question import Question


class Answer(BasePost):
    accepted = models.BooleanField(default=False)
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                         related_name='answers')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.body
