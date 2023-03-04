from django.db import models
from .base_post import BasePost
from autoslug import AutoSlugField


class Question(BasePost):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
