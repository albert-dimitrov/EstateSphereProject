from django.urls import path, include
from estatesphere.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('favourite/<int:property_id>/', views.favourite_functionality, name='favourite'),
    path('review/add/', views.AddReviewView.as_view(), name='review-add'),
    path('review/<int:property_id>/', include([
        path('edit/', views.EditReviewView.as_view(), name='review-edit'),
        path('delete/', views.DeleteReviewView.as_view(), name='review-delete'),
    ])),
    path('about/', views.about_us_page, name='about'),
]