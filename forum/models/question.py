from django.db import models
from .base_post import BasePost
from autoslug import AutoSlugField


class Question(BasePost):
    title = models.CharField(max_length=200, unique=True)
    answered = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title', unique_with='created_on')

    class Meta:
        ordering = ['-created_on']

    def __str__(self) -> str:
        """
        Returned str on the question record
        """
        return self.title
