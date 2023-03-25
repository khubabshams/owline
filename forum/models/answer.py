from django.db import models
from .base_post import BasePost
from .question import Question


class Answer(BasePost):
    accepted = models.BooleanField(default=False)
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                         related_name='answers')

    class Meta:
        ordering = ['-votes']

    def __str__(self) -> str:
        """
        Returned str on the answer record
        """
        return self.body.raw
