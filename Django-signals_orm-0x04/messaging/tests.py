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
