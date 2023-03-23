from django.urls import reverse
from django.contrib.messages import get_messages

from .test_views import TestViews, LOGIN, PASSWORD
from ..models import BasePost, Question, Answer


class TestBasePostViews(TestViews):

    # Test Question Upvote -----------------------------------------------
    def test_question_upvote_success(self):
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        question_upvote_response = self.client.post(
            reverse('question_upvote', kwargs={'slug': self.Question1.slug}),
            {})
        self.Question1.refresh_from_db()
        self.AdminUser.refresh_from_db()
        voter_ids = self.Question1.vote_users.all().values_list('id',
                                                                flat=True)
        messages = [m.message for m in
                    get_messages(question_upvote_response.wsgi_request)]
        self.assertEqual(self.Question1.votes, 1,
                         "User upvote should be counted")
        self.assertEqual(self.AdminUser.profile.score, 1,
                         "Upvote should affect user's score")
        self.assertIn(self.RegularUser.id, voter_ids)
        self.assertIn('Your vote has been signed successfully.', messages,
                      "User should be told that his upvote succeed")
        self.assertEqual(question_upvote_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    def test_question_upvote_twice(self):
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        question_first_upvote_response = self.client.post(
            reverse('question_upvote', kwargs={'slug': self.Question1.slug}),
            {})
        question_second_upvote_response = self.client.post(
            reverse('question_upvote', kwargs={'slug': self.Question1.slug}),
            {})
        self.Question1.refresh_from_db()
        self.AdminUser.refresh_from_db()
        messages = [m.message for m in
                    get_messages(question_second_upvote_response.
                                 wsgi_request)]
        self.assertEqual(self.Question1.votes, 1,
                         "Only first upvote should be counted")
        self.assertEqual(self.AdminUser.profile.score, 1,
                         "Only first upvote score should be counted")
        self.assertIn('You cannot sign a vote twice for a question.',
                      messages, "User must be warned for voting twice")
        self.assertEqual(question_second_upvote_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    def test_question_upvote_by_owner(self):
        question_upvote_by_owner_response = self.client.post(
            reverse('question_upvote', kwargs={'slug': self.Question1.slug}),
            {})
        self.Question1.refresh_from_db()
        self.AdminUser.refresh_from_db()
        messages = [m.message for m in
                    get_messages(question_upvote_by_owner_response.
                                 wsgi_request)]
        self.assertEqual(self.Question1.votes, 0,
                         "Owner upvote should not be counted")
        self.assertEqual(self.AdminUser.profile.score, 0,
                         "Owner upvote should not affect his score")
        self.assertIn('You cannot sign a vote for a question of your own.',
                      messages, "User must be warned for voting for his own"
                      " question")
        self.assertEqual(question_upvote_by_owner_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    # Test Question Downvote -----------------------------------------------
    def test_question_downvote_success(self):
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        question_downvote_response = self.client.post(
            reverse('question_downvote', kwargs={'slug': self.Question1.slug}),
            {})
        self.Question1.refresh_from_db()
        self.AdminUser.refresh_from_db()
        voter_ids = self.Question1.vote_users.all().values_list('id',
                                                                flat=True)
        messages = [m.message for m in
                    get_messages(question_downvote_response.wsgi_request)]
        self.assertEqual(self.Question1.votes, -1,
                         "User downvote should be counted")
        self.assertEqual(self.AdminUser.profile.score, -1,
                         "Downvote should affect user's score")
        self.assertIn(self.RegularUser.id, voter_ids)
        self.assertIn('Your vote has been signed successfully.', messages,
                      "User should be told that his downvote succeed")
        self.assertEqual(question_downvote_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    def test_question_downvote_twice(self):
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        question_first_downvote_response = self.client.post(
            reverse('question_downvote', kwargs={'slug': self.Question1.slug}),
            {})
        question_second_downvote_response = self.client.post(
            reverse('question_downvote', kwargs={'slug': self.Question1.slug}),
            {})
        self.Question1.refresh_from_db()
        self.AdminUser.refresh_from_db()
        messages = [m.message for m in
                    get_messages(question_second_downvote_response.
                                 wsgi_request)]
        self.assertEqual(self.Question1.votes, -1,
                         "Only first downvote should be counted")
        self.assertEqual(self.AdminUser.profile.score, -1,
                         "Only first downvote score should be counted")
        self.assertIn('You cannot sign a vote twice for a question.',
                      messages, "User must be warned for voting twice")
        self.assertEqual(question_second_downvote_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    def test_question_downvote_by_owner(self):
        question_downvote_by_owner_response = self.client.post(
            reverse('question_downvote', kwargs={'slug': self.Question1.slug}),
            {})
        self.Question1.refresh_from_db()
        self.AdminUser.refresh_from_db()
        messages = [m.message for m in
                    get_messages(question_downvote_by_owner_response.
                                 wsgi_request)]
        self.assertEqual(self.Question1.votes, 0,
                         "Owner downvote should not be counted")
        self.assertEqual(self.AdminUser.profile.score, 0,
                         "Owner downvote should not affect his score")
        self.assertIn('You cannot sign a vote for a question of your own.',
                      messages, "User must be warned for voting for his own"
                      " question")
        self.assertEqual(question_downvote_by_owner_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    # Test Answer Upvote -----------------------------------------------
    def test_answer_upvote_success(self):
        answer_upvote_response = self.client.post(
            reverse('answer_upvote', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}), {})
        self.Answer1.refresh_from_db()
        self.RegularUser.refresh_from_db()
        voter_ids = self.Answer1.vote_users.all().values_list('id',
                                                              flat=True)
        messages = [m.message for m in
                    get_messages(answer_upvote_response.wsgi_request)]
        self.assertEqual(self.Answer1.votes, 1,
                         "User upvote should be counted")
        self.assertEqual(self.RegularUser.profile.score, 1,
                         "Upvote should affect user's score")
        self.assertIn(self.AdminUser.id, voter_ids)
        self.assertIn('Your vote has been signed successfully.', messages,
                      "User should be told that his upvote succeed")
        self.assertEqual(answer_upvote_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    def test_answer_upvote_twice(self):
        answer_first_upvote_response = self.client.post(
            reverse('answer_upvote', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}), {})
        answer_second_upvote_response = self.client.post(
            reverse('answer_upvote', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}), {})
        self.Answer1.refresh_from_db()
        self.RegularUser.refresh_from_db()
        messages = [m.message for m in
                    get_messages(answer_second_upvote_response.
                                 wsgi_request)]
        self.assertEqual(self.Answer1.votes, 1,
                         "Only first upvote should be counted")
        self.assertEqual(self.RegularUser.profile.score, 1,
                         "Only first upvote score should be counted")
        self.assertIn('You cannot sign a vote twice for an answer.',
                      messages, "User must be warned for voting twice")
        self.assertEqual(answer_second_upvote_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    def test_answer_upvote_by_owner(self):
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        answer_upvote_by_owner_response = self.client.post(
            reverse('answer_upvote', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}), {})
        self.Answer1.refresh_from_db()
        self.RegularUser.refresh_from_db()
        messages = [m.message for m in
                    get_messages(answer_upvote_by_owner_response.
                                 wsgi_request)]
        self.assertEqual(self.Answer1.votes, 0,
                         "Owner upvote should not be counted")
        self.assertEqual(self.RegularUser.profile.score, 0,
                         "Owner upvote should not affect his score")
        self.assertIn('You cannot sign a vote for an answer of your own.',
                      messages, "User must be warned for voting for his own"
                      " question")
        self.assertEqual(answer_upvote_by_owner_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    # Test Answer Downvote -----------------------------------------------
    def test_answer_downvote_success(self):
        answer_downvote_response = self.client.post(
            reverse('answer_downvote', kwargs={'slug': self.Question1.slug,
                                               'pk': self.Answer1.id}), {})
        self.Answer1.refresh_from_db()
        self.RegularUser.refresh_from_db()
        voter_ids = self.Answer1.vote_users.all().values_list('id',
                                                              flat=True)
        messages = [m.message for m in
                    get_messages(answer_downvote_response.wsgi_request)]
        self.assertEqual(self.Answer1.votes, -1,
                         "User downvote should be counted")
        self.assertEqual(self.RegularUser.profile.score, -1,
                         "Downvote should affect user's score")
        self.assertIn(self.AdminUser.id, voter_ids)
        self.assertIn('Your vote has been signed successfully.', messages,
                      "User should be told that his downvote succeed")
        self.assertEqual(answer_downvote_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    def test_answer_downvote_twice(self):
        answer_first_downvote_response = self.client.post(
            reverse('answer_downvote', kwargs={'slug': self.Question1.slug,
                                               'pk': self.Answer1.id}), {})
        answer_second_downvote_response = self.client.post(
            reverse('answer_downvote', kwargs={'slug': self.Question1.slug,
                                               'pk': self.Answer1.id}), {})
        self.Answer1.refresh_from_db()
        self.RegularUser.refresh_from_db()
        messages = [m.message for m in
                    get_messages(answer_second_downvote_response.
                                 wsgi_request)]
        self.assertEqual(self.Answer1.votes, -1,
                         "Only first downvote should be counted")
        self.assertEqual(self.RegularUser.profile.score, -1,
                         "Only first downvote score should be counted")
        self.assertIn('You cannot sign a vote twice for an answer.',
                      messages, "User must be warned for voting twice")
        self.assertEqual(answer_second_downvote_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    def test_answer_downvote_by_owner(self):
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        answer_downvote_by_owner_response = self.client.post(
            reverse('answer_downvote', kwargs={'slug': self.Question1.slug,
                                               'pk': self.Answer1.id}), {})
        self.Answer1.refresh_from_db()
        self.RegularUser.refresh_from_db()
        messages = [m.message for m in
                    get_messages(answer_downvote_by_owner_response.
                                 wsgi_request)]
        self.assertEqual(self.Answer1.votes, 0,
                         "Owner downvote should not be counted")
        self.assertEqual(self.RegularUser.profile.score, 0,
                         "Owner downvote should not affect his score")
        self.assertIn('You cannot sign a vote for an answer of your own.',
                      messages, "User must be warned for voting for his own"
                      " question")
        self.assertEqual(answer_downvote_by_owner_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")

    # Test Answer Accept -----------------------------------------------
    def test_answer_accept_success(self):
        answer_accept_response = self.client.post(
            reverse('answer_accept', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}), {})
        self.Answer1.refresh_from_db()
        self.RegularUser.refresh_from_db()
        messages = [m.message for m in
                    get_messages(answer_accept_response.wsgi_request)]
        self.assertEqual(self.Answer1.votes, 3,
                         "Acceptance score should be counted")
        self.assertEqual(self.RegularUser.profile.score, 3,
                         "Acceptance should affect user's score")
        self.assertIn('an Answer has been accepted successfully.', messages,
                      "User should be told that his acceptance succeed")
        self.assertEqual(answer_accept_response.url,
                         f'/forum/{self.Question1.slug}/',
                         "User must be redirect to related question")
