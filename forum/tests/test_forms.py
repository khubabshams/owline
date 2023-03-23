from django.urls import reverse
from django.test import TestCase
from ..forms import AnswerForm


class TestForms(TestCase):

    # Test Answer form
    def test_answer_form_required_field(self):
        answer_form = AnswerForm({'body': ''})
        self.assertFalse(answer_form.is_valid(),
                         "Form with no 'body' should be invalid")
        self.assertIn('body', answer_form.errors.keys(),
                      'Body field should be existed in errors')
        self.assertEqual(answer_form.errors['body'][0],
                         'This field is required.',
                         'User should be notified that body is required')
