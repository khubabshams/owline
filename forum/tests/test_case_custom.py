from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from ..models import BasePost, Question, Answer
from ..views import QuestionCreate, AnswerCreate

USERNAME, USERNAME2, PASSWORD, EMAIL = 'username', 'username2', \
    'useremail@owline.com', 'PA$$WoRd@23'
LOGIN = '/accounts/login/'


class TestCaseCustom(TestCase):

    def setUp(self):
        # Login
        self.AdminUser = User.objects.create_superuser(USERNAME, EMAIL,
                                                       PASSWORD)
        self.RegularUser = User.objects.create_user(username=USERNAME2,
                                                    email=EMAIL,
                                                    password=PASSWORD,
                                                    is_superuser=False)
        self.client.login(username=self.AdminUser.username, password=PASSWORD)
        self.BasePost1 = BasePost.objects.\
            create(created_by=self.AdminUser, modified_by=self.AdminUser,
                   body='BODY')
        self.Question1 = Question.objects.\
            create(created_by=self.AdminUser, modified_by=self.AdminUser,
                   title='TITLE', body='BODY')
        self.Answer1 = Answer.objects.\
            create(created_by=self.RegularUser, modified_by=self.RegularUser,
                   body='BODY', related_question=self.Question1)
