from django.urls import reverse
from .test_views import TestViews, LOGIN, PASSWORD
from ..models import Answer


class TestAnswerViews(TestViews):

    # Test Answer Create View -----------------------------------------------
    def test_answer_create_success(self):
        answer_create_response = self.client.post(
            reverse('answer_create', kwargs={'slug': self.Question1.slug}),
            {'body': 'NEW ANSWER BODY'})
        answer2 = Answer.objects.filter(body='NEW ANSWER BODY').first()
        answers = list(self.Question1.answers.all())
        self.assertNotEqual(answer2, None)
        self.assertEqual(len(answers), 2)
        self.assertEqual(answer2.related_question, self.Question1)
        self.assertTrue(answer_create_response.status_code == 302)
        self.assertEqual(answer_create_response.url,
                         f'/forum/{self.Question1.slug}/')

    def test_answer_create_required_fields(self):
        required_body_response = self.client.post(
            reverse('answer_create', kwargs={'slug': self.Question1.slug}),
            {'body': ''})
        answer2 = Answer.objects.filter(body='').first()
        answers = list(self.Question1.answers.all())
        self.assertEqual(answer2, None)
        self.assertEqual(len(answers), 1)
        self.assertNotEqual(required_body_response.status_code, 302)

    def test_answer_create_login_required(self):
        self.client.logout()
        anonymous_user_create_response = self.client.post(
            reverse('answer_create', kwargs={'slug': self.Question1.slug}),
            {'body': 'NEW ANSWER BODY'})
        answer2 = Answer.objects.filter(body='NEW ANSWER BODY').first()
        answers = list(self.Question1.answers.all())
        self.assertEqual(answer2, None)
        self.assertEqual(len(answers), 1)
        self.assertEqual(anonymous_user_create_response.status_code, 302)
        self.assertEqual(anonymous_user_create_response.url,
                         f'{LOGIN}?next=/forum/{self.Question1.slug}/create/')

    # Test Answer Update View -----------------------------------------------
    def test_answer_update_success(self):
        answer_update_response = self.client.post(
            reverse('answer_update', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}),
            {'body': 'UPDATED ANSWER BODY'})
        self.Answer1.refresh_from_db()
        self.assertEqual(self.Answer1.body.raw, 'UPDATED ANSWER BODY')
        self.assertTrue(answer_update_response.status_code == 302)
        self.assertEqual(answer_update_response.url,
                         f'/forum/{self.Question1.slug}/')

    def test_answer_update_required_fields(self):
        required_body_response = self.client.post(
            reverse('answer_update', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}),
            {'body': ''})
        self.Answer1.refresh_from_db()
        self.assertEqual(self.Answer1.body.raw, 'BODY')
        self.assertNotEqual(required_body_response.status_code, 302)

    def test_answer_update_login_required(self):
        self.client.logout()
        anonymous_user_update_response = self.client.post(
            reverse('answer_update', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}),
            {'body': 'UPDATED ANSWER BODY'})
        self.Answer1.refresh_from_db()
        self.assertEqual(self.Answer1.body.raw, 'BODY')
        self.assertTrue(anonymous_user_update_response.status_code == 302)
        self.assertEqual(anonymous_user_update_response.url,
                         f'{LOGIN}?next=/forum/{self.Question1.slug}/'
                         f'{self.Answer1.id}/update/')

    # # Test Answer Delete View -----------------------------------------------
    def test_answer_delete_success(self):
        answer_delete_response = self.client.post(
            reverse('answer_delete', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}), {})
        answer1 = Answer.objects.filter(id=self.Answer1.id).first()
        self.assertEqual(answer1, None)
        self.assertEqual(answer_delete_response.status_code, 302)
        self.assertEqual(answer_delete_response.url,
                         f'/forum/{self.Question1.slug}/')

    def test_answer_delete_not_admin(self):
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        not_admin_user_update_response = self.client.post(
            reverse('answer_delete', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}), {})
        answer1 = Answer.objects.filter(id=self.Answer1.id).first()
        self.assertEqual(answer1, None)
        self.assertEqual(not_admin_user_update_response.status_code, 302)
        self.assertEqual(not_admin_user_update_response.url,
                         f'/forum/{self.Question1.slug}/')

    def test_answer_delete_login_required(self):
        self.client.logout()
        anonymous_user_update_response = self.client.post(
            reverse('answer_delete', kwargs={'slug': self.Question1.slug,
                                             'pk': self.Answer1.id}), {})
        answer1 = Answer.objects.filter(id=self.Answer1.id).first()
        self.assertNotEqual(answer1, None)
        self.assertEqual(anonymous_user_update_response.status_code, 302)
        self.assertEqual(anonymous_user_update_response.url,
                         f'{LOGIN}?next=/forum/{self.Question1.slug}/'
                         f'{self.Answer1.id}/delete/')
