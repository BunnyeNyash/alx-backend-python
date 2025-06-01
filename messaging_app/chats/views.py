from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for listing and creating conversations.
    Only shows conversations where the authenticated user is a participant.
    """
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return conversations where the authenticated user is a participant."""
        return self.request.user.conversations.all()

    def perform_create(self, serializer):
        """Create a new conversation and ensure the authenticated user is a participant."""
        serializer.save()

class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for listing and sending messages.
    Filters messages by conversation_id (if provided) or by conversations the user is in.
    """
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter messages by conversation_id or by user's conversations."""
        conversation_id = self.request.query_params.get('conversation_id')
        if conversation_id:
            return Message.objects.filter(conversation__conversation_id=conversation_id, conversation__participants=self.request.user)
        return Message.objects.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        """Save a new message with the authenticated user as the sender."""
        serializer.save(sender=self.request.user)
