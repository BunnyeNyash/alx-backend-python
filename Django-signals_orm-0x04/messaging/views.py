from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from messaging.models import Message
from django.views.decorators.cache import cache_page

# Task 5: Cached conversation list
@cache_page(60)  # Cache for 60 seconds
@login_required
def conversation_list(request):
    messages = Message.objects.filter(receiver=request.user).select_related('sender')
    return render(request, 'messaging/conversation.html', {'messages': messages})

# Task 4: Inbox with unread messages
@login_required
def inbox(request):
    unread_messages = Message.unread.unread_for_user(request.user)  # Uses .only() in manager
    return render(request, 'messaging/inbox.html', {'unread_messages': unread_messages})

# Task 3: Threaded conversation
@login_required
def threaded_conversation(request, message_id):
    message = Message.objects.select_related('sender', 'receiver').prefetch_related('replies').get(id=message_id)
    def get_replies(msg):
        replies = msg.replies.select_related('sender', 'receiver').all()
        return [(r, get_replies(r)) for r in replies]
    replies_tree = get_replies(message)
    return render(request, 'messaging/threaded.html', {'message': message, 'replies_tree': replies_tree})

# Task 2: Delete user account
@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return HttpResponseRedirect(reverse('home'))  # Redirect after deletion

# edit history of a message.
@login_required
def message_edit_history(request, message_id):
    message = get_object_or_404(Message, id=message_id, sender=request.user)
    history = message.history.select_related('edited_by').all()
    return render(request, 'messaging/edit_history.html', {'message': message, 'history': history})


# Create your views here.
