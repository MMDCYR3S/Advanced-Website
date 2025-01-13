from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


# Create a custom User Manager to manage users
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique
    identifiers for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with email and password and
        extra fields.
        """
        if not email:
            raise ValueError(_("The email must be set!"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser with email and password and
        extra fields.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") != True:
            raise ValueError(_("Superuser must have staff permission!"))
        
        if extra_fields.get("is_superuser") != True:
            raise ValueError(_("Superuser must have superuser permission!"))
        
        return self.create_user(email, password, **extra_fields)

# Create CustomUser for controlling user login/signup
class User(AbstractBaseUser, PermissionsMixin):
    """
    This is a User Model where It gets email as username.
    """
    email = models.EmailField(max_length=200, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

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
