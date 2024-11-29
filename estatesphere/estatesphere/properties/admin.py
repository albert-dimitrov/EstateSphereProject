from django.contrib import admin

from estatesphere.properties.models import RealEstateProperty


@admin.register(RealEstateProperty)
class RealEstatePropertyAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price', 'area', 'city', 'calculate_price_per_sqm']
    list_filter = ['user', 'title', 'price', 'area', 'city']
    search_fields = ['title', 'price', 'area', 'city']
    ordering = ['price', 'area', 'city']

