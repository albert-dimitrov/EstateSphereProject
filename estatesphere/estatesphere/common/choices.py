from django.db import models


class RatingChoices(models.IntegerChoices):
    ONE_STAR = 1, '1 Star'
    TWO_STARS = 2, '2 Stars'
    THREE_STARS = 3, '3 Stars'
    FOUR_STAR = 4, '4 Stars'
    FIVE_STARTS = 5, '5 Stars'


