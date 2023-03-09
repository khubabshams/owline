from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField()
    body = models.TextField()
    archive = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"From {self.email}"
