from django.db import models

from core.models import TimeStampedModel


class Review(TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.PositiveSmallIntegerField()
    communication = models.PositiveSmallIntegerField()
    cleanliness = models.PositiveSmallIntegerField()
    location = models.PositiveSmallIntegerField()
    check_in = models.PositiveSmallIntegerField()
    value = models.PositiveSmallIntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room}'
