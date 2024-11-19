from django.urls import path, include
from estatesphere.images import views

urlpatterns = [
    path('add/', views.ImageAddView.as_view(), name='image-add'),
    path('<int:pk>/', include([
        path('details/', views.ImageDetailsView.as_view(), name='image-details'),
        path('delete/', views.image_delete, name='image-delete'),
    ])),
]
