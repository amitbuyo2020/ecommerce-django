from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from .managers import CustomUserManager
from django.conf import settings

from django.core.validators import RegexValidator



class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    # The default login field for the user
    USERNAME_FIELD = 'email'

    # The fields required other than email to login by the user
    REQUIRED_FIELDS = ['username']


    # An object of the Managers
    objects = CustomUserManager()


STATES = [
    ("Province 1", "Province 1"),
    ("Province 2", "Province 2"),
    ("Bagmati", "Bagmati"),
    ("Gandaki", "Gandaki"),
    ("Lumbini", "Lumbini"),
    ("Karnali", "Karnali"),
    ("SudurPaschim", "SudurPaschim"),
]

class UserProfile(models.Model):

    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', unique=True)
    bio = models.CharField(max_length=150, blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='media')
    address = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True, choices=STATES, default="Bagmati")
    contact = models.CharField(validators = [phoneNumberRegex], null=True, blank=True, max_length = 16, unique = True)


    def __str__(self):
        return f"{self.user.username}"