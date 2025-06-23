from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This is a "signal receiver". It's a function that runs automatically
# whenever a specific event happens.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    This signal automatically creates a Profile object every time a new User is created.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    This signal automatically saves the profile whenever the User object is saved.
    """
    instance.profile.save()