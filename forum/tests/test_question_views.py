from django.urls import reverse
from django.http import HttpResponseForbidden

from .test_case_custom import TestCaseCustom, LOGIN, PASSWORD
from ..models import Question


class TestQuestionViews(TestCaseCustom):

    # Test Question Create View -----------------------------------------------
    def test_question_create_success(self) -> None:
        question_create_response = self.client.post(
            reverse('question_create', kwargs={}),
            {'title': 'NEW TITLE', 'body': 'NEW BODY'})
        question2 = Question.objects.filter(slug='new-title').first()
        self.assertEqual(question2.title, 'NEW TITLE',
                         'Title should as exact as the given value')
        self.assertEqual(question2.body.raw, 'NEW BODY',
                         'Body should as exact as the given value')
        self.assertTrue(question_create_response.status_code == 302,
                        'User should be redirect to created question')
        self.assertEqual(question_create_response.url,
                         f'/forum/{question2.slug}/',
                         'User should be redirect to created question')

    def test_question_create_required_fields(self) -> None:
        required_body_response = self.client.post(
            reverse('question_create', kwargs={}),
            {'title': 'NEW TITLE'})
        required_title_response = self.client.post(
            reverse('question_create', kwargs={}),
            {'body': 'NEW BODY'})
        question2 = Question.objects.filter(slug='new-title').first()
        question3 = Question.objects.filter(body='NEW BODY').first()
        self.assertEqual(question2, None,
                         'Question with no body should not be created.')
        self.assertEqual(question3, None,
                         'Question with no title should not be created.')

    def test_question_create_login_required(self) -> None:
        self.client.logout()
        anonymous_user_create_response = self.client.post(
            reverse('question_create', kwargs={}),
            {'title': 'NEW TITLE', 'body': 'NEW BODY'})
        question2 = Question.objects.filter(slug='new-title').first()
        self.assertEqual(question2, None,
                         'Anonymous users should not be able to ask questions')
        self.assertEqual(anonymous_user_create_response.status_code, 302,
                         'User should be redirect to login')
        self.assertEqual(anonymous_user_create_response.url,
                         f'{LOGIN}?next=/forum/create/',
                         'User should be redirect to login and next to'
                         ' create question')

    # Test Question Update View -----------------------------------------------
    def test_question_update_success(self) -> None:
        question_update_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'title': 'UPDATED TITLE', 'body': 'UPDATED BODY'})
        self.Question1.refresh_from_db()
        self.assertEqual(self.Question1.title, 'UPDATED TITLE',
                         'Title should be updated.')
        self.assertEqual(self.Question1.body.raw, 'UPDATED BODY',
                         'Body should be updated.')
        self.assertTrue(question_update_response.status_code == 302,
                        'User should be redirect to updated question')
        self.assertEqual(question_update_response.url,
                         f'/forum/{self.Question1.slug}/',
                         'User should be redirect to updated question')

    def test_question_update_required_fields(self) -> None:
        required_body_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'title': 'UPDATED TITLE'})
        required_title_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'body': 'UPDATED BODY'})
        self.Question1.refresh_from_db()
        self.assertEqual(self.Question1.title, 'TITLE',
                         'Question with no body should not be updated.')
        self.assertEqual(self.Question1.body.raw, 'BODY',
                         'Question with no title should not be updated.')
        self.assertNotEqual(required_title_response.status_code, 302,
                            'User should be redirect to related question')
        self.assertNotEqual(required_body_response.status_code, 302,
                            'User should be redirect to related question')

    def test_question_update_login_required(self) -> None:
        self.client.logout()
        anonymous_user_update_response = self.client.post(
            reverse('question_update', kwargs={'slug': self.Question1.slug}),
            {'title': 'UPDATED TITLE', 'body': 'UPDATED BODY'})
        self.Question1.refresh_from_db()
        self.assertEqual(self.Question1.title, 'TITLE',
                         'Anonymous users should not be able to update'
                         ' questions')
        self.assertTrue(anonymous_user_update_response.status_code == 302,
                        'User should be redirect to login')
        self.assertEqual(anonymous_user_update_response.url,
                         f'{LOGIN}?next=/forum/{self.Question1.slug}/update/',
                         'User should be redirect to login next to update'
                         ' question')

    # Test Question Delete View -----------------------------------------------
    def test_question_delete_success(self) -> None:
        question_delete_response = self.client.post(
            reverse('question_delete', kwargs={'slug': self.Question1.slug}),
            {})
        question1 = Question.objects.filter(slug=self.Question1.slug).first()
        self.assertEqual(question1, None, 'Question should be deleted')
        self.assertEqual(question_delete_response.status_code, 302,
                         'User should be redirect to home')
        self.assertEqual(question_delete_response.url, '/',
                         'User should be redirect to home')

    def test_question_delete_not_admin(self) -> None:
        self.client.logout()
        self.client.login(username=self.RegularUser.username,
                          password=PASSWORD)
        not_admin_user_delete_response = self.client.post(
            reverse('question_delete', kwargs={'slug': self.Question1.slug}),
            {})
        question1 = Question.objects.filter(slug=self.Question1.slug).first()
        self.assertNotEqual(question1, None,
                            'Not admin user should not be able to delete'
                            ' questions')
        self.assertTrue(isinstance(not_admin_user_delete_response,
                                   HttpResponseForbidden),
                        'User should be redirect to forbidden error page')

    def test_question_delete_login_required(self) -> None:
        self.client.logout()
        anonymous_user_delete_response = self.client.post(
            reverse('question_delete', kwargs={'slug': self.Question1.slug}),
            {})
        question1 = Question.objects.filter(slug=self.Question1.slug).first()
        self.assertNotEqual(question1, None, 'Anonymous users should not be'
                            ' able to delete questions')
        self.assertEqual(anonymous_user_delete_response.status_code, 302,
                         'User should be redirect to login page')
        self.assertEqual(anonymous_user_delete_response.url,
                         f'{LOGIN}?next=/forum/{self.Question1.slug}/delete/',
                         'User should be redirect to login page and next'
                         ' to delete form')

    # Test Question List View -------------------------------------------------
    def test_question_list_success(self) -> None:
        home_response = self.client.get(reverse('home', kwargs={}), {})
        forum_response = self.client.get(reverse('forum', kwargs={}), {})
        home_context = home_response.context
        forum_context = forum_response.context
        questions = Question.objects.filter(slug=self.Question1.slug)
        self.assertEqual(list(questions),
                         list(home_context['question_list']),
                         'Filtered question should equal returned question')
        self.assertEqual(list(questions),
                         list(forum_context['question_list']),
                         'Filtered question should equal returned question')
        self.assertEqual(home_response.status_code, 200,
                         'Response should return success status code')
        self.assertEqual(forum_response.status_code, 200,
                         'Response should return success status code')
        self.assertEqual(home_response.wsgi_request.path, f'/',
                         'User should be redirect to "/"')
        self.assertEqual(forum_response.wsgi_request.path, f'/forum/',
                         'User should be redirect to "/forum"')

    # Test Question Details View ----------------------------------------------
    def test_question_details_success(self) -> None:
        question_details_response = self.client.get(
            reverse('question_details', kwargs={'slug': self.Question1.slug}),
            {})
        context = question_details_response.context
        self.assertEqual(self.Question1, context['question'],
                         'Question in details view should equal to given'
                         ' question')
        self.assertEqual(list(self.Question1.answers.all()),
                         list(context['answers']),
                         'Answers in details view should equal to answers'
                         ' of the given question')
        self.assertEqual(question_details_response.status_code, 200,
                         'Response should return success status code')
        self.assertEqual(question_details_response.wsgi_request.path,
                         f'/forum/{self.Question1.slug}/',
                         'User should be redirect to related question')

    # Test Question Search View ----------------------------------------------
    def test_question_search_success(self) -> None:
        question2 = Question.objects.\
            create(created_by=self.AdminUser, modified_by=self.AdminUser,
                   title='TITLE TWO', body='ANOTHER BODY!')
        question3 = Question.objects.\
            create(created_by=self.AdminUser, modified_by=self.AdminUser,
                   title='TITLE THREE', body='ANOTHER BODY!')

        question_search_body_response = self.client.post(
            reverse('question_search', kwargs={}),
            {'search': 'body'})
        question_search_another_response = self.client.post(
            reverse('question_search', kwargs={}),
            {'search': 'ANOtheR'})
        question_search_three_response = self.client.post(
            reverse('question_search', kwargs={}),
            {'search': 'tHREE'})

        context_body = question_search_body_response.context
        context_another = question_search_another_response.context
        context_three = question_search_three_response.context

        self.assertEqual(len(context_body['question_list']), 3,
                         'Search with the word "body" should bring three'
                         ' results')
        self.assertEqual(len(context_another['question_list']), 2,
                         'Search with the word "ANOtheR" should bring two'
                         ' results, case ignored.')
        self.assertEqual(len(context_three['question_list']), 1,
                         'Search with the word "ANOtheR" should bring only one'
                         ' result, case ignored.')
        self.assertEqual(question_search_body_response.status_code, 200)
        self.assertEqual(question_search_body_response.wsgi_request.path,
                         f'/forum/search/')
