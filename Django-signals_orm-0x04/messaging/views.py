from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from messaging.models import Message
from django.views.decorators.cache import cache_page

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return HttpResponseRedirect(reverse('home'))  # Redirect after deletion

def threaded_conversation(request, message_id):
    # Fetch message and its replies efficiently
    message = Message.objects.select_related('sender', 'receiver').prefetch_related('replies').get(id=message_id)
    # Recursive function to collect all replies
    def get_replies(msg):
        replies = msg.replies.select_related('sender', 'receiver').all()
        return [(r, get_replies(r)) for r in replies]
    replies_tree = get_replies(message)
    return render(request, 'messaging/threaded.html', {'message': message, 'replies_tree': replies_tree})

def inbox(request):
    unread_messages = Message.unread.unread_for_user(request.user)
    return render(request, 'messaging/inbox.html', {'unread_messages': unread_messages})

@cache_page(60)  # Cache for 60 seconds
def conversation_list(request):
    messages = Message.objects.filter(receiver=request.user).select_related('sender')
    return render(request, 'messaging/conversation.html', {'messages': messages})
m

# Create your views here.
