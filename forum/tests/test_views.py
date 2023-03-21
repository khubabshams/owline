from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


from ..models import Question, Answer
from ..views import QuestionCreate, AnswerCreate

USERNAME, USERNAME2, PASSWORD, EMAIL = 'username', 'username2', \
    'useremail@owline.com', 'PA$$WoRd@23'
LOGIN = '/accounts/login/'


class TestViews(TestCase):

    def setUp(self):
        # Login
        self.AdminUser = User.objects.create_superuser(USERNAME, EMAIL,
                                                       PASSWORD)
        self.RegularUser = User.objects.create(username=USERNAME2,
                                               email=EMAIL, password=PASSWORD)
        self.client.login(username=self.AdminUser.username, password=PASSWORD)
        # Question and Answer creation
        self.Question1 = Question.objects.\
            create(created_by=self.AdminUser, modified_by=self.AdminUser,
                   title='TITLE', body='BODY')
        self.Answer1 = Answer.objects.\
            create(created_by=self.AdminUser, modified_by=self.AdminUser,
                   body='BODY', related_question=self.Question1)

    # Test Question Create View -----------------------------------------------
    def test_question_create_success(self):
        question_create_response = self.client.post(
            reverse('question_create', kwargs={}),
            {'title': 'NEW TITLE', 'body': 'NEW BODY'})
        question2 = Question.objects.filter(slug='new-title').first()
        self.assertEqual(question2.title, 'NEW TITLE')
        self.assertEqual(question2.body.raw, 'NEW BODY')
        self.assertTrue(question_create_response.status_code == 302)
        self.assertEqual(question_create_response.url,
                         f'/forum/{question2.slug}/')

    def test_question_create_required_fields(self):
        required_body_response = self.client.post(
            reverse('question_create', kwargs={}),
            {'title': 'NEW TITLE'})
        required_title_response = self.client.post(
            reverse('question_create', kwargs={}),
            {'body': 'NEW BODY'})

        question2 = Question.objects.filter(slug='new-title').first()
        question3 = Question.objects.filter(body='NEW BODY').first()
        self.assertEqual(question2, None)
        self.assertEqual(question3, None)
        self.assertNotEqual(required_title_response.status_code, 302)
        self.assertNotEqual(required_body_response.status_code, 302)

    def test_question_create_login_required(self):
        self.client.logout()
        anonymous_user_create_response = self.client.post(
            reverse('question_create', kwargs={}),
            {'title': 'NEW TITLE', 'body': 'NEW BODY'})

        question2 = Question.objects.filter(slug='new-title').first()
        self.assertEqual(question2, None)
        self.assertEqual(anonymous_user_create_response.status_code, 302)
        self.assertEqual(anonymous_user_create_response.url,
                         f'{LOGIN}?next=/forum/create/')

    # Test Question Update View -----------------------------------------------
    def test_question_update_success(self):
        question_update_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'title': 'UPDATED TITLE', 'body': 'UPDATED BODY'})
        self.Question1.refresh_from_db()
        self.assertEqual(self.Question1.title, 'UPDATED TITLE')
        self.assertEqual(self.Question1.body.raw, 'UPDATED BODY')
        self.assertTrue(question_update_response.status_code == 302)
        self.assertEqual(question_update_response.url,
                         f'/forum/{self.Question1.slug}/')

    def test_question_update_required_fields(self):
        required_body_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'title': 'UPDATED TITLE'})
        required_title_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'body': 'UPDATED BODY'})
        self.Question1.refresh_from_db()
        self.assertEqual(self.Question1.title, 'TITLE')
        self.assertEqual(self.Question1.body.raw, 'BODY')
        self.assertNotEqual(required_title_response.status_code, 302)
        self.assertNotEqual(required_body_response.status_code, 302)

    def test_question_update_login_required(self):
        self.client.logout()
        anonymous_user_update_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'title': 'UPDATED TITLE', 'body': 'UPDATED BODY'})
        self.Question1.refresh_from_db()
        self.assertEqual(self.Question1.title, 'TITLE')
        self.assertTrue(anonymous_user_update_response.status_code == 302)
        self.assertEqual(anonymous_user_update_response.url,
                         f'{LOGIN}?next=/forum/{self.Question1.slug}/update/')

    # Test Question Delete View -----------------------------------------------
    def test_question_delete_success(self):
        question_delete_response = self.client.post(
            reverse('question_delete', kwargs={'slug': self.Question1.slug}),
            {})
        question1 = Question.objects.filter(slug=self.Question1.slug).first()
        self.assertEqual(question1, None)
        self.assertEqual(question_delete_response.status_code, 302)
        self.assertEqual(question_delete_response.url, '/')

    def test_question_delete_not_admin(self):
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        not_admin_user_update_response = self.client.post(
            reverse('question_delete', kwargs={'slug': self.Question1.slug}),
            {})
        question1 = Question.objects.filter(slug=self.Question1.slug).first()
        self.assertNotEqual(question1, None)
        self.assertEqual(not_admin_user_update_response.status_code, 302)
        self.assertEqual(not_admin_user_update_response.url,
                         f'{LOGIN}?next=/forum/{self.Question1.slug}/delete/')

    def test_question_delete_login_required(self):
        self.client.logout()
        anonymous_user_update_response = self.client.post(
            reverse('question_delete', kwargs={'slug': self.Question1.slug}),
            {})
        question1 = Question.objects.filter(slug=self.Question1.slug).first()
        self.assertNotEqual(question1, None)
        self.assertEqual(anonymous_user_update_response.status_code, 302)
        self.assertEqual(anonymous_user_update_response.url,
                         f'{LOGIN}?next=/forum/{self.Question1.slug}/delete/')

    # Test Question Details View ----------------------------------------------
    def test_question_details_success(self):
        question_details_response = self.client.get(
            reverse('question_details', kwargs={'slug': self.Question1.slug}),
            {})
        context = question_details_response.context
        self.assertEqual(self.Question1, context['question'])
        self.assertEqual(list(self.Question1.answers.all()),
                         list(context['answers']))
        self.assertEqual(question_details_response.status_code, 200)
        self.assertEqual(question_details_response.wsgi_request.path,
                         f'/forum/{self.Question1.slug}/')
