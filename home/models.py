from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        """
        Returned str on the profile record
        """
        return f"{self.user.username}\n [{self.score} Points]"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a related profile for each user created
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    When save user instance, profile saved
    """
    instance.profile.save()
