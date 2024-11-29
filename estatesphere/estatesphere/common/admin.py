from django.contrib import admin

from estatesphere.common.models import Favourite, Review


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'estate_property']
    list_filter = ['user',]
    fields = ['user', 'estate_property']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'estate_property', 'rating', 'date_time_of_publication']
    list_filter = ['rating', 'date_time_of_publication', 'estate_property']
    search_fields = ['estate_property__title']
    ordering = ['rating', 'date_time_of_publication']


