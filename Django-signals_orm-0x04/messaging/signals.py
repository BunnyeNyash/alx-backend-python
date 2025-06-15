from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from messaging.models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Check if message is being updated
        old_message = Message.objects.get(pk=instance.pk)
        if old_message.content != instance.content:
            instance.edited = True
            MessageHistory.objects.create(
                message=instance,
                old_content=old_message.content
                edited_by=instance.sender  # Assume sender is the editor
            )

@receiver(post_delete, sender=User)
def cleanup_user_data(sender, instance, **kwargs):
    # Delete messages where user is sender or receiver
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    # Delete notifications for the user
    Notification.objects.filter(user=instance).delete()
    # Delete message history (handled by CASCADE)
    
