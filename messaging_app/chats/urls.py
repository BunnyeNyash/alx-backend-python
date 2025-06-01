from django.urls import path, include
import rest_framework.routers
from .views import ConversationViewSet, MessageViewSet

router = rest_framework.routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
