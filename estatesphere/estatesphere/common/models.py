from django.contrib.auth import get_user_model
from django.db import models

from estatesphere.common.choices import RatingChoices
from estatesphere.properties.models import RealEstateProperty

UserModel = get_user_model()


class Favourite(models.Model):
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    estate_property = models.ForeignKey(to=RealEstateProperty, on_delete=models.CASCADE, related_name='favourites')


class Review(models.Model):
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    estate_property = models.ForeignKey(to=RealEstateProperty, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(max_length=300)
    rating = models.IntegerField(choices=RatingChoices.choices)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['date_time_of_publication']),
        ]
        ordering = ['-date_time_of_publication']


