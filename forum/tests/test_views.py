from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


from ..models import Question, Answer
from ..views import QuestionCreate, AnswerCreate

USERNAME, PASSWORD, EMAIL = 'username', 'useremail@owline.com', 'PA$$WoRd@23'


class TestViews(TestCase):

    def setUp(self):
        # Login
        self.AdminUser = User.objects.create_superuser(USERNAME, EMAIL,
                                                       PASSWORD)
        self.client.login(username=self.AdminUser.username, password=PASSWORD)
        # Question and Answer creation
        self.Question1 = Question.objects.\
            create(created_by=self.AdminUser, modified_by=self.AdminUser,
                   title='TITLE', body='BODY')
        self.Answer1 = Answer.objects.\
            create(created_by=self.AdminUser, modified_by=self.AdminUser,
                   body='BODY', related_question=self.Question1)

    # Test Question Update View -------------------------------------------------
    def test_question_update_required_fields(self):
        required_title_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'title': 'UPDATED TITLE'})
        required_title_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'body': 'UPDATED BODY'})

        self.Question1.refresh_from_db()
        self.assertEqual(self.Question1.title, 'TITLE')
        self.assertTrue(required_title_response.status_code != 302)
        self.assertEqual(self.Question1.body.raw, 'BODY')
        self.assertTrue(required_title_response.status_code != 302)

    def test_question_update_success(self):
        required_title_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'title': 'UPDATED TITLE', 'body': 'UPDATED BODY'})

        self.Question1.refresh_from_db()
        self.assertEqual(self.Question1.title, 'UPDATED TITLE')
        self.assertTrue(required_title_response.status_code == 302)
        self.assertEqual(self.Question1.body.raw, 'UPDATED BODY')
        self.assertTrue(required_title_response.status_code == 302)
