from django.test import TestCase
from django.contrib.auth.models import User

from django.urls import reverse
from .models import Message

PASSWORD = 'PA$$WoRd@23'


class TestContactUs(TestCase):

    def setUp(self):
        self.User = User.objects.create_superuser('username',
                                                  'useremail@owline.com',
                                                  PASSWORD)
        self.Message1 = Message.objects.create(name='username',
                                               email='useremail@owline.com',
                                               body='BODY')
        self.client.logout()
        self.client.login(username=self.User.username,
                          password=PASSWORD)

    # Test Message model
    def test_message_defaults(self):
        self.assertTrue(self.Message1.unread,
                        'Message on creation should be marked as unread')
        self.assertFalse(self.Message1.archive,
                         'Message on creation should be marked as un-archived')

    # Test Message CreateView
    def test_message_create_success(self):
        message_create_response = self.client.post(
            reverse('contactus', kwargs={}),
            {'name': self.User.username, 'email': self.User.email,
             'body': 'NEW BODY'})
        message2 = Message.objects.filter(body='NEW BODY').first()
        self.assertNotEqual(message2, None, 'Message should be created')
        self.assertTrue(message2.unread,
                        'Message on creation should be marked as unread')
        self.assertFalse(message2.archive,
                         'Message on creation should be marked as un-archived')

    def test_message_create_required_field(self):
        message_required_email_response = self.client.post(
            reverse('contactus', kwargs={}),
            {'name': self.User.username, 'email': '',
             'body': 'NEW BODY'})
        message_required_body_response = self.client.post(
            reverse('contactus', kwargs={}),
            {'name': self.User.username, 'email': 'useremail2@owline.com',
             'body': ''})
        message2 = Message.objects.filter(body='NEW BODY').first()
        message3 = Message.objects.filter(email='useremail2@owline.com').\
            first()
        self.assertEqual(message2, None, "Message with empty email "
                         "should not be created")
        self.assertEqual(message3, None, "Message with empty body "
                         "should not be created")
