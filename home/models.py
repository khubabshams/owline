from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    score = models.IntegerField(default=0)

    def __str__(self):
        stars = self.score <= 0 and '-' or self.score >= 100 and '*****' \
            or self.score >= 50 and '***' or self.score >= 10 and '**' or \
            self.score >= 1 and '*'
        return f"{self.user.username}\n{stars}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
