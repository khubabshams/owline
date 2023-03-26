from django.test import TestCase
from django.contrib.auth.models import User

from django.urls import reverse
from .models import Profile


class TestModels(TestCase):

    def setUp(self) -> None:
        """
        Create the common basic data needed for tests
        """
        self.NewUser = User.objects.create_superuser('username',
                                                     'useremail@owline.com',
                                                     'PA$$WoRd@23')

    # Test Profile model
    def test_user_has_profile(self) -> None:
        self.assertTrue(self.NewUser.profile,
                        "User creation should create a related profile")

    def test_profile_defaults(self) -> None:
        profile = self.NewUser.profile
        self.assertEqual(f'username\n 0v🦉', profile.__str__())
        self.assertEqual(profile.score, 0,
                         "Score on user profile upon creation shoul be zero")
