from django.db import models
from django.contrib.auth.models import User


class BasePost(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='created_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    modifed_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='modified_posts')
    modified_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    archive = models.BooleanField(default=False)
    votes = models.IntegerField()
