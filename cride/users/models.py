from django.db import models
from django.contrib.auth.models import AbstractUser

from cride.utils.models import CRideModels


class User(CRideModels, AbstractUser):
    """
        Extend from Djang's Abastract User, change the username field to email and add some extra fields
    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_message={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_number = models.CharField()