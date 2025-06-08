from django_filters import rest_framework as filters
from .models import Message, User

class MessageFilter(filters.FilterSet):
    """
    Filter messages by conversation participants or time range.
    """
    participant = filters.UUIDFilter(method='filter_by_participant')
    sent_at__gte = filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    sent_at__lte = filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['conversation', 'sent_at__gte', 'sent_at__lte', 'participant']

    def filter_by_participant(self, queryset, name, value):
        """
        Filter messages by conversations involving a specific participant.
        """
        return queryset.filter(conversation__participants__user_id=value)
