from django.urls import path, include
from estatesphere.properties import views

urlpatterns = [
    path('add/', views.PropertyAddView.as_view(), name='property-add'),
    path('<int:pk>/', include([
        path('details/', views.PropertyDetailsView.as_view(), name='property-details'),
        path('edit/', views.PropertyEditView.as_view(), name='property-edit'),
        path('delete/', views.PropertyDeleteView.as_view(), name='property-delete'),
    ])),
]