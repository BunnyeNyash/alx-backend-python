from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from messaging.models import Message

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
    
# Create your views here.
