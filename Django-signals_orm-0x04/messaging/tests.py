from django.test import TestCase
from django.contrib.auth.models import User
from messaging.models import Message, Notification

class NotificationSignalTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='pass')
        self.receiver = User.objects.create_user(username='receiver', password='pass')

    def test_notification_created_on_message(self):
        message = Message.objects.create(
            sender=self.sender, receiver=self.receiver, content='Hello!'
        )
        notification = Notification.objects.filter(user=self.receiver, message=message)
        self.assertTrue(notification.exists())


    def test_message_edit_history(self):
        message = Message.objects.create(
            sender=self.sender, receiver=self.receiver, content='Original'
        )
        message.content = 'Edited'
        message.save()
        history = MessageHistory.objects.filter(message=message, old_content='Original')
        self.assertTrue(history.exists())
        self.assertTrue(message.edited)
