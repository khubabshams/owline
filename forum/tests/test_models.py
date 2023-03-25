from django.urls import reverse
from .test_case_custom import TestCaseCustom
from ..models import BasePost, Question, Answer


class TestModels(TestCaseCustom):

    # Test BasePost model
    def test_base_post_defaults(self) -> None:
        self.assertFalse(self.BasePost1.archive,
                         "Post should not created as an archived")
        self.assertEqual(self.BasePost1.votes, 0,
                         "Default post vote is zero")

    # Test Question model
    def test_question_defaults(self) -> None:
        self.assertFalse(self.Question1.answered,
                         "Question should not created as an answered")
        self.assertEqual(self.Question1.votes, 0,
                         "Default question vote is zero")

    # Test Answer model
    def test_answer_defaults(self) -> None:
        self.assertFalse(self.Answer1.accepted,
                         "Answer should not created as an accepted")
        self.assertEqual(self.Answer1.votes, 0,
                         "Default answer vote is zero")
