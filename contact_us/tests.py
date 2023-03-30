from django.test import TestCase
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

from django.urls import reverse
from .models import Message

PASSWORD = 'PA$$WoRd@23'


class TestContactUs(TestCase):

    def setUp(self) -> None:
        """
        Create the common basic data needed for tests
        """
        self.User = User.objects.create_superuser('username',
                                                  'useremail@owline.com',
                                                  PASSWORD)
        self.RegularUser = User.objects.create_user('username2',
                                                    'useremail@owline.com',
                                                    PASSWORD,
                                                    is_superuser=False)
        self.Message1 = Message.objects.create(name='username',
                                               email='useremail@owline.com',
                                               body='BODY')
        self.client.logout()
        self.client.login(username=self.User.username,
                          password=PASSWORD)

    # Test Message model
    def test_message_defaults(self) -> None:
        self.assertEqual(f'From {self.User.email}', self.Message1.__str__())
        self.assertTrue(self.Message1.unread,
                        'Message on creation should be marked as unread')
        self.assertFalse(self.Message1.archive,
                         'Message on creation should be marked as un-archived')

    # Test Message CreateView
    def test_message_create_success(self) -> None:
        message_create_response = self.client.post(
            reverse('contactus', kwargs={}),
            {'name': self.User.username, 'email': self.User.email,
             'body': 'NEW BODY'})
        inbox_response = self.client.get(reverse('inbox',
                                                 kwargs={}), {})
        context = inbox_response.context
        messages = Message.objects.filter(archive=False).\
            order_by('-created_on')
        message2 = Message.objects.filter(body='NEW BODY').first()
        self.assertEqual(list(context['message_list']), list(messages),
                         'Two messages should return in the inbox list')
        self.assertNotEqual(message2, None, 'Message should be created')
        self.assertTrue(message2.unread,
                        'Message on creation should be marked as unread')
        self.assertFalse(message2.archive,
                         'Message on creation should be marked as un-archived')

    def test_message_create_required_field(self) -> None:
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

    def test_message_read(self) -> None:
        read_message_response = self.client.get(
            reverse('message_details', kwargs={'pk': self.Message1.id}), {})
        self.Message1.refresh_from_db()
        context = read_message_response.context
        self.assertEqual(context['message'], self.Message1,
                         'Returned message should be the one created before')
        self.assertEqual(read_message_response.status_code, 200,
                         'Response should return forbidden status code')
        self.assertFalse(self.Message1.unread,
                         'Unread should be marked as false when message'
                         ' opened')

    def test_message_inbox_not_admin(self) -> None:
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        not_admin_inbox_response = self.client.get(reverse('inbox', kwargs={}),
                                                   {})
        not_admin_message_response = self.client.get(
            reverse('message_details', kwargs={'pk': self.Message1.id}), {})
        self.assertEqual(not_admin_inbox_response.status_code, 403,
                         'Response should return forbidden status code')
        self.assertEqual(not_admin_message_response.status_code, 403,
                         'Response should return forbidden status code')
        self.assertTrue(isinstance(not_admin_inbox_response,
                                   HttpResponseForbidden),
                        'User should be redirect to forbidden error page')
        self.assertTrue(isinstance(not_admin_message_response,
                                   HttpResponseForbidden),
                        'User should be redirect to forbidden error page')
