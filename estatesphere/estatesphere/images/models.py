from django.contrib.auth import get_user_model
from django.db import models
from estatesphere.images.validators import FileSizeValidator
from estatesphere.properties.models import RealEstateProperty

UserModel = get_user_model()


class Image(models.Model):
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    estate_property = models.ForeignKey(to=RealEstateProperty, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='', validators=[FileSizeValidator(5)])
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)