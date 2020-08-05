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
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.review} - {self.room}'

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = 'Avg.'
