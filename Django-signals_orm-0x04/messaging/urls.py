from django.urls import path
from . import views

urlpatterns = [
    path('conversation/', views.conversation_list, name='conversation_list'),  # Task 5
    path('inbox/', views.inbox, name='inbox'),  # Task 4
    path('thread/<int:message_id>/', views.threaded_conversation, name='threaded_conversation'),  # Task 3
    path('delete-account/', views.delete_user, name='delete_user'),  # Task 2
    path('message/<int:message_id>/history/', views.message_edit_history, name='message_edit_history'),    # edit history view
]
