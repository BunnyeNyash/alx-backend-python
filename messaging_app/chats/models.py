from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom User model extending AbstractUser with additional fields."""
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text="User's phone number")
    status = models.CharField(max_length=20, choices=[('online', 'Online'), ('offline', 'Offline')], default='offline')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username


class Conversation(models.Model):
    """Model to track conversations between users."""
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation {self.id} ({len(self.participants.all())} participants)"


class Message(models.Model):
    """Model for messages within a conversation."""
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message by {self.sender.username} in Conversation {self.conversation.id}"
