from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'full_name']
        read_only_fields = ['user_id', 'full_name']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.UUIDField(write_only=True)
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender', 'sender_id', 'message_body', 'sent_at']
        read_only_fields = ['message_id', 'sent_at']

    def validate(self, data):
        """Validate that the sender and conversation exist and are valid."""
        sender_id = data.get('sender_id')
        conversation = data.get('conversation')
        if not User.objects.filter(user_id=sender_id).exists():
            raise serializers.ValidationError("Invalid sender_id: User does not exist.")
        if not conversation.participants.filter(user_id=sender_id).exists():
            raise serializers.ValidationError("Sender must be a participant in the conversation.")
        return data

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    participant_ids = serializers.ListField(
        child=serializers.UUIDField(), write_only=True
    )
    messages = serializers.SerializerMethodField()
    conversation_name = serializers.CharField(read_only=True)

    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants',
            'participant_ids',
            'conversation_name',
            'messages',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['conversation_id', 'created_at', 'updated_at', 'conversation_name']

    def get_messages(self, obj):
        """Retrieve messages for the conversation, ordered by sent_at."""
        messages = obj.messages.order_by('-sent_at')
        return MessageSerializer(messages, many=True).data

    def validate_participant_ids(self, value):
        """Validate that participant_ids are valid and exist."""
        if not value:
            raise serializers.ValidationError("At least one participant_id is required.")
        for pid in value:
            if not User.objects.filter(user_id=pid).exists():
                raise serializers.ValidationError(f"Invalid participant_id: {pid} does not exist.")
        return value

    def create(self, validated_data):
        """Create a new conversation and add participants."""
        participant_ids = validated_data.pop('participant_ids')
        conversation = Conversation.objects.create()
        conversation.participants.set(User.objects.filter(user_id__in=participant_ids))
        return conversation

    def get_conversation_name(self, obj):
        """Generate a conversation name based on participant names."""
        names = [user.get_full_name() for user in obj.participants.all()]
        return ", ".join(names) or "Unnamed Conversation"
