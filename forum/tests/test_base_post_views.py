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
        self.assertEqual(self.Question1.votes, 1)
        self.assertEqual(self.AdminUser.profile.score, 1)
        self.assertIn(self.RegularUser.id, voter_ids)
        self.assertIn('Your vote has been signed successfully.', messages)
        self.assertEqual(question_upvote_response.url,
                         f'/forum/{self.Question1.slug}/')
