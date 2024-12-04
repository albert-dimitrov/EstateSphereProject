from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class ChatRoom(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    open = models.BooleanField(default=True)


class Massages(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='massages')
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='massages')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
