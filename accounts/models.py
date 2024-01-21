from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserAccountPortfolio(models.Model):
    """
    Store user values with a fixed balance.
    More information can be find in markets app/models.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=4, default=10000.0) 


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates and updates the UserAccountPortfolio
    with saving new user registration users
    """
    if created:
        UserAccountPortfolio.objects.create(user=instance)

    instance.useraccountportfolio.save()  # Existing users: just save the profile
