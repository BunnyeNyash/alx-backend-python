from rest_framework import permissions
from .models import Conversation

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only participants of a conversation to access its messages.
    Allows authenticated users to view and create, but restricts update/delete to participants.
    """
    def has_permission(self, request, view):
        # Allow authenticated users for safe methods (GET, POST) and restrictive methods (PUT, PATCH, DELETE)
        if not (request.user and request.user.is_authenticated):
            return False
        # For PUT, PATCH, DELETE, additional object-level checks will apply
        return True

    def has_object_permission(self, request, view, obj):
        # For safe methods (GET), allow participants to view
        if request.method in permissions.SAFE_METHODS:
            if isinstance(obj, Conversation):
                return obj.participants.filter(user_id=request.user.user_id).exists()
            return obj.conversation.participants.filter(user_id=request.user.user_id).exists()
        # For PUT, PATCH, DELETE, only allow participants
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if isinstance(obj, Conversation):
                return obj.participants.filter(user_id=request.user.user_id).exists()
            return obj.conversation.participants.filter(user_id=request.user.user_id).exists()
        return False
