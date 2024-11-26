from django.urls import path, include
from estatesphere.images import views

urlpatterns = [
    path('add/<int:property_id>/create/', views.add_images_view, name='image-add'),
    path('property/<int:pk>/', include([
        path('details/', views.ImageDetailsView.as_view(), name='image-details'),
    ])),
    path('<int:pk>/delete/', views.DeleteImageView.as_view(), name='image-delete'),
]
