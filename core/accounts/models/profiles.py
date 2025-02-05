from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .users import User

# Create a Profile class
class Profile(models.Model):
    """
    This is a Profile model to complete user's information.
    It gets email from User model and then put it in the user
    variable below.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
