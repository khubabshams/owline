from django.db import models
from django.contrib.auth.models import User
from markupfield.fields import MarkupField


class BasePost(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='created_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='modified_posts')
    modified_on = models.DateTimeField(auto_now=True)
    body = MarkupField(default_markup_type='markdown')
    archive = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
