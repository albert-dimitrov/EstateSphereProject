from django.contrib import admin

from estatesphere.images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['estate_property', 'image']
    list_filter = ['estate_property']
    search_fields = ['estate_property__title']
    ordering = ['estate_property_id']




