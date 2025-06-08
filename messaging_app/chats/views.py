from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation

class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for listing and creating conversations.
    """
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['conversation_id']

    def get_queryset(self):
        """Return conversations where the user is a participant."""
        return self.request.user.conversations.all()

    def perform_create(self, serializer):
        """Create a conversation, including the authenticated user."""
        validated_data = serializer.validated_data
        participant_ids = validated_data.get('participant_ids', [])
        participant_ids = [str(pid) for pid in participant_ids]
        user_id_str = str(self.request.user.user_id)
        if user_id_str not in participant_ids:
            participant_ids.append(user_id_str)
            validated_data['participant_ids'] = participant_ids
        conversation = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for listing and sending messages, supporting flat and nested routes.
    """
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['conversation']

    def get_queryset(self):
        """Filter messages by conversation_id (from URL or query) and user."""
        conversation_id = self.kwargs.get('conversation_conversation_id') or self.request.query_params.get('conversation_id')
        if conversation_id:
            return Message.objects.filter(
                conversation__conversation_id=conversation_id,
                conversation__participants=self.request.user
            )
        return Message.objects.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        """Save a message with the authenticated user as sender."""
        conversation_id = self.kwargs.get('conversation_conversation_id') or serializer.validated_data.get('conversation').conversation_id
        try:
            conversation = Conversation.objects.get(
                conversation_id=conversation_id,
                participants=self.request.user
            )
        except Conversation.DoesNotExist:
            raise serializer.ValidationError("Invalid or unauthorized conversation.")
        message = serializer.save(sender=self.request.user, conversation=conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
