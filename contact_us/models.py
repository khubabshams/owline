from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='messages')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    archive = models.BooleanField(default=False)
