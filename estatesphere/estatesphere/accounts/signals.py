from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from estatesphere.accounts.models import Profile
from estatesphere.contacts.models import ChatRoom

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def create_chat_room(sender, instance, created, **kwargs):
    if created:
        ChatRoom.objects.create(user=instance)
