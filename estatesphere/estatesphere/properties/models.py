from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class RealEstateProperty(models.Model):
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, related_name='estate_properties')
    title = models.CharField(max_length=50)
    image = models.URLField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.PositiveSmallIntegerField(help_text='The area is in square meters!')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_price_per_sqm(self):
        return f"{self.price / self.area:.2f}"

    def __str__(self):
        return self.title

