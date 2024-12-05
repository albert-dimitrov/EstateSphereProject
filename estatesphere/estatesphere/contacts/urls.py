from django.urls import path, include
from estatesphere.contacts import views

urlpatterns = [
    path('chatroom/<int:pk>/', include([
        path('', views.ChatRoomDetailView.as_view(), name='chatroom-detail'),
        path('delete/', views.ChatRoomDeleteView.as_view(), name='chatroom-delete'),
    ])),
    path('massage/<int:chat_room_id>/add/', views.AddMassageView.as_view(), name='massage-add'),
]
