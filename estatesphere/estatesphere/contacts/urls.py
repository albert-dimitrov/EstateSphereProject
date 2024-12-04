from django.urls import path, include
from estatesphere.contacts import views

urlpatterns = [
    path('chatroom/<int:pk>/', include([
        path('', views.ChatRoomDetailView.as_view(), name='chatroom-detail'),
        path('edit/', views.ChatRoomEditView.as_view(), name='chatroom-edit'),
        path('delete/', views.ChatRoomDeleteView.as_view(), name='chatroom-delete'),
    ])),
    path('massage/add/', views.AddMassageView.as_view(), name='massage-add'),
    path('massage/<int:massage_id>/delete/', views.MassageDeleteView.as_view(), name='massage-delete'),
]
