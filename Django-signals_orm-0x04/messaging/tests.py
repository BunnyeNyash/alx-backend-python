from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.cache import cache
from messaging.models import Message, Notification, MessageHistory

class MessagingTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.sender = User.objects.create_user(username='sender', password='pass')
        self.receiver = User.objects.create_user(username='receiver', password='pass')

    def test_notification_created_on_message(self):
        """Task 0: Test post_save signal creates notification"""
        message = Message.objects.create(
            sender=self.sender, receiver=self.receiver, content='Hello!'
        )
        notification = Notification.objects.filter(user=self.receiver, message=message)
        self.assertTrue(notification.exists())

    def test_message_edit_history(self):
        """Task 1: Test pre_save signal logs edit history with edited_by"""
        message = Message.objects.create(
            sender=self.sender, receiver=self.receiver, content='Original'
        )
        message.content = 'Edited'
        message.save()
        history = MessageHistory.objects.filter(message=message, old_content='Original')
        self.assertTrue(history.exists())
        self.assertEqual(history.first().edited_by, self.sender)
        self.assertTrue(message.edited)

    def test_message_edit_history_view(self):
        """Task 1: Test edit history view renders correctly"""
        self.client.login(username='sender', password='pass')
        message = Message.objects.create(
            sender=self.sender, receiver=self.receiver, content='Original'
        )
        message.content = 'Edited'
        message.save()
        response = self.client.get(reverse('message_edit_history', args=[message.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Original')
        self.assertContains(response, self.sender.username)

    def test_user_deletion_cleanup(self):
        """Task 2: Test post_delete signal cleans up user data"""
        message = Message.objects.create(
            sender=self.sender, receiver=self.receiver, content='Test'
        )
        notification = Notification.objects.create(user=self.receiver, message=message)
        self.sender.delete()
        self.assertFalse(Message.objects.filter(sender=self.sender).exists())
        self.assertFalse(Notification.objects.filter(user=self.sender).exists())

    def test_threaded_conversation(self):
        """Task 3: Test threaded conversation with prefetch_related"""
        parent = Message.objects.create(
            sender=self.sender, receiver=self.receiver, content='Parent'
        )
        reply = Message.objects.create(
            sender=self.receiver, receiver=self.sender, content='Reply', parent_message=parent
        )
        message = Message.objects.prefetch_related('replies').get(id=parent.id)
        self.assertEqual(list(message.replies.all()), [reply])

    def test_unread_messages_manager(self):
        """Task 4: Test UnreadMessagesManager filters unread messages"""
        Message.objects.create(
            sender=self.sender, receiver=self.receiver, content='Unread', read=False
        )
        Message.objects.create(
            sender=self.sender, receiver=self.receiver, content='Read', read=True
        )
        unread = Message.unread.unread_for_user(self.receiver)
        self.assertEqual(unread.count(), 1)
        self.assertEqual(unread[0].content, 'Unread')

    def test_view_cache(self):
        """Task 5: Test conversation_list view caching"""
        self.client.login(username='receiver', password='pass')
        cache.clear()
        response1 = self.client.get(reverse('conversation_list'))
        response2 = self.client.get(reverse('conversation_list'))
        self.assertEqual(response1.content, response2.content)

# create your tests here
