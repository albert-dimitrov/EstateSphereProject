from django.urls import path
from estatesphere.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('favourite/<int:property_id>/', views.favourite_functionality, name='favourite'),
    path('review/<int:property_id>/', views.review_functionality, name='review'),
    path('about/', views.about_us_page, name='about')
]