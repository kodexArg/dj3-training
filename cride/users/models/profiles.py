from tkinter import CASCADE
from django.db import models

from cride.utils.models import CRideModel


class Profile(CRideModel):
    """
        A profile holds public data like bio, picture and statistics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField('profile picture', upload_to='users/pictures/', blank=True, null=True)
    biography = models.TextField(max_length=500, blank=True)

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(default=5.0, help_text="User's reputation based on rides taken and offered")

    def __str__(self):
        return str(self.user)