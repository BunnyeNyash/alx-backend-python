from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for listing and creating conversations.
    Only shows conversations where the authenticated user is a participant.
    """
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['conversation_id']

    def get_queryset(self):
        """Return conversations where the authenticated user is a participant."""
        return self.request.user.conversations.all()

    def perform_create(self, serializer):
        """Create a new conversation, ensuring the authenticated user is included."""
        validated_data = serializer.validated_data
        participant_ids = validated_data.get('participant_ids', [])
        # Convert UUIDs to strings for consistency with serializer
        participant_ids = [str(pid) for pid in participant_ids]
        # Ensure authenticated user is included
        user_id_str = str(self.request.user.user_id)
        if user_id_str not in participant_ids:
            participant_ids.append(user_id_str)
            validated_data['participant_ids'] = participant_ids
        conversation = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for listing and sending messages.
    Filters messages by conversation_id or by user's conversations.
    """
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['conversation']

    def get_queryset(self):
        """Filter messages by conversation_id or by user's conversations."""
        conversation_id = self.request.query_params.get('conversation_id')
        if conversation_id:
            return Message.objects.filter(
                conversation__conversation_id=conversation_id,
                conversation__participants=self.request.user
            )
        return Message.objects.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        """Save a new message with the authenticated user as the sender."""
        message = serializer.save(sender=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
